# Generated by Django 3.2.3 on 2021-06-12 17:40

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('App_Account', '0004_organization_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='org_pic',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], default='default_pic.jpeg', force_format=None, keep_meta=True, null=True, quality=0, size=[294, 313], upload_to='profilePicture'),
        ),
    ]
