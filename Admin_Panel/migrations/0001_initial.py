# Generated by Django 5.0.1 on 2024-02-03 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('table_number', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('payment_mode', models.CharField(max_length=20)),
                ('payment_status', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(default='Pending', max_length=20)),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('qr_code_url', models.URLField(blank=True, null=True)),
                ('qr_code_image', models.ImageField(blank=True, null=True, upload_to='QR_codes/')),
            ],
        ),
    ]