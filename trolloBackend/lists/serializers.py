from rest_framework import serializers

class ListSerializer(serializers.Serializer):
    list_id = serializers.CharField()
    created_by = serializers.CharField()
    list_name = serializers.CharField()