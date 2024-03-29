# 开发时间 2022/9/13 21:22
# 文件: auth.py
from django.utils.deprecation import MiddlewareMixin  # 导入中间件
from django.shortcuts import redirect


class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):
        # 0.排除那些不需要登录就能访问的页面
        # request.path_info 获取当前用户请求的URL  /login/
        if request.path_info in ['/login/', '/register/', '/image/code/', '/FTmain/', '/FT/']:
            return

        # 1.读取当前用户访问的session信息，如果能读到，说明已经登录过，就可以向后走
        info_dict = request.session.get('info')
        if info_dict:
            return

        # 2.没有登录过，重新回到登录页面
        return redirect('/login/')
