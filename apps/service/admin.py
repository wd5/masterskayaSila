# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.service.models import Work,WorkCategory,WorksMedia,Client
from apps.utils.widgets import Redactor,AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin

class WorkCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','order','is_published',)
    list_display_links = ('id','title','slug',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)
    search_fields = ('title','short_description','description',)
admin.site.register(WorkCategory, WorkCategoryAdmin)

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','order','is_published',)
    list_display_links = ('id','title','slug',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)
    search_fields = ('title','description',)
admin.site.register(Client, ClientAdmin)

class WorksMeidaInline(AdminImageMixin,admin.TabularInline):
    model = WorksMedia

class WorkAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','date_create','is_published',)
    list_display_links = ('id','title','date_create','slug',)
    list_editable = ('is_published',)
    list_filter = ('is_published','date_create',)
    search_fields = ('title','description',)
    inlines = [
        WorksMeidaInline
    ]

admin.site.register(Work, WorkAdmin)