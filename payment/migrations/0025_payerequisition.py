# Generated by Django 3.0.14 on 2021-04-13 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsroom', '0022_auto_20210326_1533'),
        ('payment', '0024_commission_vat_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='PayeRequisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('payee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsroom.Author')),
            ],
        ),
    ]