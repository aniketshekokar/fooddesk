# Generated by Django 5.0.1 on 2024-02-03 09:05

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
                ('description', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Menu_Images/')),
                ('data_of_add', models.DateTimeField(auto_now_add=True)),
                ('order_times', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedOrder',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('table_number', models.IntegerField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
                ('payment_mode', models.CharField(choices=[('Not Yet', 'Not Yet'), ('Cash', 'Cash'), ('Online', 'Online')], default='Not Yet', max_length=20)),
                ('payment_status', models.CharField(choices=[('Pending', 'Pending'), ('Done', 'Done')], default='Pending', max_length=20)),
                ('overall_total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompleteOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='Menu.completedorder')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Menu.menuitems')),
            ],
        ),
        migrations.CreateModel(
            name='YourOrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('order_number', models.CharField(blank=True, max_length=100)),
                ('table_number', models.IntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('order_status', models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], default='Pending', max_length=20)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Menu.yourordermodel')),
            ],
        ),
    ]
