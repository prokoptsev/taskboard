# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import IntegrityError
from django.test import TestCase

from .models import Status, Task
from .exceptions import StateException


class StatusModelTestCase(TestCase):
    def test_status_save(self):
        Status.objects.create(name=Status.NEW)
        Status.objects.create(name=Status.IN_PROGRESS)
        Status.objects.create(name=Status.ON_REVIEW)
        Status.objects.create(name=Status.TESTED)
        Status.objects.create(name=Status.DELIVERED)

    def test_unique_status(self):
        Status.objects.create(name=Status.NEW)
        with self.assertRaises(IntegrityError):
            Status.objects.create(name=Status.NEW)

    def test_create_not_permitted_status(self):
        not_permitted_status = 42
        with self.assertRaises(StateException):
            Status.objects.create(name=not_permitted_status)

    def test_representation(self):
        status = Status(name=Status.NEW)
        self.assertEquals(str(status), dict(Status.AVAILABLE_STATUSES)[Status.NEW])


class TaskModelTestCase(TestCase):
    def test_representation(self):
        task = Task(name="task name")
        self.assertEquals(str(task), task.name)
