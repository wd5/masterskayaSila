# -*- coding: utf-8 -*-
from django.contrib import admin
from django import forms
from apps.siteblocks.models import Settings,Blog
from apps.utils.widgets import Redactor,RedactorMini
from sorl.thumbnail.admin import AdminImageMixin

#--Виджеты jquery Редактора
class SettingsAdminForm(forms.ModelForm):
    class Meta:
        model = Settings

    def __init__(self, *args, **kwargs):
        super(SettingsAdminForm, self).__init__(*args, **kwargs)
        try:
            instance = kwargs['instance']
        except KeyError:
            instance = False
        if instance:
            if instance.type == u'input':
                self.fields['value'].widget = forms.TextInput()
            elif instance.type == u'textarea':
                self.fields['value'].widget = forms.Textarea()
            elif instance.type == u'redactor':
                self.fields['value'].widget = Redactor(attrs={'cols': 100, 'rows': 10},)

#--Виджеты jquery Редактора

class SettingsAdmin(admin.ModelAdmin):
    list_display = ('title','value',)
    fields = ('title','value',)
    form = SettingsAdminForm
admin.site.register(Settings, SettingsAdmin)

class BlogAdminForm(forms.ModelForm):
    text = forms.CharField(widget=Redactor(attrs={'cols': 100, 'rows': 20}))
    text.label=u'Текст'

    class Meta:
        model = Blog

class BlogAdmin(AdminImageMixin,admin.ModelAdmin):
    list_display = ('id','title','date_create','is_published',)
    list_display_links = ('id','title','date_create',)
    list_editable = ('is_published',)
    list_filter = ('is_published','date_create',)
    search_fields = ('text','short_description','title',)
    form = BlogAdminForm
admin.site.register(Blog, BlogAdmin)

