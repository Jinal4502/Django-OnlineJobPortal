# Generated by Django 3.1.3 on 2021-08-13 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0004_recruiter_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
