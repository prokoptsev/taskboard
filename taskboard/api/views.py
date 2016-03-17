# coding: utf-8
from __future__ import unicode_literals, absolute_import
from rest_framework import viewsets, mixins
from .serializers import StatusSerializer, TaskWithStatusSerializer, BoardSerializer
from ..models import Status, Task


class BoardViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Status.objects.prefetch_related("tasks")
    serializer_class = BoardSerializer


class StatusViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related("status")
    serializer_class = TaskWithStatusSerializer
