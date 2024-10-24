# Generated by Django 3.2.15 on 2023-03-02 11:52

from django.db import migrations, models
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0034_alter_article_copyright'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='audio_publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='article',
            name='audio_summary',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='audio summary'),
        ),
    ]
