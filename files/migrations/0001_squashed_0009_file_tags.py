# Generated by Django 2.2.3 on 2019-07-16 21:58

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    replaces = [('files', '0001_initial'), ('files', '0002_file_tags'), ('files', '0003_auto_20190710_1428'), ('files', '0004_auto_20190710_1436'), ('files', '0005_auto_20190710_1442'), ('files', '0006_auto_20190710_1450'), ('files', '0007_auto_20190710_1451'), ('files', '0008_remove_file_tags'), ('files', '0009_file_tags')]

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('public', models.BooleanField(default=False)),
                ('file', models.FileField(upload_to='')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
