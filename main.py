
from lib.igbot import InstagramBot
from lib.ai import AIGEenerator
import requests
from PIL import Image
from io import BytesIO
api_key=""
generator =AIGEenerator(api_key)
instagram_bot=InstagramBot("usernameinsta","passwaordinsta")
instagram_bot.sign_in()
def make_post():
    res, images_url=generator.generate_prompt_and_image()
    for i in range(3):
        response=requests.get(images_url[i])
        img= Image.open(BytesIO(response.content))
        img.save(f"images/{i}.jpg")
    caption="  #پست_موقت AI generated, with prompt:"+res
    image_paths=["images/0.jpg","images/1.jpg","images/2.jpg"]
    instagram_bot.post_album(caption,image_paths)
make_post()