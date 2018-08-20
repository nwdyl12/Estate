# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from django.core import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from RealEstate.models import CustomerInfo, CustomerSource, CustomerType, CustomerCondition, UserInfo


def cusList(request):
    cusinfos = CustomerInfo.objects.all()

    count =0
    for u in cusinfos:
        count += 1

    curr_page= request.GET.get('page', 1)
    curr_page = int(curr_page)
    paginator = Paginator(cusinfos,3)
    try:
        perpage_data = paginator.page(curr_page)  # 获取当前页码的记录
    except PageNotAnInteger:  # 如果用户输入的页码不是整数时,显示第1页的内容
        perpage_datae = paginator.page(1)
    except EmptyPage:  # 如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        perpage_data = paginator.page(paginator.num_pages)

    # 每页开始页码
    begin = (curr_page - int(math.ceil(10.0 / 2)))
    if begin < 1:
        begin = 1
    # 每页结束页码
    end = begin + 9
    if end > paginator.num_pages:
        end = paginator.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9
    pagelist = range(begin, end + 1)


    # # 计算总记录数
    # count = 0
    # size = 3
    # for u in cusinfos:
    #     count += 1
    #
    # if count % size == 0:
    #     total_page = count / size
    # else:
    #     total_page = count / size + 1
    # # 获取当前页面
    # curr_page = request.GET.get('page', 1)
    # curr_page = int(curr_page)
    # if curr_page < 1:
    #     curr_page = 1
    # if curr_page > total_page:
    #     curr_page = total_page
    # # 创建分页器对象
    # pageobj = Paginator(cusinfos, size)
    # # 获取当前页数据
    # try:
    #     perpage_data = pageobj.page(curr_page)
    # except PageNotAnInteger:
    #     # 返回第一页的数据
    #     perpage_data = pageobj.page(1)
    # except EmptyPage:
    #     # 返回最后一页的数据
    #     perpage_data = pageobj.page(pageobj.num_pages)

    return render(request,'customer_list1.html',{'cusinfos':cusinfos,
        'count': count, 'curr_page': curr_page, 'total_page': pagelist[-1],'paginator':paginator,
                                                 'perpage_data':perpage_data})

#客户信息添加
def cusAdd(request):
    if request.method == 'GET':
        cursours = CustomerSource.objects.all()
        curtypes = CustomerType.objects.all()
        cuscons = CustomerCondition.objects.all()
        return render(request, 'customer_add.html', {'cursours': cursours, 'curtypes': curtypes, 'cuscons': cuscons})
    elif request.method == 'POST':
        customerName = request.POST.get('customerName')
        customerSource = request.POST.get('customerSource')
        customerJob =request.POST.get('customerJob')
        customerType =request.POST.get('customerType')
        customerSex =request.POST.get('customerSex')
        customerEmail =request.POST.get('customerEmail')
        customerBirthday =request.POST.get('customerBirthday').rstrip()+'.0'

        import datetime
        customerBirthday = datetime.datetime.strptime(customerBirthday,'%Y-%m-%d %H:%M:%S.%f')

        customerCondition =request.POST.get('customerCondition')
        customerMobile =request.POST.get('customerMobile')
        customerQq =request.POST.get('customerQq')
        customerAddress =request.POST.get('customerAddress')
        customerChangeMan =request.POST.get('customerChangeMan')
        customerAddMan =request.POST.get('customerAddMan')
        customerBlog =request.POST.get('customerBlog')
        customerTel =request.POST.get('customerTel')
        customerMsn =request.POST.get('customerMsn')
        customerCompany =request.POST.get('customerCompany')
        customerRemark =request.POST.get('customerRemark')

        try:
            cus = CustomerInfo.objects.get(customer_name=customerName)
            return HttpResponse('<script>alert("添加失败!");location.href="/customer/customer_add/";</script>')
        except CustomerInfo.DoesNotExist:
            cus = CustomerInfo.objects.create(
                condition_id=customerCondition,
                source_id=customerSource,
                type_id=customerType,
                customer_name=customerName,
                customer_sex=customerSex,
                customer_mobile=customerMobile,
                customer_qq=customerQq,
                customer_address=customerAddress,
                customer_email=customerEmail,
                customer_remark=customerRemark,
                customer_job=customerJob,
                customer_blog=customerBlog,
                customer_tel=customerTel,
                customer_msn=customerMsn,
                birth_day=customerBirthday,
                customer_addman=customerAddMan,
                change_man=customerChangeMan,
                customer_company=customerCompany,
            )
            return HttpResponse('<script>alert("添加成功!");location.href="/customer/customer_add/";</script>')



        # if cus:
        #     return HttpResponse('<script>alert("添加成功!");location.href="/customer/customer_add/";</script>')
        # return HttpResponse('<script>alert("添加失败!");location.href="/customer/customer_add/";</script>')


def cusDet(request,num):
    num  =int(num)
    cusinfo = CustomerInfo.objects.get(customer_id =num)

    return render(request,'customer_detail.html',{'cusinfo':cusinfo})


def cusDel(request,num):
    num  =int(num)
    CustomerInfo.objects.filter(customer_id =num).delete()
    return HttpResponse('<script>alert("删除成功!");location.href="/customer/customer_list1/";</script>')


