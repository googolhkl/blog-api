import os
from django.db import models
from django.conf import settings

class Photo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField('Portfolio Description', blank=True)
    image = models.ImageField(upload_to='photo/')
    link = models.URLField(max_length=500, blank=True, default='')
    upload_date = models.DateTimeField('Upload Date')
    is_show = models.BooleanField(default=True)
    likes = models.CharField(max_length=255)

    class Meta:
        ordering = ['-upload_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/media/' + str(self.image)

    @property
    def image_url(self):
        return 'https://' +settings.AWS_S3_HOST + '/' +  settings.AWS_STORAGE_BUCKET_NAME+ '/' + str(self.image)

    def delete(self, *args, **kwargs):
        super(Portfolio, self).delete(*args, **kwargs)

        try:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.name))
        except:
            pass
