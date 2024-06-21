from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255)
    user_password = models.CharField(max_length=255)

    def __str__(self):
        return self.user_name

class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=255)
    admin_password = models.CharField(max_length=255)
    report_id = models.IntegerField()  # Assuming this is intended to link to a Report model

    def __str__(self):
        return self.admin_name

from django.db import models

class Visitor(models.Model):
    name = models.CharField(max_length=100, default='Unknown')
    phone_number = models.CharField(max_length=15, blank=True, default='')
    email = models.EmailField(max_length=255, blank=True, default='')

    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name
