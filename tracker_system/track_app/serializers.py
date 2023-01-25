from rest_framework import serializers
from .models import Company, Device,User

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'employees')

class DeviceSerializer(serializers.ModelSerializer):
    assigned_employee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Device
        fields = ('id', 'name', 'serial_number', 'model', 'company', 'assigned_employee', 'start_date', 'end_date', 'status', 'checked_out', 'condition_at_checkout', 'condition_at_return')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'companies', 'devices')
