# -*- coding: utf-8 -*-
from django.db import models
import os
from django.db.models.aggregates import Sum,Count
from pytils.translit import translify
from apps.utils.managers import PublishedManager
from apps.utils.utils import ImageField
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

def image_path_work_category(instance, filename):
    return os.path.join('images','worksCategory', translify(filename).replace(' ', '_') )

class WorkCategory(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'название')
    image = ImageField(upload_to=image_path_work_category, verbose_name=u'картинка')
    short_description =  models.TextField(verbose_name = u'краткое описание')
    description =  models.TextField(verbose_name = u'описание')
    slug = models.SlugField(verbose_name=u'Алиас', help_text=u'уникальное имя на латинице')
    works_count = models.IntegerField(verbose_name = u'количество отображаемых работ', help_text=u'Количество работ для начального отображения в категории.', default=2)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'category')
        verbose_name_plural = _(u'categories')

    def get_absolute_url(self):
        return reverse('show_work_category',kwargs={'slug': '%s' % self.slug})

    def get_src_image(self):
        return self.image.url

    def get_works(self):
        return self.work_set.published()

def image_path_client(instance, filename):
    return os.path.join('images','clients', translify(filename).replace(' ', '_') )

class Client(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'название')
    image = ImageField(upload_to=image_path_client, verbose_name=u'картинка')
    description =  models.TextField(verbose_name = u'описание')
    slug = models.SlugField(verbose_name=u'Алиас', help_text=u'уникальное имя на латинице')
    is_at_clientblock = models.BooleanField(verbose_name=u'отображать в блоке «Клиенты»', default=True)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'client')
        verbose_name_plural = _(u'clients')

    def get_absolute_url(self):
        return reverse('show_client',kwargs={'slug': '%s' % self.slug})

    def get_src_image(self):
        return self.image.url

    def get_works(self):
        return self.work_set.published()

    def get_works_categories(self):
        categories = self.work_set.values('workcategory').annotate(count=Count).order_by('count')
        return categories

class Work(models.Model):
    workcategory = models.ForeignKey(WorkCategory, verbose_name=u'категория работ')
    client = models.ForeignKey(Client, verbose_name=u'клиент')
    title = models.CharField(max_length=255, verbose_name=u'название')
    slug = models.SlugField(verbose_name=u'Алиас', help_text=u'уникальное имя на латинице')
    is_at_category_list = models.BooleanField(verbose_name=u'отображать в списке категорий', default=True)
    is_on_main = models.BooleanField(verbose_name=u'отображать в блоке на главной', default=False)
    date_create = models.DateTimeField(verbose_name = u'дата создания', default = datetime.now)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'work')
        verbose_name_plural = _(u'works')

    def get_works_media(self):
            return self.worksmedia_set.all()


def image_path_media(instance, filename):
    return os.path.join('images','worksMedia', translify(filename).replace(' ', '_') )

class WorksMedia(models.Model):
    work = models.ForeignKey(Work, verbose_name=u'работа')
    image = ImageField(upload_to=image_path_media, verbose_name=u'изображение')
    code_video = models.TextField(verbose_name=u'код видеоролика', blank=True)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)

    def __unicode__(self):
           return self.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'media_item')
        verbose_name_plural = _(u'media_items')

    def get_src_image(self):
            return self.image.url






