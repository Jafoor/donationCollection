# Generated by Django 3.2.3 on 2021-06-26 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Event', '0009_auto_20210626_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='withdraw',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
