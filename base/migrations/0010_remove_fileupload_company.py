# Generated by Django 4.2.2 on 2023-07-23 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_user_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='company',
        ),
    ]
