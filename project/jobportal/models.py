from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class StudentUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, null=True)
    image = models.ImageField(null=True)
    user_type = models.CharField(max_length=15, null=True)
    def _str_(self):
        return self.user.username  

class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10, null=True)
    image = models.ImageField(null=True)
    company = models.CharField(max_length=100, null=True)
    user_type = models.CharField(max_length=15, null=True)
    status = models.CharField(max_length=15, null=True)
    def _str_(self):
        return self.user.username