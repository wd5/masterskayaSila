# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django import forms
from apps.utils.widgets import Redactor
from sorl.thumbnail.admin import AdminImageMixin
from mptt.admin import MPTTModelAdmin


from models import *

class CategoryAdmin(AdminImageMixin, MPTTModelAdmin):
    list_display = ('id','name','parent','alias','order','show',)
    list_display_links = ('id','name',)
    list_editable = ('order','show',)

admin.site.register(Category, CategoryAdmin)

class PhotoInline(admin.TabularInline):
    model = Photo
#--Виджеты jquery Редактора
class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=Redactor(attrs={'cols': 110, 'rows': 20}), required=False)
    description.label=u'Описание'

    full_description = forms.CharField(widget=Redactor(attrs={'cols': 110, 'rows': 20}), required=False)
    full_description.label=u'Полное описание'

    class Meta:
        model = Product
#--Виджеты jquery Редактора
class ProductAdmin(AdminImageMixin, admin.ModelAdmin):
    list_display = ('id','name', 'category','price','old_price','top', 'order','show',)
    list_display_links = ('id','name',)
    list_editable = ('top','order','show',)
    list_filter = ('show','top',)
    search_fields = ('name', 'description', 'full_description',)
    inlines = [PhotoInline]
    form = ProductAdminForm

admin.site.register(Product, ProductAdmin)

class PhraseAdmin(admin.ModelAdmin):
    list_display = ('id','example',)
    list_display_links = ('id','example',)
    search_fields = ('example',)

admin.site.register(Phrase, PhraseAdmin)