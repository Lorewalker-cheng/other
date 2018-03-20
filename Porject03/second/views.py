from django.shortcuts import render
from second.models import Info, Focus


# Create your views here.
def index(request):
    info = Info.objects.all()

    return render(request, 'index.html', {"info": info})


def center(request):

    return render(request, 'center.html', {})