# -*- coding: utf-8 -*-
import os
from django.core.mail import EmailMultiAlternatives
from django.contrib.sites.models import Site
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template.loader import get_template
from sorl.thumbnail import ImageField as sorl_ImageField
from django.db import models
from django.template import Context
from django.db.models.loading import get_model
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
import settings
#from apps.siteblocks.models import Settings


class ImageField(models.ImageField, sorl_ImageField):
    pass

def random_key(length=6, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789'):
    from random import choice
    return ''.join([choice(allowed_chars) for i in range(length)])

def send_order_email(subject, html_content, email_list, file):
    current_site = Site.objects.get_current()

    email_from = u'«3DX Moscow Open» <reply@%s>' % current_site.domain
    text_content = u''

    if email_list:
        msg = EmailMultiAlternatives(subject, text_content, email_from, email_list)
        msg.attach_alternative(html_content, "text/html")
        msg.attach_file(file, mimetype="application/pdf")
        msg.send()

#def render_to_pdf(template_src, id_guest, context_dict):
#    from cStringIO import StringIO
#    response = HttpResponse(mimetype='application/pdf')
#    response['Content-Disposition'] = 'attachment; filename=somefilename.pdf'
#    template = get_template(template_src)
#    context = Context(context_dict)
#    html = template.render(context)
#    result = StringIO()
#
#    file_name = 'guest_%s.pdf' % id_guest
#    path_name = settings.MEDIA_ROOT + 'uploads/files/guests/' + file_name
#    destination = open(path_name, 'wb+')
#
#    pdf = pisa.pisaDocument(StringIO(html.encode("utf-8")), result, show_error_as_pdf=True, encoding='utf-8', )
#
#    destination.write(result.getvalue())
#    destination.close()
#    return u'%s' % path_name


#def send_emails(m, file):
#    admin_email = Settings.objects.get(name = 'email_notification').value
#    email_list = [u'%s' % admin_email,]
#    subject = u'Новый зарегистрированный гость'
#    html_content = u'''
#        <p style="font-size: 12px;">Здравствуйте.<br /><br />Новый зарегистрированный гость.</p>
#        <p style="padding-left: 10px; font-style: italic; font-size: 12px;
#        border-left: 2px solid #666;">
#        <b>Номер п/п:</b> %s<br />
#        <b>ФИО:</b> %s<br />
#        <b>E-mail:</b> %s<br />
#        <b>Телефон:</b> %s<br />
#        <b>Уникальный ключ:</b> %s</p>
#        <p><a href="http://3dxopen.ru/admin/members/guests/%s/">перейти к просмотру</a></p>''' % \
#           (m.id, m.name, m.email, m.phone, m.key, m.id)
#
#    send_order_email(subject, html_content, email_list, file)
#
#    email_list = [u'%s' % m.email,]
#    subject = u'Приглашение на 3DX Moscow Open'
#    html_content = u'''
#        <p style="font-size: 12px;">Здравствуйте.<br /><br />Пропуск успешно выписан(см. прикрепления).</p>
#        <p style="padding-left: 10px; font-style: italic; font-size: 12px;
#        border-left: 2px solid #666;">
#        <b>Номер п/п:</b> %s<br />
#        <b>ФИО:</b> %s<br />
#        <b>E-mail:</b> %s<br />
#        <b>Телефон:</b> %s<br /></p>''' % \
#           (m.id, m.name, m.email, m.phone)
#
#    send_order_email(subject, html_content, email_list, file)

@csrf_exempt
def items_loader(request):
    if not request.is_ajax():
        return HttpResponseRedirect('/')
    else:
        if 'cnt' not in request.POST or 'init_cnt' not in request.POST or 'm_name' not in request.POST or 'a_name' not in request.POST:
            return HttpResponseBadRequest()

        count = request.POST['cnt']
        try:
            count = int(count)
        except ValueError:
            return HttpResponseBadRequest()

        initial_count = request.POST['init_cnt']
        try:
            initial_count = int(initial_count)
        except ValueError:
            return HttpResponseBadRequest()

        app_name = request.POST['a_name']
        model_name = request.POST['m_name']
        model = get_model(app_name, model_name)
        endrange = initial_count + count

        if model:
            try:
                queryset = model.objects.published()
                remaining_count = queryset.count() - endrange
                queryset = queryset[initial_count:endrange]
                if count<remaining_count:
                    remaining_count = False
            except model.DoesNotExist:
                return HttpResponseBadRequest()
        else:
            return HttpResponseBadRequest()

        response = HttpResponse()
        load_template = 'items_loader/%s_load_template.html' % model_name
        items_html = render_to_string(
            'items_loader/base_loader.html',
            {'items': queryset, 'load_template': load_template, 'endrange':endrange, 'remaining_count':remaining_count, }
        )
        response.content = items_html
        return response