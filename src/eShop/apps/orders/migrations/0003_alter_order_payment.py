# Generated by Django 4.0 on 2022-01-04 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_alter_address_full_address_alter_order_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.payment', verbose_name='اطلاعات پرداخت'),
        ),
    ]
