from django.test import TestCase
from django.contrib.auth.models import User
from .models import Company, Device

class DeviceTestCase(TestCase):
    def setUp(self):
        # create a test user
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.user.save()

        # create a test company
        self.company = Company.objects.create(name='Test Company')
        self.company.save()
        self.company.employees.add(self.user)

        # create a test device
        self.device = Device.objects.create(
            name='Test Device',
            serial_number='123456',
            model='Test Model',
            company=self.company,
            assigned_employee=self.user,
            start_date='2022-01-01',
            end_date='2022-12-31',
            status='available',
            checked_out=False,
            condition_at_checkout='Good',
            condition_at_return='Good'
        )
        self.device.save()

    def test_device_creation(self):
        device = Device.objects.get(name='Test Device')
        self.assertEqual(device.serial_number, '123456')
        self.assertEqual(device.model, 'Test Model')
        self.assertEqual(device.assigned_employee, self.user)
        self.assertEqual(device.company, self.company)
        self.assertEqual(device.status, 'available')
        self.assertEqual(device.checked_out, False)
        self.assertEqual(device.condition_at_checkout, 'Good')
        self.assertEqual(device.condition_at_return, 'Good')

    def test_device_assignment(self):
        # assign the device to a different user
        user2 = User.objects.create_user(username='testuser2', password='testpass2')
        user2.save()
        self.device.assigned_employee = user2
        self.device.save()

        # check that the device has been assigned to the new user
        device = Device.objects.get(name='Test Device')
        self.assertEqual(device.assigned_employee, user2)
        self.assertNotEqual(device.assigned_employee, self.user)

    def test_device_status_change(self):
        # check out the device
        self.device.status = 'checked_out'
        self.device.checked_out = True
        self.device.save()
