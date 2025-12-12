from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Menu, Booking


# Serializer for your Menu model
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'


# Serializer for your Booking model
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


# Serializer for built-in Django User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']
