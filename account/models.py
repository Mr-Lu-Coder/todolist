from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True)
    email = models.CharField(unique=True, max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    head_image = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.name


class UserGroup(models.Model):
    group_name = models.CharField(unique=True, max_length=255, blank=True)
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.group_name