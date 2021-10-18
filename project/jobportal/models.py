from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
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

class JobModel(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    domain = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    skillset = models.CharField(max_length=250, null=True)
    salary = models.FloatField(null=True)
    joining_date = models.DateField(null=True)
    location = models.CharField(max_length=50)
    logo = models.ImageField(null=True)
    description = models.CharField(max_length=250, null=True)
    job_description_file = models.FileField(null=True, validators=[FileExtensionValidator(allowed_extensions=['docx'])])
    job_creation_date = models.CharField(max_length=50, null=True)
    def _str_(self):
        return self.domain

class Application(models.Model):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    student = models.ForeignKey(StudentUser, on_delete=models.CASCADE)
    resume = models.FileField(null=True)
    application_date = models.DateField()
    def _str_(self):
        return self.id

class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.CharField(max_length=250)

class newsletter_sub(models.Model):
    username = models.CharField(max_length=50)
    receipent = models.EmailField(max_length=50)
