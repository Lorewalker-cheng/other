from datetime import date

from django.shortcuts import render, redirect

# Create your views here.
from fist.models import Department, Employee


def index(request):
    departments = Department.objects.all()
    return render(request, "index.html", {'departments': departments})


def show_data(request, dep_id):
    departments = Department.objects.get(id=dep_id)
    employees = Employee.objects.all().filter(department=dep_id)
    # 通过小括号对正则表达式进行分组，视图函数才能获取到参数
    return render(request, 'show_data.html', {'departments': departments, 'employees': employees})


def add_data(request):
    d = Department()
    d.id = None
    d.name = '研发部'
    d.create_date = date(2017,1,1)
    d.save()
    # 重定向url
    return redirect("/fist/index/")


def del_data(request, dep_id):
    d = Department.objects.get(id=dep_id)
    d.delete()
    return redirect("/fist/index/")
