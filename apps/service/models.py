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
    short_description_on_main =  models.CharField(max_length=255, verbose_name = u'краткое описание отображаемое на главной странице', blank=True)
    additional_text =  models.TextField(verbose_name = u'текст для врезки')
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

    def get_works_at_list(self):
        return self.work_set.published().filter(is_at_category_list=True)

    def get_works_to_show(self):
        return self.work_set.published()[:self.works_count]

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
        #return u'/clients/%s/' % self.slug

    def get_src_image(self):
        return self.image.url

    def get_works(self):
        return self.work_set.published()

    def get_works_categories(self):
        works = self.get_works()
        categories_id_list = works.distinct().values_list('workcategory', flat=True)
        categories = WorkCategory.objects.published().filter(id__in=categories_id_list)
        return categories

    def get_works_categories_and_works(self):
        categories = WorkCategory.objects.published()
        for item in categories:
            work = Work.objects.published().filter(client=self.id, workcategory = item)[:2]
            if work:
                setattr(item, 'works', work)
        return categories

    def get_add_parameter(self):
        return "get_works().filter(client='%s')" % self.id

def image_path_works(instance, filename):
    return os.path.join('images','works', translify(filename).replace(' ', '_') )

class Work(models.Model):
    workcategory = models.ForeignKey(WorkCategory, verbose_name=u'категория работ')
    client = models.ForeignKey(Client, verbose_name=u'клиент')
    title = models.CharField(max_length=255, verbose_name=u'название')
    image = ImageField(upload_to=image_path_works, verbose_name=u'картинка')
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

    def get_src_image(self):
            return self.image.url

    def get_absolute_url(self):
        id_cat = self.workcategory.id
        if id_cat==4:
            href = 'video_examples'
        elif id_cat==2:
            href = 'foto_examples'
        elif id_cat==3:
            href = 'smi_examples'
        elif id_cat==5:
            href = 'design_examples'
        elif id_cat==1:
            href = 'out_adv_examples'
        elif id_cat==6:
            href = 'pred_examples'
        else:
            href = ''

        return u'%s#%s' % (self.client.get_absolute_url(), href)

    def get_works_media(self):
        return self.worksmedia_set.all()

def image_path_media(instance, filename):
    return os.path.join('images','worksMedia', translify(filename).replace(' ', '_') )

class WorksMedia(models.Model):
    work = models.ForeignKey(Work, verbose_name=u'работа')
    image = ImageField(upload_to=image_path_media, verbose_name=u'изображение')
    code_video = models.TextField(verbose_name=u'код видеоролика', blank=True)
    order = models.IntegerField(u'порядок сортировки', help_text=u'Чем больше число, тем выше располагается элемент', default=10)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()


    def __unicode__(self):
           return u'контент к работе %s' % self.work.title

    class Meta:
        ordering = ['-order']
        verbose_name = _(u'media_item')
        verbose_name_plural = _(u'media_items')

    def get_src_image(self):
        return self.image.url






