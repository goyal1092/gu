# Generated by Django 4.2.7 on 2024-10-15 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('donationPage', '0008_auto_20230802_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('one_time', 'One Time'), ('subscription', 'Subscription')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='platform',
            field=models.CharField(blank=True, choices=[('paypal', 'Paypal'), ('snapscan', 'Snapscan'), ('payfast', 'Payfast')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='status',
            field=models.CharField(blank=True, choices=[('success', 'Success'), ('failed', 'Failed'), ('pending', 'Pending')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='donation',
            name='transaction_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_id', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('cancelled', 'Cancelled')], max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('failed_payments', models.PositiveIntegerField(default=0)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='donationPage.donor')),
            ],
        ),
    ]
