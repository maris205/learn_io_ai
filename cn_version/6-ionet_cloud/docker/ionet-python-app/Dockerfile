# 步骤 1: 使用您提供的 NVIDIA CUDA 13.0.1 官方镜像
FROM nvidia/cuda:13.0.1-cudnn-runtime-ubuntu24.04

# 设置环境变量，避免在构建过程中出现交互式提示
ENV DEBIAN_FRONTEND=noninteractive
ENV CUDA_VERSION=13.0.1
ENV PYTHON_VERSION=3.12

# 步骤 2: 安装 pip
# Ubuntu 24.04 自带 Python 3.12，我们只需要安装 pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    rm -rf /var/lib/apt/lists/*

# 步骤 3: 设置工作目录
WORKDIR /app

# 步骤 4: 复制并安装 Python 依赖
COPY requirements.txt .
# 使用 --break-system-packages 以兼容 Ubuntu 24.04 的 pip 保护机制
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# 步骤 5: 复制你的应用代码
COPY app.py .

# 步骤 6: 暴露应用运行的端口
EXPOSE 8000

# 步骤 7: 定义容器启动时要执行的命令
# Ubuntu 24.04 默认的 python3 就是 3.12
CMD ["python3", "app.py"]
