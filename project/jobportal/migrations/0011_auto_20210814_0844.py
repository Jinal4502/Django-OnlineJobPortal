# Generated by Django 3.1.3 on 2021-08-14 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0010_auto_20210814_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recruiter',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
