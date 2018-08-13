# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from seinfo import models

# Create your views here.

def insert(request):
    if request.method == "POST":
        name = request.POST.get("name",None)
        address = request.POST.get("address",None)
        phone = request.POST.get("phone",None)
        codeid = request.POST.get("codeid",None)
        idc = models.IDCInfo.objects.create(name=name,address=address,phone=phone,codeid=codeid)

        cablocate = request.POST.get("cablocate",None)
        IDCid_id = idc.id
        cab = models.CabInfo.objects.create(cablocate=cablocate,IDCid_id=IDCid_id)

        setype = request.POST.get("setype",None)
        serial = request.POST.get("serial",None)
        ipaddr = request.POST.get("ipaddr",None)
        CabID_id =cab.id
        models.ServerInfo.objects.create(type=setype, serial=serial, ipaddr=ipaddr, CabID_id=CabID_id)
    server_list = models.IDCInfo.objects.all()




    return render(request,'insert.html',{"server_list":server_list})


def list(request):
    server_list = models.IDCInfo.objects.all()
    return render(request,'show.html',{"server_list":server_list})