# Generated by Django 3.0.2 on 2020-02-11 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0005_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='index',
            name='Title',
        ),
    ]
