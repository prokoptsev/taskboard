# coding: utf-8
from __future__ import unicode_literals, absolute_import
from rest_framework import viewsets, mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .serializers import StatusSerializer, TaskWithStatusSerializer, BoardSerializer
from ..models import Status, Task


class CSRFExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        pass


class CSRFExemptMixin(object):
    authentication_classes = (CSRFExemptSessionAuthentication, BasicAuthentication)


class BoardViewSet(CSRFExemptMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Status.objects.prefetch_related("tasks")
    serializer_class = BoardSerializer


class StatusViewSet(CSRFExemptMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class TaskViewSet(CSRFExemptMixin, viewsets.ModelViewSet):
    queryset = Task.objects.select_related("status")
    serializer_class = TaskWithStatusSerializer
