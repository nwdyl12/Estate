# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from RealEstate.models import *
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage


# Create your views here.
def cusCareList(request):
    if request.method=='GET':
        num = request.GET.get('num', 1)
        num = int(num)
        cus=CustomerCare.objects.all().order_by('-care_id')
        page_obj = Paginator(cus, 5)
        cusPages=page_obj.num_pages
        cusCount=page_obj.count
        if num<=1:
            num=1
        elif num>=cusPages:
            num=cusPages
        cusList = page_obj.page(num)

        return render(request,'customer_care_list.html',{'cusList':cusList,'currentPage':num,'cusPages':cusPages,'cusCount':cusCount})



def cusCareAdd(request):
    if request.method=='GET':

        cusList=CustomerInfo.objects.all()
        cusCareList=CustomerCare.objects.values('care_way').all().distinct()
        # print cusCareList
        cList = []
        for c in cusCareList:
            c = c['care_way'].encode('utf-8').decode('utf-8')
            cList.append(c)
        # print cList
        return render(request, 'customer_care_add.html', {'cusList': cusList, 'cusCareList': cList})
    else:
        careTheme=request.POST.get('careTheme')
        customerId=request.POST.get('customerId')
        careTime=request.POST.get('careTime')
        careNexttime=request.POST.get('careNexttime')
        careWay=request.POST.get('careWay')
        carePeople=request.POST.get('carePeople')
        careRemark=request.POST.get('careRemark')
        cusInfo=CustomerInfo.objects.get(customer_name=customerId)
        CustomerCare.objects.create(care_theme=careTheme,customer=cusInfo,care_time=careTime,care_way=careWay,care_people=carePeople,care_remark=careRemark)
        cusList=CustomerCare.objects.all()

        return HttpResponse('<script>alert("添加成功!");location.href="/customer/customer_care_list/";</script>')

def cusCareEdit(request):
    if request.method=='GET':
        cid=request.GET.get('cid')
        cid=int(cid)
        cus=CustomerCare.objects.get(care_id=cid)
        cusInfo=CustomerInfo.objects.all()
        cusWay=CustomerCare.objects.values('care_way').all().distinct()
        cList=[]
        for c in cusWay:
            c=c['care_way'].encode('utf-8').decode('utf-8')
            cList.append(c)
        return render(request,'customer_care_edit.html',{'cus':cus,'cusAll':cList,'cusInfo':cusInfo})
    else:
        cid=request.POST.get('cid')
        cid=int(cid)
        careTheme=request.POST.get('careTheme')
        customerId=request.POST.get('customerId')
        careTime=request.POST.get('careTime')
        careNexttime=request.POST.get('careNexttime').rstrip()+'.0'
        import datetime
        careNexttime=datetime.datetime.strptime(careNexttime,'%Y-%m-%d %H:%M:%S.%f')
        carePeople=request.POST.get('carePeople')
        careWay=request.POST.get('careWay')
        careRemark=request.POST.get('careRemark')
        cusInfo=CustomerInfo.objects.get(customer_id=customerId)

        flag=CustomerCare.objects.filter(care_id=cid).update(care_theme=careTheme,customer_id=cusInfo,care_people=carePeople,care_time=careTime,care_nexttime=careNexttime,care_way=careWay,care_remark=careRemark)
        return HttpResponse('<script>alert("修改成功!");location.href="/customer/customer_care_list/";</script>')

def cusCareDelete(request):
    if request.method=='GET':
        id=request.GET.get('did')
        CustomerCare.objects.filter(care_id=id).delete()

    return HttpResponse('<script>alert("删除成功!");location.href="/customer/customer_care_list/";</script>')

def cusCareQuery(request):
    customerInput=request.POST.get('customerInput')
    # print customerInput
    queryType=request.POST.get('queryType')
    # print queryType
    if customerInput:
        if queryType=='1':
            cus1=CustomerInfo.objects.filter(customer_name__contains=customerInput)
            # cus=cusId[0]['customer_id']
            # print cusId
            # cusList=
            for cus in cus1:
                cusList=CustomerCare.objects.filter(customer=cus)
               # cusList=CustomerCare.objects.filter(customer_id=cus['customer_id'])
            # print cusList
        elif queryType=='2':
            cusList=CustomerCare.objects.filter(care_theme__contains=customerInput)

        else:
            cusList=CustomerCare.objects.filter(care_way__contains=customerInput)
        # CustomerInfo.objects.
        return render(request,'customer_care_list.html',{'cusList':cusList})
    else:
        return HttpResponse('<script>alert("输入值不能为空!");location.href="/customer/customer_care_list/";</script>')

