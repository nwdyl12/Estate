# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from RealEstate.models import *
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.
def houseList(request,num):
    print num
    house=HouseInfo.objects.all().order_by('-house_id')
    page_obj=Paginator(house,5)
    houPages = page_obj.num_pages
    print houPages
    houCount = page_obj.count
    # if num<=1:
    #     num=1
    # elif num>=houPages:
    #     num=houPages
    houseList = page_obj.page(num)
    print num

    return render(request,'house_list.html',{'houseList':houseList,'currentPage':num,'houPages':houPages,'houCount':houCount})

def houseAdd(request):
    if request.method=='GET':
        userList=UserInfo.objects.all()
        houseType=HouseType.objects.all()
        return render(request,'house_add.html',{'userList':userList,'houseType':houseType})
    else:
        houseType=request.POST.get('houseType')
        userInfo=request.POST.get('userInfo')
        houseAdd=request.POST.get('houseAdd')
        housePrice=request.POST.get('housePrice')
        houseEnv=request.POST.get('houseEnv')
        houseObj=HouseType.objects.get(type_name=houseType)
        userObj=UserInfo.objects.get(user_name=userInfo)
        HouseInfo.objects.create(type=houseObj,user=userObj,house_address=houseAdd,house_price=housePrice,house_ambient=houseEnv)
        houseList=HouseInfo.objects.all()
        return render(request,'house_list.html',{'houseList':houseList})



def houseEdit(request,num):
    if request.method=='GET':
        houseObj=HouseInfo.objects.get(house_id=num)
        userList=UserInfo.objects.all()
        houseType=HouseType.objects.all()

        return render(request,'house_edit.html',{'houseObj':houseObj,'userList':userList,'houseType':houseType})
    else:
        houseType = request.POST.get('houseType')
        userInfo = request.POST.get('userInfo')
        houseAdd = request.POST.get('houseAdd')
        housePrice = request.POST.get('housePrice')
        houseEnv = request.POST.get('houseEnv')
        houseObj=HouseType.objects.get(type_name=houseType)
        userObj=UserInfo.objects.get(user_name=userInfo)
        HouseInfo.objects.filter(house_id=num).update(type=houseObj,user=userObj,house_address=houseAdd,house_price=housePrice,house_ambient=houseEnv)

        return HttpResponse('<script>alert("修改成功！");location.href="/employee/house_list/";</script>')





def houseDelete(request,num):

    HouseInfo.objects.filter(house_id=num).delete()

    return HttpResponse('<script>alert("删除成功！");location.href="/employee/house_list/";</script>')


def houseQuery(request):
    queryType=request.POST.get('queryType')
    houseInput=request.POST.get('houseInput')
    if houseInput:
        if queryType=='1':

                house=HouseType.objects.filter(type_name=houseInput)
                houseList=HouseInfo.objects.filter(type_id=house)

        else:

              houseList=HouseInfo.objects.filter(house_address__contains=houseInput)

        return render(request,'house_list.html',{'houseList':houseList})
    else:
        return HttpResponse('<script>alert("输入值不能为空!");location.href="/employee/house_list/";</script>')