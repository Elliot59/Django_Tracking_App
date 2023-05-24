from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'password', 'username', 'phone')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }}

    def create(self, validated_data):
        hash_password = make_password(validated_data['password'])
        user = UserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            username=validated_data['username'],
            phone=validated_data['phone']
        )
        return user


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class DeviceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceCompany
        fields = '__all__'

class DeviceUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceUsage
        fields = '__all__'
        read_only_fields = ['device_log']


class DeviceLogSerializer(serializers.ModelSerializer):
    device_usage = DeviceUsageSerializer(many=True)

    class Meta:
        model = DeviceLog
        fields = '__all__'

    def create(self, validated_data):
        device_usage_data = validated_data.pop('device_usage')
        device_log = DeviceLog.objects.create(**validated_data)

        for devices in device_usage_data:
            DeviceUsage.objects.create(device_log=device_log, **devices)

        return device_log



# Placeholder Codes Serializers
class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'