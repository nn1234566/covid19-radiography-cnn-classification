import os
import shutil
import random

# 设置随机种子，这样每次划分结果都一样
random.seed(42)

def split_images(source_folder, train_folder, test_folder, split_ratio=0.8):
    """
    自动将图片分成训练集和测试集
    
    参数:
    source_folder: 原始图片所在的文件夹（比如 COVID-19_Radiography_Dataset/COVID）
    train_folder: 训练集目标文件夹
    test_folder: 测试集目标文件夹
    split_ratio: 训练集比例，0.8表示80%
    """
    
    # 确保目标文件夹存在
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    
    # 获取所有图片文件
    image_files = [f for f in os.listdir(source_folder) 
                  if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]
    
    # 随机打乱文件顺序
    random.shuffle(image_files)
    
    # 计算分割点
    split_index = int(len(image_files) * split_ratio)
    
    # 划分文件
    train_files = image_files[:split_index]
    test_files = image_files[split_index:]
    
    # 复制文件到训练集
    for file_name in train_files:
        src_path = os.path.join(source_folder, file_name)
        dst_path = os.path.join(train_folder, file_name)
        shutil.copy2(src_path, dst_path)
    
    # 复制文件到测试集
    for file_name in test_files:
        src_path = os.path.join(source_folder, file_name)
        dst_path = os.path.join(test_folder, file_name)
        shutil.copy2(src_path, dst_path)
    
    print(f"从 {source_folder} 处理了 {len(image_files)} 张图片:")
    print(f"  训练集: {len(train_files)} 张")
    print(f"  测试集: {len(test_files)} 张")

# 主程序
if __name__ == "__main__":
    # 原始数据路径 - 根据您的实际情况修改
    base_source = "COVID-19_Radiography_Dataset"
    base_target = "dataset"
    
    # 四个疾病类别
    categories = ["COVID", "Lung_Opacity", "Normal", "Viral Pneumonia"]
    
    print("开始自动划分图片...")
    
    for category in categories:
        source_folder = os.path.join(base_source, category)
        train_folder = os.path.join(base_target, "train", category)
        test_folder = os.path.join(base_target, "test", category)
        
        # 检查源文件夹是否存在
        if os.path.exists(source_folder):
            split_images(source_folder, train_folder, test_folder)
        else:
            print(f"警告: 找不到文件夹 {source_folder}")
    
    print("\n所有图片划分完成！")
    print("现在您可以在训练代码中使用 dataset/train 和 dataset/test 路径了")