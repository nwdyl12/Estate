# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from RealEstate.models import *

# Create your views here.
def showFrame(request):
    nname = request.POST.get('userNum')
    pwd = request.POST.get('userPw')
    if nname =='admin' and pwd=='pwd':
        return render(request,'base.html')
    return render(request,'login.html')


def top(request):
    nlist = NoticeInfo.objects.all().order_by('-notice_time')
    return render(request,'top.html',{'nlist':nlist})


def left(request):
    return render(request,'left.html')


def center(request):
    return render(request,'center.html')


def down(request):
    return render(request,'down.html')