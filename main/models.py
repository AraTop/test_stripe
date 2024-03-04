from django.db import models
from users.models import User

PAYMENT_METHOD_CHOICES = (
   ('USD', 'Доллар США'),  
   ('AUD', 'Австралийский доллар'),
   ('NZD', 'Новозеландский доллар'),  
   ('SGD', 'Сингапурский доллар'),
   ('RON', 'Румынский лей'),  
   ('CAD', 'Канадский доллар'),
)
NULLABLE = {'null':True, 'blank':True}


class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')
    currency = models.CharField(max_length=50, verbose_name='Валюта', choices=PAYMENT_METHOD_CHOICES)

    def __str__(self):
        return f'{self.name} - {self.price}'
   
    class Meta:
        verbose_name = 'элемент'
        verbose_name_plural = 'элементы'
        ordering = ('name',)


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    payment_date = models.DateField(verbose_name='Дата оплаты')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='Оплаченный item')
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Сумма оплаты')

    def __str__(self):
        return f'{self.user} - {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежы'
        ordering = ('user',)


class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    item = models.ForeignKey(Item, on_delete=models.CASCADE, verbose_name='item')

    def __str__(self):
        return f'{self.user}'

    class Meta:
        verbose_name = 'корзина'
        verbose_name_plural = 'корзины'
        ordering = ('item',)
