from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from picture.models import Area


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

