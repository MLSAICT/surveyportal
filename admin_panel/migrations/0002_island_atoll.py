# Generated by Django 4.2.4 on 2023-11-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='island',
            name='atoll',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
