# Generated by Django 3.0.2 on 2020-02-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_auto_20200216_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='card2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title2', models.CharField(max_length=50)),
                ('Description12', models.CharField(max_length=50)),
                ('Description22', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='card3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title2', models.CharField(max_length=50)),
                ('Description13', models.CharField(max_length=50)),
                ('Description23', models.CharField(max_length=50)),
            ],
        ),
    ]