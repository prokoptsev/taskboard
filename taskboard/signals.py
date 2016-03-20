# coding: utf-8
from __future__ import unicode_literals, absolute_import
import json

from ws4redis.publisher import RedisPublisher
from ws4redis.redis_store import RedisMessage
from django.db.models.signals import post_save, post_delete

from .models import Task, Status


def _send_change_broadcast(*args, **kwargs):
    redis_publisher = RedisPublisher(facility='tasks', broadcast=True)
    redis_publisher.publish_message(RedisMessage(json.dumps({
        'update': True
    })))

post_save.connect(_send_change_broadcast, sender=Task, dispatch_uid="taskboard_update_by_create_task")
post_delete.connect(_send_change_broadcast, sender=Task, dispatch_uid="taskboard_update_by_delete_task")
post_save.connect(_send_change_broadcast, sender=Status, dispatch_uid="taskboard_update_by_create_status")
post_delete.connect(_send_change_broadcast, sender=Status, dispatch_uid="taskboard_update_by_delete_status")
