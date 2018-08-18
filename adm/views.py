# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from RealEstate.models import *


def empAdd(request):
    departs = DepartmentInfo.objects.all()
    userole = UserRole.objects.all()
    return render(request,'emp_add.html',{'departs':departs,'useroles':userole})


def empAddInfo(request):
    userName = request.POST.get('userName')
    userNum = request.POST.get('userNum')
    userAge = request.POST.get('userAge')
    userPw = request.POST.get('userPw')
    userSex =request.POST.get('userSex')
    userNation = request.POST.get('userNation')
    userDiploma = request.POST.get('userDiploma')
    isMarried = request.POST.get('isMarried')
    departmentId = request.POST.get('departmentId')
    roleId = request.POST.get('roleId')
    userTel = request.POST.get('userTel')
    userIntest = request.POST.get('userIntest')
    userBankcard = request.POST.get('userBankcard')
    userMobile = request.POST.get('userMobile')
    isIdCard = request.POST.get('isIdCard')
    userIdnum =request.POST.get('userIdnum')
    userAddress =request.POST.get('userAddress')
    userAddman =request.POST.get('userAddman')
    userEmail = request.POST.get('userEmail')


    try:
         user = UserInfo.objects.get(user_idnum = userIdnum)
         return HttpResponse('<script>alert("用户已存在,添加失败!");location.href="/adm/emp_add/";</script>')
    except UserInfo.DoesNotExist:
        user =  UserInfo.objects.create(department_id =departmentId,role_id =roleId,user_name =userName,user_sex =userSex,user_mobile =userMobile
       ,user_age =userAge,user_address = userAddress,user_num =userNum,user_pw = userPw, user_tel =userTel, user_idnum =userIdnum ,
       user_email =userEmail, user_addman  =userAddman ,user_changeman =userAddman,user_intest =userIntest , user_diploma = userDiploma, user_bankcard =userBankcard,
        user_nation =userNation,is_married =isMarried)
        return HttpResponse('<script>alert("添加成功!");location.href="/adm/emp_add/";</script>')
