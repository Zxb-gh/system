
"""
生成验证码
1.准备素材
字体（ttf），文字内容，颜色，干扰线
2.画验证码
Pillow库 、random
创建图片
记录文字内容，Django session 【服务器，python代码】
字符串（2334） cookie【浏览器】

（1）cookie + session 对应关系
（2）携带cookie，找到对应的session【提交表单】
    请求带上验证码参数 与 session中的验证码进行比较
3.io文件流
BytesIO
"""
import io
import os
import random
import matplotlib.pyplot as plt

from PIL import Image, ImageDraw, ImageFont
from django.conf import settings
from django.http import HttpResponse
from matplotlib.ticker import MultipleLocator


class VerifyCode(object):
    def __init__(self, dj_request):
        self.dj_request = dj_request
        self.code_len = 4
        # 验证码图片尺寸
        self.img_width = 150
        self.img_height = 30

        # Django中session的名称
        self.session_key = 'verify_code'

    """验证码类"""
    def gen_code(self):
        """生成验证码"""
        # 1.使用随机数生成字符串
        code = self._get_vcode()
        # print(code)
        # 2.把验证码存在session
        self.dj_request.session[self.session_key] = code
        # 3.准备随机元素（背景颜色， 验证码文字的颜色， 干扰线、）
        font_color = (random.randrange(170, 255), random.randrange(160, 255), random.randrange(150, 255))
        # RGB随机背景色
        bg_color = (random.randrange(20, 255), random.randrange(20, 255), random.randrange(30, 255))
        # 字体路径
        font_path = os.path.join(settings.BASE_DIR, 'static', 'fonts', 'timesbi.ttf')

        # 创建图片
        im = Image.new('RGB', (self.img_width, self.img_height), bg_color)
        draw = ImageDraw.Draw(im)

        # 画干扰线
        # 随机条数，到底画几条
        for i in range(random.randrange(1, int(self.code_len/2)+1)):
            # 线条的颜色
            line_color = random.choice(bg_color)
            # 线条的位置
            point = (random.randrange(0, self.img_width * 0.2),
                     random.randrange(0, self.img_height),
                     random.randrange(self.img_width - self.img_width * 0.2, self.img_width),
                     random.randrange(0, self.img_height))
            # 线条的宽度
            width = random.randrange(1, 3)
            draw.line(point, fill=line_color, width=width)

        # 画验证码
        # enumerate枚举函数
        for index, char in enumerate(code):
            code_color = random.choice(font_color)
            # 指定字体
            font_size = random.randrange(15, 25)
            font = ImageFont.truetype(font_path, font_size)
            point = index * self.img_width / self.code_len
            # 位置、内容、大小、颜色
            draw.text((point, random.randrange(0, self.img_height/3)), char, font=font, code=code_color)

        buf = io.BytesIO()
        im.save(buf, 'gif')
        return HttpResponse(buf.getvalue(), 'image/gif')

    def _get_vcode(self):
        random_str = 'ABCDEFGHIJKLMNPQRSTUVWXYZabcdefghigkmnpqrstuvwxyz23456789'
        code_list = random.sample(list(random_str), self.code_len)
        code = ''.join(code_list)
        return code

    def validate_code(self, code):
        """验证验证码是否正确"""
        # 1.转变大小写
        code = str(code).lower()
        vcode = self.dj_request.session.get(self.session_key, '')
        # if vcode.lower() == code:
        #     return True
        # else:
        return vcode.lower() == code


# if __name__ == '__main__':
#     client = VerifyCode(None)
#     client.gen_code()


class MatplotlibPng(object):
    def __init__(self, dp_request):
        self.dp_request = dp_request
        self.code_len = 4
        # 验证码图片尺寸
        self.img_width = 150
        self.img_height = 30

    # 画图类
    def draw_plt(self):

        plt.plot(self.dp_request, linewidth=3)

        # plt.title('1', fontsize=24)
        # plt.xlabel('2', fontsize=3)
        x_major_locator = MultipleLocator(1)
        ax = plt.gca()
        ax.xaxis.set_major_locator(x_major_locator)
        # plt.ylabel('3', fontsize=24)
        # plt.tick_params(axis='both', labelsize=14)
        # my_file = os.path.abspath()


        plt.savefig('static/images/gif')
        plt.clf()
        # return HttpResponse('gif')


# if __name__ == '__main__':
#     dp_request = [1, 2, 3, 4, 5]
#     client = MatplotlibPng(dp_request)
#     client.draw_plt()
