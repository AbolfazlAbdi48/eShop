# Generated by Django 4.0 on 2022-01-04 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0002_alter_product_created_alter_product_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='نام کامل')),
                ('city', models.CharField(max_length=100, verbose_name='شهر')),
                ('full_address', models.CharField(max_length=100, verbose_name='آدرس کامل')),
                ('code_postal', models.BigIntegerField(verbose_name='کدپستی')),
                ('phone_number', models.CharField(max_length=12, verbose_name='شماره تلفن')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='مشتری')),
            ],
            options={
                'verbose_name': 'آدرس',
                'verbose_name_plural': 'آدرس ها',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_sent', models.BooleanField(default=False, verbose_name='ارسال شده / نشده')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.address', verbose_name='آدرس ارسال')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer', verbose_name='مشتری')),
            ],
            options={
                'verbose_name': 'سبد خرید',
                'verbose_name_plural': 'سبد های خرید',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='نام و نام خانوادگی')),
                ('amount', models.IntegerField(verbose_name='مبلغ')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='شماره موبایل')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='توضیحات')),
                ('trans_id', models.IntegerField(verbose_name='شماره فاکتور')),
                ('status', models.BooleanField(default=False, verbose_name='وضعیت')),
                ('card_number', models.CharField(blank=True, max_length=18, null=True, verbose_name='شماره کارت')),
                ('trace_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='شماره پیگیری')),
                ('message', models.TextField(blank=True, null=True, verbose_name='پیام')),
                ('insert_date_time', models.DateTimeField(auto_now_add=True, verbose_name='زمان ایجاد')),
                ('payment_date_time', models.DateTimeField(auto_now=True, verbose_name='زمان پرداخت')),
            ],
            options={
                'verbose_name': 'پرداخت',
                'verbose_name_plural': 'پرداخت ها',
            },
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='قیمت محصول در زمان خرید')),
                ('count', models.IntegerField(default=1, verbose_name='تعداد سفارش')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order', verbose_name='محصول در سبد')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'جزئیات سبد خرید',
                'verbose_name_plural': 'جزئیات سبد های خرید',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.payment', verbose_name='اطلاعات پرداخت'),
        ),
    ]