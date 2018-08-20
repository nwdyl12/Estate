# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from RealEstate.models import UserInfo


def login(request):
    if request.method=='GET':
        return render(request, 'login.html')
    else:
            nname = request.POST.get('userNum')
            pwd = request.POST.get('userPw')
            c = UserInfo.objects.filter(user_num =nname,user_pw =pwd).count()
            if c ==1:
                return HttpResponseRedirect('/view/frame/')
                # return render(request,'base.html')
            else:
                return render(request,'login.html')

