# Generated by Django 4.2.2 on 2023-07-22 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_department_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='base.company'),
        ),
    ]
