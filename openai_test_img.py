from dotenv import load_dotenv
import os
from openai import OpenAI
from PIL import Image
import requests

# api 키를 가져옴(보안)
load_dotenv()
openai_api_key=os.getenv("OPENAI_API_KEY")
MODEL = "dall-e-3"
client = OpenAI(api_key = openai_api_key)

response = client.images.generate(
  model=MODEL,
  prompt="주인 몰래 사람인척하며 119에 장난 신고를하는 귀여운 앵무새",
  size="1024x1024",
  quality="standard",
  n=1,
)

# 이미지를 받을 수 있는 url
image_url = response.data[0].url

# 사진을 받아와서 저장하고 띄워줌
filename = "image.jpg"
img_respone = requests.get(image_url)
with open(filename, 'wb') as f:
    f.write(img_respone.content)
Image.open(filename)
