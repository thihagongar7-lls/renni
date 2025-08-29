from django.shortcuts import render
from .models import *

# Create your views here.

def Homepage(request):
    banner = BannerModel.objects.all()
    contex = {
        'banner':banner
    }
    return render(request,'index.html',contex )