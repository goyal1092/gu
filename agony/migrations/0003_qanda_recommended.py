# Generated by Django 2.1.12 on 2019-09-24 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agony', '0002_auto_20190108_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='qanda',
            name='recommended',
            field=models.BooleanField(default=True),
        ),
    ]
