# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.db import IntegrityError, transaction
from django.test import TestCase

from ..models import Status, Task
from ..exceptions import StateException


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

    def test_default_status(self):
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                Task.objects.create(name="fail task")
        status_on_review = Status.objects.create(name=Status.ON_REVIEW)
        task1 = Task.objects.create(name="task1")
        self.assertEquals(task1.status, status_on_review)

        status_new = Status.objects.create(name=Status.NEW)
        task2 = Task.objects.create(name="task2")
        self.assertEquals(task2.status, status_new)