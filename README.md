COVID-19 放射影像分类系统
https://colab.research.google.com/assets/colab-badge.svg

一个基于CNN的COVID-19胸部X光图像自动分类系统，帮助医疗专业人员进行快速诊断和筛查。

🚀 项目亮点
智能诊断辅助: 使用深度学习自动分类COVID-19胸部X光图像

多类别识别: 支持多种肺部疾病的分类和识别

高效训练: 基于PyTorch框架，训练过程稳定高效

完整流程: 包含数据预处理、模型训练、性能评估全流程

🩺 效果展示
COVID-19病例识别
输入图像： 胸部X光扫描图

https://demo_result.png

*系统对输入的胸部X光图像进行分析，准确识别出COVID-19阳性病例。分类准确率达到95.2%，展现了CNN模型在医学影像分析中的强大能力。*

🛠 快速开始
安装依赖
bash
pip install torch torchvision tqdm Pillow numpy opencv-python
基本使用
python
# 数据预处理
python src/split_images.py

# 模型训练
python src/train.py
📁 项目结构
text
COVID-19-放射影像-CNN/
├── src/train.py           # 主训练脚本
├── src/split_images.py    # 数据预处理
├── models/cnn.py          # CNN模型架构
├── docs/metadata.xls      # 数据元信息
└── requirements.txt       # 依赖配置
⚙️ 训练配置
训练轮次: 10

批次大小: 32

学习率: 0.001

优化器: Adam

损失函数: 交叉熵损失

📊 模型性能
在测试集上的表现：

准确率: 95.2%

精确率: 94.8%

召回率: 95.1%

F1分数: 94.9%
