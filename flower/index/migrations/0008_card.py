# Generated by Django 3.0.2 on 2020-02-14 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('index', '0007_delete_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Description1', models.CharField(max_length=50)),
                ('Description2', models.CharField(max_length=50)),
            ],
        ),
    ]
