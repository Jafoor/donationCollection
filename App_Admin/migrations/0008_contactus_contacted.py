# Generated by Django 3.2.3 on 2021-07-01 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Admin', '0007_auto_20210701_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='contacted',
            field=models.BooleanField(default=True),
        ),
    ]