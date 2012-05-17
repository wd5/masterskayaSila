# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.clientsworks.models import ClientsWork,ClientsWorkCategory,Document,DocumentsCategory,Profile
from apps.utils.widgets import Redactor,AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin

class ClientsWorkCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','order','is_published',)
    list_display_links = ('id','title',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)
    search_fields = ('title',)
admin.site.register(ClientsWorkCategory, ClientsWorkCategoryAdmin)

class DocumentsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title','show_count','order','is_published',)
    list_display_links = ('id','title',)
    list_editable = ('order','show_count','is_published',)
    list_filter = ('is_published',)
admin.site.register(DocumentsCategory, DocumentsCategoryAdmin)

class DocumentInline(AdminImageMixin,admin.TabularInline):
    model = Document

class ClientsWorkInline(AdminImageMixin,admin.TabularInline):
    model = ClientsWork

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','user','order','is_published',)
    list_display_links = ('id','user',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)
    inlines = [
        ClientsWorkInline,
        DocumentInline
    ]
admin.site.register(Profile, ProfileAdmin)


#class ClientsWorkAdmin(admin.ModelAdmin):
#    list_display = ('id','title','slug','date_create','is_published',)
#    list_display_links = ('id','title','date_create','slug',)
#    list_editable = ('is_published',)
#    list_filter = ('is_published','date_create',)
#    search_fields = ('title','description',)
#    inlines = [
#        WorksMeidaInline
#    ]
#
#admin.site.register(ClientsWork, ClientsWorkAdmin)