import torch.nn as nn

class cnn(nn.Module):
    def __init__(self,num_class):
        super(cnn, self).__init__()
        self.features=nn.Sequential(
            nn.Conv2d(3,16,kernel_size=3,stride=1,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2,stride=2),
            nn.Conv2d(16,32,kernel_size=3,stride=1,padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2,stride=2)
        )

        self.classifier=nn.Sequential(
            nn.Linear(32*56*56,128),
            nn.ReLU(),
            nn.Linear(128,num_class)
        )

    def forward(self,x):
        x=self.features(x)
        x=x.view(x.size(0),-1)
        x=self.classifier(x)

        return x

    