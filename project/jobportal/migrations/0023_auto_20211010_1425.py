# Generated by Django 3.1.3 on 2021-10-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0022_jobmodel_job_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='job_creation_date',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
