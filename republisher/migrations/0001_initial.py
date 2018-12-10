# Generated by Django 2.1.4 on 2018-12-10 16:18

from django.db import migrations, models
import django.db.models.deletion
import republisher.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('newsroom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Republisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('email_addresses', models.CharField(max_length=250, validators=[republisher.models.validate_email_list])),
                ('message', models.TextField(blank=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='RepublisherArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wait_time', models.PositiveIntegerField(default=0, help_text='Minimum number of minutes after publication till sent.')),
                ('note', models.TextField(blank=True, help_text='A note for the republisher specific to this article.')),
                ('status', models.CharField(choices=[('scheduled', 'Scheduled'), ('sent', 'Sent'), ('failed', 'Failed'), ('paused', 'Paused')], default='scheduled', max_length=20)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsroom.Article')),
                ('republisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='republisher.Republisher')),
            ],
            options={
                'ordering': ['article__published', 'republisher'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='republisherarticle',
            unique_together={('article', 'republisher')},
        ),
    ]
