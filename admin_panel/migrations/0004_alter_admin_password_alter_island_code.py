# Generated by Django 5.0.1 on 2024-01-21 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_alter_admin_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='island',
            name='code',
            field=models.CharField(max_length=254, unique=True),
        ),
    ]
