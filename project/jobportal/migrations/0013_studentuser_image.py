# Generated by Django 3.1.3 on 2021-09-28 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0012_remove_studentuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]