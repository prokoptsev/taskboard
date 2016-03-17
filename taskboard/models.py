# coding: utf-8
from __future__ import unicode_literals
from django.db import models
from django.utils.six.moves import range
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

from .exceptions import StateException


@python_2_unicode_compatible
class Status(models.Model):
    NEW, IN_PROGRESS, ON_REVIEW, TESTED, DELIVERED = range(10, 60, 10)
    AVAILABLE_STATUSES = (
        (NEW, _('new')),
        (IN_PROGRESS, _('in progress')),
        (ON_REVIEW, _('on review')),
        (TESTED, _('tested')),
        (DELIVERED, _('delivered')),
    )

    name = models.IntegerField(_("Name"), choices=AVAILABLE_STATUSES, unique=True)

    class Meta:
        verbose_name = _("Status")
        verbose_name_plural = _("Statuses")
        ordering = ("name",)

    def __str__(self):
        return self.get_name_display()

    def save(self, *args, **kwargs):
        if self.name not in (i for i, _ in self.AVAILABLE_STATUSES):
            raise StateException("Not permitted state.")
        super(Status, self).save(*args, **kwargs)


@python_2_unicode_compatible
class Task(models.Model):
    name = models.CharField(_("Name"), max_length=255)
    status = models.ForeignKey("Status", verbose_name=_("Status"), related_name="tasks")

    class Meta:
        verbose_name = _("Task")
        verbose_name_plural = _("Tasks")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.id and not hasattr(self, 'status'):
            self.set_default_status()
        super(Task, self).save(*args, **kwargs)

    def set_default_status(self):
        """
        Добавить начальный статус.

        Если статус не установлен выбрать из существуюших статусов с наименьшм значением.
        """
        if Status.objects.exists():
            self.status = Status.objects.order_by("name")[0]