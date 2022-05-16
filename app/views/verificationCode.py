from flask import make_response, session
from io import BytesIO
import random
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter


class imageCode():
    def rndColor(self):
        """随机颜色"""
        return random.randint(32, 127), random.randint(32, 127), random.randint(32, 127)

    def geneText(self):
        """生成 4 位验证码"""
        return ''.join(
            random.sample(string.ascii_letters + string.digits, 4))  # ascii_letters 是生成所有字母digits是生成所有数字0 - 9

    def drawLines(self, draw, num, width, height):
        """划线"""
        for num in range(num):
            x1 = random.randint(0, width / 2)
            y1 = random.randint(0, height / 2)
            x2 = random.randint(0, width)
            y2 = random.randint(height / 2, height)
            draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

    def getVerifyCode(self):
        """生成验证码图形"""
        code = self.geneText()
        # 图片大小 120×40
        width, height = 120, 40
        # 新图片对象
        im = Image.new('RGB', (width, height), 'white')
        # 字体
        font = ImageFont.truetype('app/static/arial.ttf', 30)
        # draw 对象
        draw = ImageDraw.Draw(im)
        # 绘制字符串
        for item in range(4):
            draw.text((15 + random.randint(-3, 3) + 23 * item, 2 + random.randint(-3, 3)),
                      text=code[item], fill=self.rndColor(), font=font)
        # 划线
        self.drawLines(draw, 3, width, height)
        return im, code

    def getImgCode(self):
        image, code = self.getVerifyCode()
        # 图片以二进制形式写入
        buf = BytesIO()
        image.save(buf, 'jpeg')
        buf_str = buf.getvalue()
        # 把 buf_str 作为 response 返回前端，并设置首部字段
        response = make_response(buf_str)
        response.headers['Content-Type'] = 'image/gif'
        # 将验证码字符串储存在 session 中
        session['imageCode'] = code
        return response
