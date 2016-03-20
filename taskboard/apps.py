# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class TaskBoardConfig(AppConfig):
    name = 'taskboard'
    verbose_name = _('Taskboard')

    def ready(self):
        import taskboard.signals