def cusEdit(request,num):
    num=int(num)
    cusinfo = CustomerInfo.objects.get(customer_id=num)

    userList = UserInfo.objects.all()
    #客户来源
    cusList = CustomerSource.objects.all()
    #客户状态
    cusCon = CustomerCondition.objects.all()
    #客户类型
    cusType = CustomerType.objects.all()
    return render(request,'customer_edit.html',{'cusinfo':cusinfo,'userList':userList,'cls':num,'cusList':cusList,'cusCon':cusCon,'cusType':cusType})




def cusSecAdd(request,num):
    num =int(num)
    reponse = request.POST
    cus = CustomerInfo.objects.filter(customer_id =num).update(
        user_id=reponse['customerForUser'],
        source_id=reponse['customerSource'],
        # customer_name=reponse['customerName'],
        condition_id=reponse['customerCondition'],
        customer_sex=reponse['customerSex'],
        type_id=reponse['customerType'],
        # birth_day=reponse['customerBirthday'],
        customer_mobile=reponse['customerMobile'],
        customer_qq=reponse['customerQq'],
        customer_address=reponse['customerAddress'],
        customer_email=reponse['customerEmail'],
        customer_job=reponse['customerJob'],
        customer_blog=reponse['customerBlog'],
        customer_tel=reponse['customerTel'],
        customer_msn=reponse['customerMsn'],
        customer_company=reponse['customerCompany'],
        # customer_addman=reponse['customerAddMan'],
        change_man=reponse['customerChangeMan'],
        customer_remark=reponse['customerRemark'],
    )
    if cus:
        return HttpResponse('<script>alert("修改成功!");location.href="/customer/customer_list1/";</script>')

#查询信息查询
def cusSea(request):
    queryType = request.POST.get('queryType')
    queryType = int(queryType)

    customerInput = request.POST.get('customerInput')
    #按客户姓名查询
    if queryType ==1:
        cname = customerInput
        if cname:
            c  = CustomerInfo.objects.filter(customer_name__contains= cname)
            if c.count()>=0 :
                return render(request,'customer_list1.html',{'perpage_data':c})
            else:
                return HttpResponse('<script>alert("不存在，请输入正确的名字!");location.href="/customer/customer_list1";</script>')
        else:
             return HttpResponse('<script>location.href="/customer/customer_list1";</script>')

    # 按客户状态查询
    if queryType == 2:
        ccon = customerInput
        if ccon:
            c =CustomerCondition.objects.filter(condition_name =ccon)
            if c:
                cusinfos = CustomerInfo.objects.filter(condition_id= c[0])
                if cusinfos:
                   return render(request,'customer_list1.html',{'perpage_data':cusinfos})
            return HttpResponse('<script>alert("不存在，请输入正确的名字!");location.href="/customer/customer_list1";</script>')
        return HttpResponse('<script>location.href="/customer/customer_list1";</script>')

    # 按客户来源查询
    if queryType == 3:
        csou = customerInput
        if csou:
            c = CustomerSource.objects.filter(source_name = csou )
            if c :
                cusinfos = CustomerInfo.objects.filter(source_id =c[0])
                if cusinfos:
                    return render(request,'customer_list1.html',{'perpage_data':cusinfos})
                return HttpResponse('<script>alert("不存在，请输入正确的名字!");location.href="/customer/customer_list1";</script>')
        return HttpResponse('<script>location.href="/customer/customer_list1";</script>')

    # 按客户类型查询
    if queryType == 4:
        ctype = customerInput
        if ctype:
            c = CustomerType.objects.filter(type_name= ctype)
            if c :
                cusinfos= CustomerInfo.objects.filter(type_id = c)
                if cusinfos:
                    return render(request, 'customer_list1.html', {'perpage_data': cusinfos})
            return HttpResponse('<script>alert("不存在，请输入正确的名字!");location.href="/customer/customer_list1";</script>')
        return HttpResponse('<script>location.href="/customer/customer_list1";</script>')
    # 按客户员工查询
    if queryType == 5:
        cuname = customerInput
        if cuname:
            c =UserInfo.objects.filter(user_name = cuname)
            if c :
                cusinfos = CustomerInfo.objects.filter(user_id= c)
                if cusinfos:
                    return render(request, 'customer_list1.html', {'perpage_data': cusinfos})
            return HttpResponse('<script>alert("不存在，请输入正确的名字!");location.href="/customer/customer_list1";</script>')
        return HttpResponse('<script>location.href="/customer/customer_list1";</script>')

    # 按客户公司查询
    if queryType == 6:
        ccompany = customerInput
        if ccompany:
            cusinfos = CustomerInfo.objects.filter(customer_company  =ccompany)
            if cusinfos:
                return render(request, 'customer_list1.html', {'perpage_data': cusinfos})
        return HttpResponse('<script>location.href="/customer/customer_list1";</script>')


def customQury(request):
    cusTyname=request.GET.get('typename')
    cusT=CustomerType.objects.filter(type_name=cusTyname)
    print cusT
    ccusT = serializers.serialize('json',cusT)
    c = cusT.count()
    return JsonResponse({'cusT':ccusT,'c':c})


def customDel(request):
    type_id = request.GET.get('typeID')
    print type_id
    cus = CustomerType.objects.filter(type_id=type_id).delete()
    print cus
    return render(request, 'customer_type_list.html', {'cus': cus})


def customAdd(request):
    return render(request, 'customer_type_add.html')


def cusTypeList(request):
    customList=CustomerType.objects.all()
    return render(request,'customer_type_list.html',{'customList':customList})


def cusTypeAdd(request):
    cusTyname=request.GET.get('typeName')
    CustomerType.objects.create(type_name=cusTyname,is_used=1)
    flag=True
    return JsonResponse({'flag':flag})
