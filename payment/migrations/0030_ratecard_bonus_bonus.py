# Generated by Django 3.2.15 on 2023-03-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0029_alter_commission_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='ratecard',
            name='bonus_bonus',
            field=models.FloatField(default=500.0),
        ),
    ]