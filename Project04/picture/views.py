import os

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from Project04.settings import BASE_DIR
from picture.models import Area, Picture


def index(request):
    return render(request, 'index.html')


# 这个是通用的，通过传入上一层的id，来找出他的下层子集
# id为1的是最顶层的，没有父集
def provinces(request, id=1):
    p = Area.objects.filter(parent=id)

    prov_list = []

    for i in p:
        prov_list.append((i.id, i.title))

    data = {'provinces': prov_list}
    return JsonResponse(data)


def upload(request):
    # 获取post参数（图片）
    pic = request.FILES.get('pic')

    # 拼接图片存放路径， 必须是static/media下，有其他文件夹，就继续接
    path = '%s/media/pic/%s' % (os.path.join(BASE_DIR, 'static'), pic.name)

    with open(path, 'wb') as f:
        for data in pic.chunks():
            # 图片的内容有可能很大，需要循环读出来
            f.write(data)

    # 保存路径到数据库
    p = Picture()
    p.name = pic.name
    p.path = 'pic/%s' % pic.name
    p.save()

    return render(request, 'index.html')


def show_pic(request, page_no=1):
    # 查询所有的图片对象，返回所有的图片
    pics = Picture.objects.all()
    # 创建page_obj对象
    # 参数1: 要分页的数据
    # 参数2: 每页多少条
    page_obj = Paginator(pics, 3)

    page_num = page_obj.page_range

    # 获取第一页数据 Page类型, page_no为要搜索的那个分页的页码
    page = page_obj.page(page_no)
    # 当前是第几页
    page_n = page.number

    pic = {}
    for i in page:
        pic[i.name] = i.path
    context = {'pics': pic, 'page_num': page_num, 'page_n': page_n} # ,
    return JsonResponse(context)
