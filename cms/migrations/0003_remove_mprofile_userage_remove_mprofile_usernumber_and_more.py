# Generated by Django 4.2.5 on 2024-01-12 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0002_email_mprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mprofile',
            name='userage',
        ),
        migrations.RemoveField(
            model_name='mprofile',
            name='usernumber',
        ),
        migrations.AlterField(
            model_name='mprofile',
            name='userfile',
            field=models.FileField(upload_to=None),
        ),
    ]
