from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Company, Device ,User
from .serializers import CompanySerializer, DeviceSerializer, UserSerializer
from django.shortcuts import get_object_or_404

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

    @action(detail=True, methods=['post'])
    def delegate(self, request, pk=None):
        device = self.get_object()
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            device.assigned_employee = serializer.validated_data['assigned_employee']
            device.start_date = serializer
            device.end_date = serializer.validated_data['end_date']
            device.status = 'delegated'
            device.save()
            return Response(DeviceSerializer(device).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def revoke(self, request, pk=None):
        device = self.get_object()
        device.assigned_employee = None
        device.start_date = None
        device.end_date = None
        device.status = 'available'
        device.save()
        return Response(DeviceSerializer(device).data)

    @action(detail=True, methods=['post'])
    def checkout(self, request, pk=None):
        device = self.get_object()
        device.checked_out = True
        device.condition_at_checkout = request.data.get('condition')
        device.save()
        return Response(DeviceSerializer(device).data)

    @action(detail=True, methods=['post'])
    def checkin(self, request, pk=None):
        device = self.get_object()
        device.checked_out = False
        device.condition_at_return = request.data.get('condition')
        device.save()
        return Response(DeviceSerializer(device).data)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



    def checkin_device(request, pk):
        device = get_object_or_404(Device, pk=pk)
        device.status = 'available'
        device.checked_out = False
        device.condition_at_return = request.data.get('condition_at_return') or "N/A"
        device.save()
        return Response(status=status.HTTP_200_OK)


