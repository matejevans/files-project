# Generated by Django 2.2.3 on 2019-07-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20190710_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
