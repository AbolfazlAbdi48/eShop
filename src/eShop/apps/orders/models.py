from django.db import models
from eShop.apps.customers.models import Customer
from eShop.apps.products.models import Product


# Create your models here.


class Payment(models.Model):
    full_name = models.CharField(
        verbose_name="نام و نام خانوادگی", max_length=255, blank=True, null=True
    )
    amount = models.IntegerField(
        verbose_name="مبلغ"
    )
    mobile = models.CharField(
        verbose_name="شماره موبایل", max_length=11, blank=True, null=True
    )
    description = models.CharField(
        verbose_name="توضیحات", max_length=255, blank=True, null=True
    )
    trans_id = models.IntegerField(
        verbose_name="شماره فاکتور"
    )
    status = models.BooleanField(
        verbose_name="وضعیت", default=False
    )
    card_number = models.CharField(
        verbose_name="شماره کارت", max_length=18, blank=True, null=True
    )
    trace_number = models.CharField(
        verbose_name="شماره پیگیری", max_length=255, blank=True, null=True
    )
    message = models.TextField(
        verbose_name="پیام", blank=True, null=True
    )
    insert_date_time = models.DateTimeField(
        auto_now_add=True, verbose_name="زمان ایجاد"
    )
    payment_date_time = models.DateTimeField(
        auto_now=True, verbose_name="زمان پرداخت"
    )

    class Meta:
        verbose_name = 'پرداخت'
        verbose_name_plural = 'پرداخت ها'

    def __str__(self):
        return f"قیمت: {self.amount} | TransID : {self.trans_id}"

    def get_status(self):
        if self.status:
            status = 'پرداخت شده'
        else:
            status = 'پرداخت نشده'
        return status

    get_status.short_description = "وضعیت پرداخت"


class Address(models.Model):
    owner = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='مشتری')
    full_name = models.CharField(max_length=100, verbose_name='نام کامل')
    city = models.CharField(max_length=100, verbose_name='شهر')
    full_address = models.TextField(max_length=100, verbose_name='آدرس کامل')
    code_postal = models.BigIntegerField(verbose_name='کدپستی')
    phone_number = models.CharField(max_length=12, verbose_name='شماره تلفن')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'آدرس'
        verbose_name_plural = 'آدرس ها'

    def __str__(self):
        return f'شهر : {self.city} | کدپستی : {self.code_postal}'


class Order(models.Model):
    owner = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name='owner', verbose_name='مشتری'
    )
    payment = models.ForeignKey(
        Payment, on_delete=models.CASCADE, blank=True, null=True, related_name='payment', verbose_name='اطلاعات پرداخت'
    )
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, related_name='address', verbose_name='آدرس ارسال'
    )
    is_sent = models.BooleanField(default=False, verbose_name='ارسال شده / نشده')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید'

    def __str__(self):
        return f'مشتری : {self.owner.email}'


class OrderDetail(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order', verbose_name='محصول برای سبد خرید'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='product', verbose_name='محصول'
    )
    price = models.IntegerField(verbose_name='قیمت محصول در زمان خرید')
    count = models.IntegerField(default=1, verbose_name='تعداد سفارش')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'جزئیات سبد خرید'
        verbose_name_plural = 'جزئیات سبد های خرید'

    def __str__(self):
        return f'سبد خرید : {self.order.owner.email} | محصول : {self.product.title}'

    def get_sum_price(self):
        return f'{self.price * self.count} تومان '

    get_sum_price.short_description = "جمع قیمت"
