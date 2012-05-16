# -*- coding: utf-8 -*-
import os, datetime
from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

from pytils.translit import translify
from django.core.urlresolvers import reverse

from sorl.thumbnail import ImageField
from mptt.models import MPTTModel, TreeForeignKey, TreeManager

from apps.utils.managers import VisibleObjects


def file_path_Category(instance, filename):
    return os.path.join('images','category',  translify(filename).replace(' ', '_') )
class Category(MPTTModel):
    parent = TreeForeignKey('self', verbose_name=u'Категория', related_name='children', blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(verbose_name=u'Название', max_length=100)
    alias = models.CharField(verbose_name=u'Алиас', max_length=100, unique=True)
    image = ImageField(verbose_name=u'Картинка', upload_to=file_path_Category)
    order = models.IntegerField(verbose_name=u'Порядок сортировки',default=10)
    show = models.BooleanField(verbose_name=u'Отображать', default=True)

    objects = TreeManager()

    def __unicode__(self):
            return self.name

    class Meta:
        verbose_name =_(u'category')
        verbose_name_plural =_(u'categories')
        ordering = ['-order', 'name']

    class MPTTMeta:
            order_insertion_by = ['order']


    def get_absolute_url(self):
        return u'' #self.alias


def str_price(price):
    if not price:
        return u'0'
    value = u'%s' %price
    if price._isinteger():
        value = u'%s' %value[:len(value)-3]
        count = 3
    else:
        count = 6

    if len(value)>count:
        ends = value[len(value)-count:]
        starts = value[:len(value)-count]

        return u'%s %s' %(starts, ends)
    else:
        return value


def file_path_Product(instance, filename):
    return os.path.join('images','products',  translify(filename).replace(' ', '_') )
class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=u'Категория')
    name = models.CharField(verbose_name=u'Название', max_length=400)
    description = models.TextField(blank=True)
    full_description = models.TextField(blank=True)
    image = ImageField(verbose_name=u'Картинка', upload_to=file_path_Product,blank=True)
    price = models.DecimalField(verbose_name=u'Цена', decimal_places=2, max_digits=10, blank=True, null=True)
    old_price = models.DecimalField(verbose_name=u'Старая цена', decimal_places=2, max_digits=10, blank=True, null=True)

    top = models.BooleanField(verbose_name=u'Лидер', default=False)

    count = models.IntegerField(verbose_name=u'Остаток', default=0, blank=True)

    order = models.IntegerField(verbose_name=u'Порядок сортировки',default=10)
    show = models.BooleanField(verbose_name=u'Отображать', default=True)

    objects = models.Manager() # The default manager.
    items = VisibleObjects() # The visible objects manager.

    class Meta:
        verbose_name =_(u'product_item')
        verbose_name_plural =_(u'product_items')
        ordering = ['-order', 'name']

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products_detail',kwargs={'pk': '%s'%self.id})


    def get_str_price(self):
        return str_price(self.price)

    def get_str_old_price(self):
        return str_price(self.old_price)

    def get_photos(self):
        return self.photo_set.all()


def file_path_Product(instance, filename):
     return os.path.join('images','products',  translify(filename).replace(' ', '_') )
class Photo(models.Model):
    product = models.ForeignKey(Product, verbose_name=u'Товар')
    image = ImageField(verbose_name=u'Картинка', upload_to=file_path_Product)

    class Meta:
        verbose_name =_(u'product_photo')
        verbose_name_plural =_(u'product_photos')

    def __unicode__(self):
        return u'Фото товара %s' %self.product.name


#Класс фраз для поиска
class Phrase(models.Model):
    example = models.CharField(verbose_name=u'Пример фразы', max_length=100)

    class Meta:
        verbose_name =_(u'phrase')
        verbose_name_plural =_(u'phrases')

    def __unicode__(self):
        return self.example
