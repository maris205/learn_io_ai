import os
from openai import OpenAI
import base64
import cv2

#目标定位，https://www.volcengine.com/docs/82379/1616136

# 请确保您已将 API Key 存储在环境变量 ARK_API_KEY 中
# 初始化Ark客户端，从环境变量中读取您的API Key
client = OpenAI(
    # 此为默认路径，您可根据业务所在地域进行配置
    base_url="https://ark.cn-beijing.volces.com/api/v3",
    # 从环境变量中获取您的 API Key。此为默认方式，您可根据需要进行修改
    api_key="9ce78cb0-3e2d-4f50-964d-920c7a53fdb9",
)

IMAGE_PATH = "门把手2.jpg"
PROMPT = "帮我框选门把手，以<bbox>x1 y1 x2 y2</bbox>的形式表示"

with open(IMAGE_PATH, "rb") as f:
    base64_image = base64.b64encode(f.read()).decode('utf-8')

response = client.chat.completions.create(
    # 指定您创建的方舟推理接入点 ID，此处已帮您修改为您的推理接入点 ID
    model="doubao-seed-1-6-250615",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpg;base64,{base64_image}"
                    },
                },
                {"type": "text", "text": PROMPT},
            ],
        }
    ],
)

#print(response.choices[0])
bbox_content = response.choices[0].message.content
print(bbox_content) #<bbox>0.26 0.28 0.87 0.59</bbox>或者<bbox>256 270 868 585</bbox>
#坐标格式为 <bbox>x_min y_min x_max y_max</bbox>，其中(x_min, y_min)为方框左上角的坐标，(x_max, y_max )为方框右下角的坐标。
BBOX_TAG_START = "<bbox>"
BBOX_TAG_END = "</bbox>"
coords_str = bbox_content[len(BBOX_TAG_START):-len(BBOX_TAG_END)]
coords = list(map(int, coords_str.split()))
x_min, y_min, x_max, y_max = coords
print(x_min, y_min, x_max, y_max)

# 读取原图
image = cv2.imread(IMAGE_PATH)

# 获取图像尺寸并缩放坐标(模型输出范围为0-1000)
h, w = image.shape[:2]
# x_min_real = int(x_min * w)
# y_min_real = int(y_min * h)
# x_max_real = int(x_max * w)
# y_max_real = int(y_max * h)

x_min_real = int(x_min * w / 1000)
y_min_real = int(y_min * h / 1000)
x_max_real = int(x_max * w / 1000)
y_max_real = int(y_max * h / 1000)

# 绘制红色边界框
cv2.rectangle(image, (x_min_real, y_min_real), (x_max_real, y_max_real), (0, 0, 255), 3)

# 保存结果图片
output_path = os.path.splitext(IMAGE_PATH)[0] + "_with_bboxes.jpg"
cv2.imwrite(output_path, image)
print(f"成功保存标注图片: {output_path}")