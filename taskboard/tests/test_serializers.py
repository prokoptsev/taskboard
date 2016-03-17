# coding: utf-8
from __future__ import unicode_literals, absolute_import
from django.test import TestCase

from ..models import Task, Status
from ..api.serializers import TaskSerializer, StatusSerializer, BoardSerializer


class TaskSerializerTestCase(TestCase):
    def test(self):
        serialized_task = TaskSerializer(Task(id=1, name="test"))
        self.assertEqual(
            serialized_task.data,
            {"id": 1, "name": "test"}
        )


class StatusSerializerTestCase(TestCase):
    def test(self):
        status = Status(id=1, name=Status.NEW)
        serializer_status = StatusSerializer(status)
        self.assertEquals(
            serializer_status.data,
            {"id": 1, "name": dict(Status.AVAILABLE_STATUSES)[Status.NEW]}
        )


class BoardSerializerTestCase(TestCase):
    def test(self):
        status = Status.objects.create(id=1, name=Status.NEW)
        Task.objects.create(id=1, name="test", status=status)
        board_serializer = BoardSerializer(Status.objects.all(), many=True)
        self.assertEquals(
            board_serializer.data,
            [
                {
                    "id": 1,
                    "name": dict(Status.AVAILABLE_STATUSES)[Status.NEW],
                    "tasks": [
                        {"id": 1, "name": "test"}
                    ]
                }
            ]
        )


