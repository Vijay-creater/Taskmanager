from task.models import *
from rest_framework import serializers

class PostTankSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields = ['title','description','due_date']

class GetTankSerializer(serializers.ModelSerializer):
    Status_name = serializers.StringRelatedField(source='status.Status_name')
    due_date = serializers.DateField(format='%d-%m-%Y')
    class Meta:
        model= Task
        fields = ['id','title','description','due_date','status','Status_name']

class GetTankUnitSerializer(serializers.ModelSerializer):
    Status_name = serializers.StringRelatedField(source='status.Status_name')
    class Meta:
        model= Task
        fields = ['id','title','description','due_date','status','Status_name']

class GetStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ['id','Status_name']