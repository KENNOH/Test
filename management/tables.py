from __future__ import absolute_import, unicode_literals
import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Asset, Attachments



class AssetTable(tables.Table):
    class Meta:
        model = Asset
        fields = ('asset_code', 'name', 'user', 'purchase_date','cost','description')
