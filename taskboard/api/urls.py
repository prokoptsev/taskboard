# coding: utf-8
from __future__ import unicode_literals, absolute_import
from rest_framework import routers
from .views import StatusViewSet, BoardViewSet, TaskViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'board', BoardViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'tasks', TaskViewSet)
urlpatterns = router.urls
