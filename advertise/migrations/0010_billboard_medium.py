# Generated by Django 3.0.5 on 2020-07-08 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0009_auto_20200708_1805'),
    ]

    operations = [
        migrations.AddField(
            model_name='billboard',
            name='Medium',
            field=models.CharField(default='Print Medium', max_length=60),
        ),
    ]