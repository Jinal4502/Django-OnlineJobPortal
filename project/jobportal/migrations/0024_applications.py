# Generated by Django 3.1.3 on 2021-10-16 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0023_auto_20211010_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(null=True, upload_to='')),
                ('application_date', models.DateField()),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobportal.jobmodel')),
                ('recruiter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobportal.recruiter')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobportal.studentuser')),
            ],
        ),
    ]
