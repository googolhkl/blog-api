# Generated by Django 2.0.1 on 2018-01-17 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_resume', '0004_auto_20180116_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='privateinformation',
            name='home',
            field=models.CharField(default='', max_length=100),
        ),
    ]