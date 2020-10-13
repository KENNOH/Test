from __future__ import absolute_import, unicode_literals
import django_tables2 as tables
from django.utils.html import format_html
from django_tables2.utils import A
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Asset, Attachments



class AssetTable(tables.Table):
    edit = tables.LinkColumn('edit', args=[A('pk')], verbose_name="Edit Record", orderable=False, empty_values=())
    delete = tables.LinkColumn('delete', args=[A('pk')], verbose_name="Delete Record", orderable=False, empty_values=())


    def render_edit(self, record):
        return format_html('<a href='+reverse("edit", args=[record.pk])+'><input class="btn btn-info btn-sm btn-block" type="Submit" id="button1" value="Edit" /></a>')

    def render_delete(self, record):
        return format_html('<a href='+reverse("delete", args=[record.pk])+'><input class="btn btn-danger btn-sm btn-block" type="Submit" id="button1" value="Delete" /></a>')


    class Meta:
        model = Asset
        fields = ('asset_code', 'name', 'user', 'purchase_date','cost','description','edit')
