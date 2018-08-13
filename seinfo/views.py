# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import IDCInfo 
from .forms import IDCInfoForm

# Create your views here.



# 添加机房信息.
def idc_add(request):
    if request.method == 'POST':
        form = IDCInfoForm(request.POST)
	if form.is_valid():
	    idcinfo = form.save()
	    return HttpResponse('add sucess')
    else:
        form = IDCInfoForm()
	
    return render(request,'idc_add.html',{'form': form})



#更新机房信息
def idc_update(request,idc_id):
    idcinfo = get_object_or_404(IDCInfo, id=idc_id)

    if request.method == 'GET':
        form = IDCInfoForm(instance=idcinfo)
	return render(request,'idc_add.html', {'form': form})
    elif request.method == 'POST':
        form = IDCInfoForm(request.POST, instance=idcinfo)
	if form.is_valid():
	    form.save()
	    return HttpResponse('update sucess')
    return HttpResponse('Valid')
