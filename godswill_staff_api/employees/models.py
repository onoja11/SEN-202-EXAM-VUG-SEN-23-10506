from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Group, Permission


# Create your models here.


class StaffBase(AbstractUser, PermissionsMixin):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    groups = models.ManyToManyField(
        Group,
        related_name='staffbase_set',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='staffbase_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
class Manager(StaffBase):
    department = models.CharField(max_length=50, blank=True, null=True)
    has_company_card = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
    
class Intern(StaffBase):
    department = models.CharField(max_length=50, blank=True, null=True)
    mentor = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True, related_name='intern')
    internship_end = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.position}"
    
    
