# Generated by Django 3.1 on 2020-09-26 05:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_tintuc_ngaygio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tintuc',
            name='image',
        ),
        migrations.AddField(
            model_name='tintuc',
            name='created',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
