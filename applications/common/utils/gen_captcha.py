from captcha.image import ImageCaptcha

from PIL import Image
from random import choices


def gen_captcha(content='0123456789'):
    """ 生成验证码 """
    image = ImageCaptcha()
    # 获取字符串
    captcha_text = "".join(choices(content, k=4))
    # 生成图像
    captcha_image = Image.open(image.generate(captcha_text))
    return captcha_text, captcha_image
