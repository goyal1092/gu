# Generated by Django 3.2.15 on 2022-10-04 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('republisher', '0003_republisherarticle_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='republisher',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]