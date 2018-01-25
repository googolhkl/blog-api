import os
from django.db import models
from django.conf import settings
from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
	name = models.CharField(max_length=50, blank=False, null=False, unique=True)
	description = models.CharField(max_length=100, blank=True ) # 
	created_date = models.DateTimeField(default=timezone.now) # 작성 날짜

	class Meta:
		ordering = ['created_date']

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=50, blank=True, null=False, unique=True)

	class Meta:
		ordering = ['name']

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return settings.SITE_URL + "/blog/tags/%s" % self.name


class Post(models.Model):
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)
	title = models.CharField(max_length=200, default='') 
	content = RichTextUploadingField('contents')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
	is_subscription = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return settings.SITE_URL + "/blog/posts/%i" % self.id
