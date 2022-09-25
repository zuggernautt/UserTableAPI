from rest_framework import serializers
from .models import  UserTable

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'fullname', 'email', 'mobile', 'created_at',)
        model = UserTable