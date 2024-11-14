# Generated by Django 5.1.3 on 2024-11-11 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_user_department'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='full_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='ippis_number',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
