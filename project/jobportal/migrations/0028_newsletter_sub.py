# Generated by Django 3.1.3 on 2021-10-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0027_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='newsletter_sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
            ],
        ),
    ]