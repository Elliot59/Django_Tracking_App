from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,
                                        BaseUserManager,
                                        PermissionsMixin)
from rest_framework.permissions import AllowAny


# USER CREATION OF USER AND SUPERUSER
class UserProfileManager(BaseUserManager):
    def create_user(self, email, phone, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have email')
        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('username', 'admin')
        return self.create_user(email, phone, password, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    def __str__(self):
        return self.email


class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class DeviceCompany(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    hand_over_date = models.DateTimeField(auto_now_add=True)
    condition_when_handed_over = models.CharField(max_length=100)
    return_date = models.DateTimeField(null=True, blank=True)
    condition_when_returned = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.employee.name)


class DeviceUsage(models.Model):
    name = models.CharField(max_length=100)
    device_company = models.ForeignKey(DeviceCompany, on_delete=models.CASCADE)
    device_log = models.ForeignKey(DeviceLog, on_delete=models.CASCADE, related_name='device_usage')

    def __str__(self):
        return self.device_log.employee.name



#Some Placeholder codes for subscription and  payment
class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField()

class Payment(models.Model):
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)