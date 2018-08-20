# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from RealEstate.models import *
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.
# ================================员工信息=================================

# 员工分页
def ygfy(request,ulist):
    # 计算总记录数
    count = 0
    # 每页存放记录数
    size = 3
    for i in ulist:
        count += 1
    if count % size == 0:
        total_page = count / size
    else:
        total_page = count / size + 1
    # 获取当前页码数
    curr_page = request.GET.get('page', 1)
    curr_page = int(curr_page)
    if curr_page < 1:
        curr_page = 1
    if curr_page > total_page:
        curr_page = total_page
    # 创建分页器对象
    pageobj = Paginator(ulist, size)
    # 获取当前页数据
    try:
        perpage_data = pageobj.page(curr_page)
    except PageNotAnInteger:
        # 返回第一页的数据
        perpage_data = pageobj.page(1)
    except EmptyPage:
        # 返回最后一页的数据
        perpage_data = pageobj.page(pageobj.num_pages)

    return {'ulist': perpage_data, 'count': count, 'curr_page': curr_page, 'total_page': total_page}

# 员工信息显示页面
def empList(request):
    # 获取所有的员工数据
    ulist = UserInfo.objects.all()
    u = ygfy(request,ulist)
    return render(request, 'emp_list.html',u)

# 员工查询操作
def empSea(request):
    # 获取查询类型
    queryType = request.POST.get('queryType')
    queryType = int(queryType)

    # 获取查询内容
    querycontent = request.POST.get('userName')
    if queryType and querycontent:
        if queryType == 1:
            user_name = querycontent
            # 如果user_name不为空
            if user_name:
                ulist = UserInfo.objects.filter(user_name__contains=user_name)
                # 如果数据库存在
                if ulist:
                    u = ygfy(request, ulist)
                    return render(request, 'emp_list.html', u)
                else:
                    return HttpResponse('<script>alert("不存在，请输入正确的员工姓名!");location.href="/employee/emp_list";</script>')
            else:
                return HttpResponse('<script>alert("内容不能为空!");location.href="/employee/emp_list";</script>')

        elif queryType == 2:
            department_name = querycontent
            # 如果department_name不为空
            if department_name:
                dlist = DepartmentInfo.objects.filter(department_name=department_name)
                # 如果数据库存在
                if dlist:
                    ulist = UserInfo.objects.filter(department_id=dlist[0].department_id)
                    u = ygfy(request, ulist)
                    return render(request, 'emp_list.html',u)
                else:
                    return HttpResponse('<script>alert("不存在，请输入正确的部门名称!");location.href="/employee/emp_list";</script>')
            else:
                return HttpResponse('<script>alert("内容不能为空!");location.href="/employee/emp_list";</script>')

        elif queryType == 3:
            role_name = querycontent
            # 如果role_name不为空
            if role_name:
                rlist = UserRole.objects.filter(role_name=role_name)
                # 如果数据库存在
                if rlist:
                    ulist = UserInfo.objects.filter(role_id=rlist[0].role_id)
                    u = ygfy(request, ulist)
                    return render(request, 'emp_list.html', u)
                else:
                    return HttpResponse('<script>alert("不存在，请输入正确的角色名称!");location.href="/employee/emp_list";</script>')
            else:
                return HttpResponse('<script>alert("内容不能为空!");location.href="/employee/emp_list";</script>')

        else:
            user_diploma = querycontent
            # 如果user_diploma不为空
            if user_diploma:
                ulist = UserInfo.objects.filter(user_diploma=user_diploma)
                # 如果数据库存在
                if ulist:
                    u = ygfy(request, ulist)
                    return render(request, 'emp_list.html', u)
                else:
                    return HttpResponse('<script>alert("不存在，请输入正确的员工学历!");location.href="/employee/emp_list";</script>')
            else:
                return HttpResponse('<script>alert("内容不能为空!");location.href="/employee/emp_list";</script>')

    else:
        return HttpResponse('<script>alert("内容不能为空!");location.href="/employee/emp_list";</script>')

# 员工编辑操作
def empEdit(request, user_id):
    uedit = UserInfo.objects.get(user_id=user_id)
    dep = DepartmentInfo.objects.all()
    return render(request, 'emp_edit.html', {'u': uedit, 'dep': dep})

# 员工详情操作
def empDetail(request, num):
    num = int(num)
    uinfo = UserInfo.objects.get(user_id=num)
    return render(request, 'emp_detail.html', {'uinfo': uinfo})

