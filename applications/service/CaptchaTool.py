from captcha.image import ImageCaptcha
from PIL import Image
import random


# 定义随机方法
def random_captcha():
    # 定义一个容器
    captcha_text = []
    for i in range(4):
        # 定义验证码字符
        c = random.choice(['0', '1', '2', '4', '6', '8'])
        captcha_text.append(c)
    # 返回一个随机生成的字符串
    return ''.join(captcha_text)


# 生成验证码方法
def gen_captcha():
    # 定义图片对象
    image = ImageCaptcha()
    # 获取字符串
    captcha_text = random_captcha()
    # 生成图像
    captcha_image = Image.open(image.generate(captcha_text))
    return captcha_text, captcha_image
