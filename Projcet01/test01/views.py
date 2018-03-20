from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 必须有一个参数request
from django.template import loader

from test01.models import Department


def test(request):
    # 处理完请求，返回字符串内容给浏览器显示
    return HttpResponse('This is a test code')


def index(request):
    datas = {
        'name': 'django',
        'sex': '男',
        'age': 25,
        'salary': 10000,
        'hobby': ['python', 'c/c++', 'java']
    }

    # 读取模板文件, 得到Template对象
    template = loader.get_template('index.html')
    # 渲染模板, 生成标准的html内容
    html = template.render(datas, request)
    # 响应请求,返回html界面
    return HttpResponse(html)


def show_date(request):
    # 查询出所有部门
    departments = Department.objects.all()
    return render(request, "show_date.html", {"departments": departments})