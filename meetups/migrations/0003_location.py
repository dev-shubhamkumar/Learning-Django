# Generated by Django 3.2.4 on 2021-06-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_meetup_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
    ]
