# Generated by Django 5.1.3 on 2024-11-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(choices=[('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.'), ('Dr.', 'Dr.'), ('Prof', 'Prof')], max_length=10),
        ),
    ]