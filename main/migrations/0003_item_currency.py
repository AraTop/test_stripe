# Generated by Django 5.0.2 on 2024-03-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.CharField(default='usd', max_length=50, verbose_name='Валюта'),
            preserve_default=False,
        ),
    ]
