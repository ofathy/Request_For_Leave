from django.db.models import *
from django.db.models import  Expression
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect,request
from django.shortcuts import render
from .form import  Aprove_Reject_form,Leave_request_form
from django.urls import reverse
from app1.models import Leave_Requests
from datetime import datetime, timedelta
from datetime import date
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
import json
import uuid
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from itertools import chain
from django import template
from django.contrib.auth.models import Group
from django.utils.timezone import now
from datetime import timedelta as tdelta
from django.utils import timezone
from django.core import serializers
import time
from decimal import Decimal
from django.db.models.functions import ExtractMonth




###########################################################################################




#############################################################################################

def index(request):
    return HttpResponse("<center><h1>here you are Osama</h1></center>")




# =======================================
# =======================================
# =======================================
# =======================================
# ==========================================
# ****************************************=======================================
# =======================================
# =======================================
# =======================================
# ==========================================
# ****************************************=======================================
# =======================================
# =======================================
# =======================================
# ==========================================
# ****************************************=======================================
# =======================================
# =======================================
@login_required
def addition_Forbidden(request):
    return render(request, "addition_Forbidden.html", {})
# =======================================

@login_required
def success(request):
    return render(request,"success.html", {}) 
# ==========================================
@login_required
def main(request):
    if request.user.groups.filter(name='employees') :
       return HttpResponseRedirect(reverse('main1'))
    elif request.user.groups.filter(name='managers'):
       return HttpResponseRedirect(reverse('main2'))
# ****************************************

register = template.Library()
#loggedadmin = request.user
@register.filter(name='has_group')

def has_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return True if group in user.groups.all() else False
    #----------------------------------------------------------
@login_required
def Request_to_Leave_V(request):

    form = Leave_request_form((request.POST or None))
    title2 = ""
    if form.is_valid():
        request.session['form-submitted'] = True
        instance = form.save(commit=False)
        instance.employee_name = request.user.get_full_name()
        if has_group(request.user,"Finance"):
           instance.department_name="Finance"
        elif  has_group(request.user,"IT"): 
              instance.department_name="IT"
        elif  has_group(request.user,"Investment"): 
              instance.department_name="Investment"                    
        instance.time_to_leave=datetime.now()
        instance.save()
        return HttpResponseRedirect(reverse('success'))


    context = { "form": form,}
    return render(request, "Admision.html", context)

#--------------------------------------------------
@login_required
def main1(request):
    return render(request, "index.html", {})
#----------------------------------------------------
@login_required
def main2(request):
    return render(request, "index2.html", {})    
#-----------------------------------------------------------
@login_required
def H_req_for_managers(request,id=None):
    today = str(date.today())
    if has_group(request.user,"IT"):
       requests = Leave_Requests.objects.all().filter(department_name='IT').order_by('time_to_leave')
    elif has_group(request.user,"Investment"):
       requests = cartridges.objects.all().filter(department_name='Investment').order_by('time_to_leave')
    elif has_group(request.user,"Finance"):
       requests = cartridges.objects.all().filter(department_name='Finance').order_by('time_to_leave')
  
    return render(request, "H_req_for_managers.html", { "requests":requests,})

#----------------------------------------------------------------------
@login_required
def H_req_for_employees(request,id=None):
    today = str(date.today())
    requests = Leave_Requests.objects.all().filter(employee_name=request.user.get_full_name()).order_by('time_to_leave')
    return render(request, "H_req_for_employees.html", { "requests":requests,})    
#----------------------------------------------------------------------
@login_required
def Today_req_for_managers(request,id=None):
    today = str(date.today())
    if has_group(request.user,"IT"):
       requests = Leave_Requests.objects.all().filter(department_name='IT').order_by('time_to_leave')
    elif has_group(request.user,"Investment"):
       requests = cartridges.objects.all().filter(department_name='Investment').order_by('time_to_leave')
    elif has_group(request.user,"Finance"):
       requests = cartridges.objects.all().filter(department_name='Finance').order_by('time_to_leave')
  
    return render(request, "Today_req_for_managers.html", { "requests":requests,})

#----------------------------------------------------------------------
@login_required
def Today_req_for_employees(request,id=None):
    today = str(date.today())
    requests = Leave_Requests.objects.all().filter(employee_name=request.user.get_full_name()).filter(time_to_leave=today).order_by('id')
    return render(request, "Today_req_for_employees.html", { "requests":requests,})    
#--------------------------------------
@login_required
def Today_req_for_managers(request,id=None):
    today = str(date.today())
    if has_group(request.user,"IT"):
       requests = Leave_Requests.objects.all().filter(department_name='IT').filter(time_to_leave=today).order_by('time_to_leave')
    elif has_group(request.user,"Investment"):
       requests = Leave_Requests.objects.all().filter(department_name='Investment').filter(time_to_leave=today).order_by('time_to_leave')
    elif has_group(request.user,"Finance"):    
       requests = Leave_Requests.objects.all().filter(department_name='Finance').filter(time_to_leave=today).order_by('time_to_leave')

    
    return render(request, "Today_req_for_managers.html", { "requests":requests,})        
#======================================================================================
# 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
@login_required
def Approve(request,id=None):
    Request = get_object_or_404(Leave_Requests,id=id)  
    if Request.request_revised == True:
       return HttpResponseRedirect(reverse('addition_Forbidden')) 
    else:
       Request.request_status = True
       Request.request_revised = True       
       Request.save()
       return HttpResponseRedirect(reverse('success')) 












#----------------------------------------------------------------------------
@login_required
def  Reject(request,id=None):
    Request = get_object_or_404(Leave_Requests,id=id)  
    if Request.request_revised == True:
       return HttpResponseRedirect(reverse('addition_Forbidden')) 
    else:
       Request.request_status = False
       Request.request_revised = True       
       Request.save()
       return HttpResponseRedirect(reverse('success'))  
     