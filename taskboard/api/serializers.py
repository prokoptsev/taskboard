# coding: utf-8
from __future__ import unicode_literals, absolute_import
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _

from ..models import Task, Status


class StatusSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_name_display')

    class Meta:
        model = Status
        fields = ("id", "name")


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "name")


class TaskWithStatusSerializer(serializers.ModelSerializer):
    status = StatusSerializer(read_only=True)
    status_id = serializers.IntegerField(label=_("Status"), write_only=True, required=False)

    class Meta(TaskSerializer.Meta):
        model = Task
        fields = ("id", "name", "status", "status_id")

    def validate_status_id(self, value):
        try:
            Status.objects.get(id=value)
        except Status.DoesNotExist:
            raise serializers.ValidationError(_("Status not found"))
        return value

    def update(self, instance, validated_data):
        if validated_data['status_id'] != instance.status.id:
            instance.status = Status.objects.get(id=validated_data['status_id'])
        return super(TaskWithStatusSerializer, self).update(instance, validated_data)


class BoardSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='get_name_display')
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Status
        fields = ("id", "name", "tasks")
