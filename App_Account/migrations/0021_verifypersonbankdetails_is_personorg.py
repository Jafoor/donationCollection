# Generated by Django 3.2.3 on 2021-06-30 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Account', '0020_verifypersonbankdetails_filled'),
    ]

    operations = [
        migrations.AddField(
            model_name='verifypersonbankdetails',
            name='is_personorg',
            field=models.BooleanField(default=False),
        ),
    ]
