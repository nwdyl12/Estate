# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from RealEstate.models import UserInfo


def top(request):
    return render(request,'top.html')


def left(request):
    return render(request,'left.html')


def center(request):
    return render(request,'center.html')


def down(request):
    return render(request,'down.html')


def showFrame(request):
    return render(request,'base.html')