# Generated by Django 3.1.3 on 2021-10-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0026_remove_application_recruiter'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('message', models.CharField(max_length=250)),
            ],
        ),
    ]