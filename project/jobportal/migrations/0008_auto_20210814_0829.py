# Generated by Django 3.1.3 on 2021-08-14 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0007_auto_20210814_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentuser',
            name='image',
            field=models.ImageField(default='static/images/mickeymouse.png', null=True, upload_to='MEDIA_ROOT/images/'),
        ),
    ]
