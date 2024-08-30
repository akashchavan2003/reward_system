from rest_framework import serializers
from admin_app.models import App

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
