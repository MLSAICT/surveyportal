# Generated by Django 4.2.4 on 2023-11-10 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surveyor', '0004_alter_surveyor_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyor',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
