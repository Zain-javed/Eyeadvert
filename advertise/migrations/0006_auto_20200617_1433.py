# Generated by Django 3.0.5 on 2020-06-17 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advertise', '0005_auto_20200617_1431'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billboard',
            old_name='facelink',
            new_name='facebook',
        ),
        migrations.RenameField(
            model_name='billboard',
            old_name='instalink',
            new_name='insta',
        ),
    ]
