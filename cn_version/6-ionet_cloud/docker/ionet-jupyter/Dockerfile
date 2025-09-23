# 步骤 1: 使用 NVIDIA CUDA 13.0.1 官方镜像
FROM nvidia/cuda:13.0.1-cudnn-runtime-ubuntu24.04

# 设置环境变量
ENV DEBIAN_FRONTEND=noninteractive

# 步骤 2: 安装 Python pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    rm -rf /var/lib/apt/lists/*

# 步骤 3: 复制并安装 Python 依赖 (包括 JupyterLab)
WORKDIR /workspace
COPY requirements.txt .
RUN pip install --no-cache-dir --break-system-packages -r requirements.txt

# 步骤 4: 暴露 JupyterLab 默认端口
EXPOSE 8888

# 步骤 5: 设置容器启动命令来运行 JupyterLab
#
# --ip=0.0.0.0      -> 允许从任何IP地址访问 (外网访问的关键)
# --port=8888       -> 指定服务端口
# --no-browser      -> 不要在服务器上尝试打开浏览器
# --allow-root      -> 允许 root 用户运行 (Docker 容器内通常是 root)
# --NotebookApp.token -> 设置一个固定的访问密码/令牌
#
# !!! 安全警告: 请务必将下面的 'your-secret-token-change-me' 替换成一个您自己的、足够复杂的密码 !!!
#
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=88888888"]
