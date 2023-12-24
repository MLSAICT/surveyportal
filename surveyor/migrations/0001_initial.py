# Generated by Django 4.2.4 on 2023-11-09 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Surveyor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_number', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PSMRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('island', models.CharField(max_length=255)),
                ('request_letter', models.FileField(upload_to='psm_requests/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('surveyor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveyor.surveyor')),
            ],
        ),
        migrations.CreateModel(
            name='CSRRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('excel_data', models.FileField(upload_to='csr_requests/excel/')),
                ('raw_data', models.FileField(upload_to='csr_requests/raw_data/')),
                ('survey_report', models.FileField(upload_to='csr_requests/reports/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('psm_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveyor.psmrequest')),
                ('surveyor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='surveyor.surveyor')),
            ],
        ),
    ]