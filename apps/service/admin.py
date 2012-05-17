# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.service.models import Work,WorkCategory,WorksMedia,Client
from apps.utils.widgets import Redactor,AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin

class WorkCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = WorkCategory

    class Media:
        js = (
            '/media/js/jquery.js',
            '/media/js/clientadmin.js',
            '/media/js/jquery.synctranslit.js',
            )

class WorkCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','order','is_published',)
    list_display_links = ('id','title','slug',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)
    search_fields = ('title','short_description','description',)
    form = WorkCategoryAdminForm
admin.site.register(WorkCategory, WorkCategoryAdmin)

class ClientAdminForm(forms.ModelForm):
    class Meta:
        model = Client

    class Media:
        js = (
            '/media/js/jquery.js',
            '/media/js/clientadmin.js',
            '/media/js/jquery.synctranslit.js',
            )

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','order','is_published',)
    list_display_links = ('id','title','slug',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)
    search_fields = ('title','description',)
    form = ClientAdminForm
admin.site.register(Client, ClientAdmin)

class WorksMeidaInline(AdminImageMixin,admin.TabularInline):
    model = WorksMedia

class WorkAdminForm(forms.ModelForm):
    class Meta:
        model = Work

    class Media:
        js = (
            '/media/js/jquery.js',
            '/media/js/clientadmin.js',
            '/media/js/jquery.synctranslit.js',
            )

class WorkAdmin(admin.ModelAdmin):
    list_display = ('id','title','slug','date_create','is_published',)
    list_display_links = ('id','title','date_create','slug',)
    list_editable = ('is_published',)
    list_filter = ('is_published','date_create',)
    search_fields = ('title','description',)
    form = WorkAdminForm
    inlines = [
        WorksMeidaInline
    ]

admin.site.register(Work, WorkAdmin)