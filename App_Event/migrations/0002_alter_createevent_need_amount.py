# Generated by Django 3.2.3 on 2021-06-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createevent',
            name='need_amount',
            field=models.IntegerField(default=100),
        ),
    ]
