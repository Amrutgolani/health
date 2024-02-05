# Generated by Django 4.2.5 on 2024-01-16 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_remove_mprofile_userage_remove_mprofile_usernumber_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mprofile',
            name='userfile',
        ),
        migrations.AddField(
            model_name='mprofile',
            name='userage',
            field=models.IntegerField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='mprofile',
            name='usernumber',
            field=models.IntegerField(max_length=20, null=True),
        ),
    ]
