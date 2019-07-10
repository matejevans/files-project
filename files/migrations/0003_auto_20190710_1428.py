# Generated by Django 2.2.3 on 2019-07-10 12:28

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0002_file_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
