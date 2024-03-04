# Generated by Django 5.0.2 on 2024-03-02 13:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateField(verbose_name='Дата оплаты')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Сумма оплаты')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.item', verbose_name='Оплаченный item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Платеж',
                'verbose_name_plural': 'Платежы',
                'ordering': ('user',),
            },
        ),
    ]
