
import uuid

from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone

from .managers import CustomUserManager




# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=100, unique=True)
    date_of_registarion = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=100)
    contact_person = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.name
    
    class Meta:
        db_table = "company"

class User(AbstractBaseUser, PermissionsMixin):

    # Roles created here
    ADMIN = 1
    COMPANY = 2

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (COMPANY, 'company'),
    )
    company = models.ForeignKey(Company, related_name='user', on_delete=models.CASCADE, null=True, blank=True)
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=2)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, related_name='department', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "department"



class Employee(models.Model):
    company = models.ForeignKey(Company, related_name='employees', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    ec_number = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    department = models.ForeignKey(Department, related_name='employees', on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    year_started = models.CharField(max_length=100, blank=True, null=True)
    year_left = models.CharField(max_length=100, blank=True, null=True)

    # def __str__(self):
    #     return self.full_name
    
    class Meta:
        db_table = "employee"

class Roles(models.Model):
    role = models.CharField(max_length=100)
    company_id = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=100)
    date_started = models.CharField(max_length=100, blank=True, null=True)
    date_left = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = "roles"

class Duties(models.Model):
    company_id = models.CharField(max_length=100)
    role_id = models.CharField(max_length=100, blank=True, null=True)
    duty = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.duty
    
    class Meta:
        db_table = "duties"

# Create your models here.
class FileUpload(models.Model):
    FILE_CHOICES = (
        ('departments', 'departments'),
        ('employees', 'employees'),
    )
    type = models.CharField(choices=FILE_CHOICES, blank=True, null=True, default='notset', max_length=100)
    #company = models.ForeignKey(Company, related_name='fileUpload', on_delete=models.CASCADE)
    file = models.FileField(upload_to='csv_uploads/%y/%m')
    created_at = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        db_table = "files"