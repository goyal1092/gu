# Generated by Django 2.1.12 on 2019-09-24 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]
