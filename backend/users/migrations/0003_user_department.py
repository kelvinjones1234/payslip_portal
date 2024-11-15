# Generated by Django 5.1.3 on 2024-11-11 14:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0002_alter_department_name'),
        ('users', '0002_remove_user_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='department',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='departments.department'),
            preserve_default=False,
        ),
    ]
