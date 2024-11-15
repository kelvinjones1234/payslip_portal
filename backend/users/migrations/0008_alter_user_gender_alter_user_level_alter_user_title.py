# Generated by Django 5.1.3 on 2024-11-13 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.CharField(blank=True, choices=[('Level 1', 'Level 1'), ('Level 2', 'Level 2'), ('Level 3', 'Level 3'), ('Level 4', 'Level 4'), ('Level 5', 'Level 5'), ('Level 6', 'Level 6'), ('Level 7', 'Level 7'), ('Level 8', 'Level 8'), ('Level 9', 'Level 9'), ('Level 10', 'Level 10'), ('Level 11', 'Level 11'), ('Level 12', 'Level 12'), ('Level 13', 'Level 13'), ('Level 14', 'Level 14'), ('Level 15', 'Level 15'), ('Level 16', 'Level 16'), ('Level 17', 'Level 17')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='title',
            field=models.CharField(choices=[('Ms.', 'Ms.'), ('Mrs.', 'Mrs.'), ('Mr.', 'Mr.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof.')], max_length=10),
        ),
    ]
