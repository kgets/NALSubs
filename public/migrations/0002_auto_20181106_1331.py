# Generated by Django 2.1.3 on 2018-11-06 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
