# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class MenuType(models.Model):
    menu_type = models.CharField(max_length=30)


class MenuItem(models.Model):
    item_name = models.CharField(max_length=60)
    item_price = models.FloatField(max_length=5)
    item_type = models.ForeignKey(MenuType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.item_type) + ":\n" + str(self.item_name) + ": " + str(self.item_price) + " TL"

