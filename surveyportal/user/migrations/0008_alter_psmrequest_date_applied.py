# Generated by Django 4.2.2 on 2023-09-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_psmrequest_date_applied'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psmrequest',
            name='date_applied',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
