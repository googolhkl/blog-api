import os
from django.db import models
from django.conf import settings
from django.db import models

class PrivateInformation(models.Model):
    photo = models.ImageField(upload_to='photo/', null=True, blank=True)
    name = models.CharField(max_length=30, default='') 
    birth = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=30, default='') 
    email = models.EmailField(max_length=100, default='') 

    def __str__(self):
        return self.name

    @property
    def photo_url(self):
        return 'https://' +settings.AWS_S3_HOST + '/' +\
                settings.AWS_STORAGE_BUCKET_NAME+ '/' + str(self.photo)


class Skill(models.Model):
    information = models.ForeignKey(
            PrivateInformation,
            on_delete=models.CASCADE,
            related_name="skills")
    name = models.CharField(max_length=30, default='') 
    proficiency = models.IntegerField(default=0) 
    description = models.CharField(max_length=255, default='') 

    def __str__(self):
        return "{}[{}]".format(self.name, self.proficiency)


class Education(models.Model):
    information = models.ForeignKey(
            PrivateInformation,
            on_delete=models.CASCADE,
            related_name="educations")
    name = models.CharField(max_length=100, default='') 
    department = models.CharField(max_length=100, default='') 
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)
    graduation = models.CharField(max_length=15, default='졸업') 

    def __str__(self):
        return self.name


class Experience(models.Model):
    information = models.ForeignKey(
            PrivateInformation,
            on_delete=models.CASCADE,
            related_name="experiences")
    host = models.CharField(max_length=100, default='') 
    period_start = models.DateField(null=True, blank=True)
    period_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.host


class Project(models.Model):
    education = models.ForeignKey(
            Experience,
            on_delete=models.CASCADE,
            related_name="projects")
    name = models.CharField(max_length=100, default='') 
    role = models.CharField(max_length=100, default='') 
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}[{}]".format(self.name, self.role)


class SelfIntroduction(models.Model):
    information = models.ForeignKey(
            PrivateInformation,
            on_delete=models.CASCADE,
            related_name="self_introductions")
    subject = models.CharField(max_length=100, default='') 
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject


