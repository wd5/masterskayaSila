# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
from apps.clientsworks.models import ClientsWork,ClientsWorkCategory,Document,DocumentsCategory,Profile
from apps.utils.widgets import Redactor,AdminImageWidget
from sorl.thumbnail.admin import AdminImageMixin

class ClientsWorkCategoryAdmin(AdminImageMixin,admin.ModelAdmin):
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
    extra = 0

class ClientsWorkForm(forms.ModelForm):
    class Meta:
        model = ClientsWork

    class Media:
        js = (
            '/media/js/jquery.js',
            '/media/js/clientwork_hidetextarea.js'
            )

class ClientsWorkInline(AdminImageMixin,admin.TabularInline):
    model = ClientsWork
    form = ClientsWorkForm
    extra = 0

class ProfileAdminForm(forms.ModelForm):
    user = forms.ModelMultipleChoiceField(queryset=User.objects.filter(is_staff=False),widget=forms.CheckboxSelectMultiple(),required=False, label='Пользователи')
    class Meta:
        model = Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','prof_title','order','is_published',)
    list_display_links = ('id',)
    list_editable = ('order','is_published',)
    list_filter = ('is_published',)
    form = ProfileAdminForm
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