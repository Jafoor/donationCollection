# Generated by Django 3.2.3 on 2021-06-24 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Account', '0015_organization_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='banned',
            field=models.BooleanField(default=False),
        ),
    ]
