# Generated by Django 3.1.3 on 2021-10-09 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0019_jobmodel_joining_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobmodel',
            old_name='recuiter',
            new_name='recruiter',
        ),
    ]
