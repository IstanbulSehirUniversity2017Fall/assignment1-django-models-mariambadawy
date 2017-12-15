# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import MenuItem


def index(request):

    html = ''
    for menu in MenuItem.objects.all():
        url = '/Menu/%s/' % (str(menu.id))
        name_of_item = menu.item_name
        price_of_item = menu.item_price
        html += '<a href= "' + url + '">' + str(name_of_item) + " : " + str(price_of_item) + ' TL' + '</a>'

        return HttpResponse("<h1> Welcome to Safroot's Pancakes Cafe! Here's the Menu:</h1>" + html)


def detail(request, menu_id):
    return HttpResponse("<h2>Details for %s :</h2>" % (str(menu_id)))

