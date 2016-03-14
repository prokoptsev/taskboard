# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.contrib import admin

from .models import Status, Task


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass
