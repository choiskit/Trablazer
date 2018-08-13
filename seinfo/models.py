# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class IDCInfo(models.Model):
    name = models.CharField(max_length=20,verbose_name=u'机房名称')
    address = models.CharField(max_length=100,verbose_name=u'机房位置')
    phone = models.CharField(max_length=15,verbose_name=u'机房电话')
    codeid = models.CharField(max_length=50, verbose_name=u'客户号')

    class Meta:
        verbose_name = u'机房信息表'
        verbose_name_plural = verbose_name
        db_table = "idcinfo"

class CabInfo(models.Model):
    cablocate = models.CharField(max_length=20,verbose_name=u'机柜位置')
    IDCid = models.ForeignKey('IDCInfo')

    class Meta:
        verbose_name = u'机柜信息表'
        verbose_name_plural = verbose_name
        db_table = "cabinfo"


class ServerInfo(models.Model):
    type = models.CharField(max_length=20,verbose_name=u'服务器型号')
    serial = models.CharField(max_length=50, verbose_name=u'序列号')
    ipaddr = models.CharField(max_length=20,verbose_name=u'服务器IP地址')
    CabID = models.ForeignKey('CabInfo')

    class Meta:
        verbose_name = u'服务器信息表'
        verbose_name_plural = verbose_name
        db_table = "serverinfo"