# 删除员工操作
def empDel(request, num):
    num = int(num)
    UserInfo.objects.filter(user_id=num).delete()
    return HttpResponse('<script>alert("删除成功!");location.href="/employee/emp_list";</script>')

# 提交方法
def employeeSubmit(request, num):
    num = int(num)
    response = request.POST
    uedit = UserInfo.objects.filter(user_id=num).update(
        user_age=response['userAge'],
        user_sex=response['userSex'],
        user_nation=response['userNation'],
        user_diploma=response['userDiploma'],
        is_married=response['isMarried'],
        department_id=response['departmentId'],
        user_tel=response['userTel'],
        user_intest=response['userIntest'],
        user_mobile=response['userMobile'],
        user_idnum=response['userIdnum'],
        user_email=response['userEmail'],
        user_address=response['userAddress'])

    if uedit:
        return HttpResponse('<script>alert("修改成功!");location.href="/employee/emp_list";</script>')


#=================================公 告===================================

# 公告分页
def ggfy(request,nlist):
    # 计算总记录数
    count = 0
    # 每页存放记录数
    size = 2
    for i in nlist:
        count += 1
    if count % size == 0:
        total_page = count / size
    else:
        total_page = count / size + 1
    # 获取当前页码数
    curr_page = request.GET.get('page', 1)
    curr_page = int(curr_page)
    # 判断是否越界
    if curr_page < 1:
        curr_page = 1
    if curr_page > total_page:
        curr_page = total_page
    # 创建分页器对象
    pageobj = Paginator(nlist, size)
    # 获取当前页的数据
    try:
        perpage_data = pageobj.page(curr_page)
    except PageNotAnInteger:
        # 返回第一页的数据
        perpage_data = pageobj.page(1)
    except EmptyPage:
        # 返回最后一页的数据
        perpage_data = pageobj.page(pageobj.num_pages)
    return {'nlist': perpage_data, 'count': count, 'curr_page': curr_page, 'total_page': total_page}

# 显示公告信息
def noticeList(request):
    nlist = NoticeInfo.objects.all()
    n = ggfy(request, nlist)
    return render(request,'notice_list.html',n)

# 添加公告信息
def noticeAdd(request):
    if request.method == 'GET':
        ulist=UserInfo.objects.all()
        return render(request,'notice_add.html',{'ulist':ulist})
    # 接受请求参数
    else:
        user = request.POST.get('user')
        notice_item = request.POST.get('notice_item')
        notice_content = request.POST.get('notice_content')
        notice_time = request.POST.get('notice_time')
        notice_endtime = request.POST.get('notice_endtime')
        puser = UserInfo.objects.filter(user_name=user)
        # 将数据注册到数据库
        notice = NoticeInfo.objects.create(user_id=user,notice_item=notice_item,notice_content=notice_content,notice_time=notice_time,notice_endtime=notice_endtime )
        if notice:
            return HttpResponse('<script>alert("添加成功");location.href ="/employee/notice_list/";</script>')
        else:
            return HttpResponse('<script>alert("添加失败");location.href ="/employee/notice_add/";</script>')

# 删除公告信息
def noticeDel(request,num):
    num = int(num)
    NoticeInfo.objects.filter(notice_id=num).delete()
    return HttpResponse('<script>alert("删除成功!");location.href="/employee/notice_list";</script>')

# 查询公告信息
def noticeSearch(request):
    # 获取查询类型
    queryType = request.POST.get('queryType')
    queryType = int(queryType)

    # 获取查询内容
    querycontent = request.POST.get('noticeInput')
    if querycontent and queryType:
        if queryType == 1:
            notice_item = querycontent
            if notice_item:
                nlist = NoticeInfo.objects.filter(notice_item__contains=notice_item)
                if nlist:
                    n = ggfy(request, nlist)
                    return render(request,'notice_list.html',n)
                else:
                    return HttpResponse('<script>alert("此公告不存在!");location.href="/employee/notice_list";</script>')
            else:
                return HttpResponse('<script>alert("内容不能为空!");location.href="/employee/notice_list";</script>')
        else:
            notice_content = querycontent
            if notice_content:
                nlist = NoticeInfo.objects.filter(notice_item__contains=notice_content)
                if nlist:
                    n = ggfy(request, nlist)
                    return render(request,'notice_list.html',n)
                else:
                    return HttpResponse('<script>alert("此公告不存在!");location.href="/employee/notice_list";</script>')
            else:
                return HttpResponse('<script>alert("内容不能为空!");location.href="/employee/notice_list";</script>')
    else:
        return HttpResponse('<script>alert("输入不能为空!");location.href="/employee/notice_list/";</script>')
