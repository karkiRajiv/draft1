# Generated by Django 3.0.2 on 2020-02-11 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0004_delete_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Title', models.CharField(max_length=100)),
                ('Description', models.TextField()),
            ],
        ),
    ]