# Generated by Django 3.2.3 on 2021-06-09 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='date_joined',
            new_name='start_date',
        ),
        migrations.AddField(
            model_name='customuser',
            name='about',
            field=models.TextField(blank=True, max_length=500, verbose_name='about'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]
