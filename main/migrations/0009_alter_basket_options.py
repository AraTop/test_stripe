# Generated by Django 5.0.2 on 2024-03-03 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_order_basket'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'ordering': ('item',), 'verbose_name': 'корзины', 'verbose_name_plural': 'корзине'},
        ),
    ]
