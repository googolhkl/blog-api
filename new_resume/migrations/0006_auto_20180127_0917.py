# Generated by Django 2.0.1 on 2018-01-27 09:17

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_resume', '0005_privateinformation_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selfintroduction',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='contents'),
        ),
    ]
