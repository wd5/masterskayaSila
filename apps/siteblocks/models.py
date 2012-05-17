# -*- coding: utf-8 -*-
from datetime import datetime
from django.utils.translation import ugettext_lazy as _
from django.db import models
from apps.utils.utils import ImageField
import os
from pytils.translit import translify
from apps.utils.managers import PublishedManager


type_choices = (
    (u'input',u'input'),
    (u'textarea',u'textarea'),
    (u'redactor',u'redactor'),
)

class Settings(models.Model):
    title = models.CharField(
        verbose_name = u'Название',
        max_length = 150,
    )
    name = models.CharField( 
        verbose_name = u'Служебное имя',
        max_length = 250,
    )
    value = models.TextField(
        verbose_name = u'Значение'
    )
    type = models.CharField(
        max_length=20,
        verbose_name=u'Тип значения',
        choices=type_choices
    )
    class Meta:
        verbose_name =_(u'site_setting')
        verbose_name_plural =_(u'site_settings')

    def __unicode__(self):
        return u'%s' % self.name

def image_path_Blog(instance, filename):
    return os.path.join('images','blog', translify(filename).replace(' ', '_') )

class Blog(models.Model):
    title = models.CharField(max_length=255, verbose_name=u'название')
    short_description =  models.TextField(verbose_name = u'краткое описание')
    text =  models.TextField(verbose_name = u'текст')
    image = ImageField(upload_to=image_path_Blog, verbose_name=u'картинка')
    date_create = models.DateTimeField(verbose_name = u'дата публикации', default = datetime.now)
    is_published = models.BooleanField(verbose_name=u'опубликовано', default=True)

    objects = PublishedManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date_create']
        verbose_name = _(u'blog_item')
        verbose_name_plural = _(u'blog_items')

    def get_src_image(self):
        return self.image.url

