# Generated by Django 4.1 on 2022-08-15 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('price', models.IntegerField(max_length=20)),
                ('description', models.CharField(max_length=1000)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
