import torch
import os
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torchvision import datasets,transforms
from tqdm import tqdm
from model.cnn import cnn

device=torch.device("cuda" if torch.cuda.is_available() else "cpu")

train_transformer=transforms.Compose([
    transforms.Resize((224,224)),#将数据裁剪为224*224
    transforms.ToTensor(),#图像转化为 tensor 张量，0-1像素值
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))#标准化，转为(-1,1)
])
test_transformer=transforms.Compose([
    transforms.Resize((224,224)),#将数据裁剪为224*224
    transforms.ToTensor(),#图像转化为 tensor 张量，0-1像素值
    transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))#标准化，转为(-1,1)
])
#定义训练集和测试集
trainset=datasets.ImageFolder(root=r"D:/archive/dataset/train",#拼接路径
                              transform=train_transformer)#进行数据集变换
testset=datasets.ImageFolder(root=r"D:/archive/dataset/test",
                             transform=test_transformer)
#定义数据加载器
train_loader=DataLoader(trainset,batch_size=32,num_workers=0,shuffle=True)
#num_workers 代表多线程进行，为0则不打开
test_loader=DataLoader(testset,batch_size=32,num_workers=0,shuffle=False)

def train(model,train_loader,loss_fuction,optimizer,num_epochs):
    best_acc=0.0
    for epoch in range(num_epochs):
        model.train()
        running_loss=0.0
        for inputs,labels in tqdm(train_loader,desc=f"epoch:{epoch+1}/{num_epochs}",unit="batch"):#训练时可以看到epoch和batch
            inputs,labels=inputs.to(device),labels.to(device)#把数据传到设备上
            optimizer.zero_grad()#梯度清零
            outputs=model(inputs)#前向传播
            loss=loss_fuction(outputs,labels)#loss计算
            loss.backward()#反向传播
            optimizer.step()#更新参数
            running_loss+=loss.item()*inputs.size(0)#用loss×批次大小
        epoch_loss=running_loss/len(train_loader.dataset)#总损失除以数据集大小，为每轮损失
        print(f"epoch:{epoch+1}/{num_epochs} epoch_loss:{epoch_loss}")
        
        accuracy=evaluate(model,test_loader,loss_fuction)
        print(f"accuracy:{accuracy}")
        if accuracy>best_acc:
            best_acc=accuracy
            save_model(model,save_path)

def evaluate(model,test_loader,loss_function):
    model.eval()#指定模式为验证模式
    test_loss=0.0
    correct=0
    total=0
    with torch.no_grad():
        for inputs,labels in test_loader:
            inputs,labels=inputs.to(device),labels.to(device)
            outputs=model(inputs)
            loss=loss_function(outputs,labels)
            test_loss+=loss.item()*inputs.size(0)
            _,predicted=torch.max(outputs,dim=1)
            total+=labels.size(0)
            correct+=torch.eq(predicted,labels).sum().item()

    avg_loss=test_loss/len(test_loader.dataset)
    accuracy=100.0*correct/total#计算准确率，100是为了变成百分率
    print(f"Test loss:{avg_loss},accuracy:{accuracy}")
    return accuracy

def save_model(model,save_path):
    torch.save(model.state_dict(),save_path)

if __name__ =="__main__":
    num_epochs=10
    learning_rate=0.001
    num_class=4
    save_path=r"model_pth\best.pth"
    model=cnn(num_class).to(device)
    loss_function=nn.CrossEntropyLoss()
    optimizer=optim.Adam(model.parameters(),lr=learning_rate)
    train(model,train_loader,loss_function,optimizer,num_epochs)
    final_acc=evaluate(model,test_loader,loss_function)
    print(final_acc)