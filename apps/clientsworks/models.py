# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import os
from pytils.translit import translify
from apps.utils.managers import PublishedManager
from apps.utils.utils import ImageField
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

def image_path_work_category(instance, filename):
    return os.path.join('images','clientWorksCategory', translify(filename).replace(' ', '_') )

class ClientsWorkCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'название')
    image = ImageField(upload_to=image_path_work_category, verbose_name=u'картинка', blank=True)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'client_category')
        verbose_name_plural = _(u'client_categories')

    def get_src_image(self):
        if self.image:
            return self.image.url
        else:
            return False

    def get_works(self):
        return self.clientswork_set.published()

def image_path_client(instance, filename):
    return os.path.join('images','clients', translify(filename).replace(' ', '_') )

class Profile(models.Model):
    user = models.ManyToManyField(User, verbose_name=u'пользователь', blank=True)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return u'профиль №%s' % self.id

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'profile')
        verbose_name_plural = _(u'profiles')

    def get_works(self):
        return self.clientswork_set.published()

    def get_new_works(self):
        return self.clientswork_set.published().filter(is_new=True)

    def get_works_categories_and_works(self):
        categories = ClientsWorkCategory.objects.published()
        for item in categories:
            work = ClientsWork.objects.published().filter(profile=self.id, workcategory = item)[:5]
            if work:
                setattr(item, 'works', work)
        return categories

    def get_documents(self):
        return self.document_set.published()

    def get_documents_categories_and_docs(self):
        categories = DocumentsCategory.objects.published()
        for item in categories:
            docs = Document.objects.published().filter(profile=self.id, category = item)[:3]
            if docs:
                setattr(item, 'docs', docs)
        return categories

    def get_work_add_parameter(self):
        return "get_works().filter(profile='%s')" % self.id

    def get_doc_add_parameter(self):
        return "get_docs().filter(profile='%s')" % self.id

    def prof_title(self):
        user_set = self.user.all()
        if user_set:
            str = ''
            for user in user_set:
                str='%s, %s' % (user.first_name,str)
            return u'%s' % str[:-2]
        else:
            return u'не выбрано'
    prof_title.allow_tags = True
    prof_title.short_description = 'Пользователи'

def image_path_ClientMedia(instance, filename):
    return os.path.join('images','clientWorksMedia', translify(filename).replace(' ', '_') )

class ClientsWork(models.Model):
    workcategory = models.ForeignKey(ClientsWorkCategory, verbose_name=u'категория работ')
    profile = models.ForeignKey(Profile, verbose_name=u'профиль клиента')
    title = models.CharField(max_length=255, verbose_name=u'название')
    is_new = models.BooleanField(verbose_name=u'новая работа', default=True)
    date_create = models.DateTimeField(verbose_name = u'дата создания')
    image = ImageField(upload_to=image_path_ClientMedia, verbose_name=u'изображение')
    code_video = models.TextField(verbose_name=u'код видеоролика', blank=True)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'client_work')
        verbose_name_plural = _(u'client_works')

    def get_src_image(self):
        return self.image.url

class DocumentsCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'название')
    show_count = models.IntegerField(verbose_name = u'количество отображаемых документов', help_text=u'Количество документов для начального отображения в категории.', default=3)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'documents_category')
        verbose_name_plural = _(u'documents_categories')

    def get_docs(self):
        return self.document_set.published()

class Document(models.Model):
    profile = models.ForeignKey(Profile, verbose_name=u'профиль клиента')
    category = models.ForeignKey(DocumentsCategory, verbose_name=u'категория')
    title = models.CharField(max_length=255, verbose_name=u'название')
    date_create = models.DateTimeField(verbose_name = u'дата создания')
    document = models.FileField(upload_to='documents/', verbose_name=u'файл документа')
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'document')
        verbose_name_plural = _(u'documents')

    def get_file_path(self):
        return self.document.url






