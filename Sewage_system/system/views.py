from utils.verify import VerifyCode, MatplotlibPng


def verify_code(request):
    """验证码显示"""
    client = VerifyCode(request)
    return client.gen_code()


def matplotlib_png(request):
    dp_request = [1, 2, 3, 4, 5]
    client = MatplotlibPng(dp_request)
    client.draw_plt()