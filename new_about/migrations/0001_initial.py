# Generated by Django 2.0.1 on 2018-01-17 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, verbose_name='Portfolio Description')),
                ('image', models.ImageField(upload_to='photo/')),
                ('link', models.URLField(blank=True, default='', max_length=500)),
                ('upload_date', models.DateTimeField(verbose_name='Upload Date')),
                ('is_show', models.BooleanField(default=True)),
                ('likes', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-upload_date'],
            },
        ),
    ]
