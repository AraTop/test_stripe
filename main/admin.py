from django.contrib import admin
from .models import Item, Basket, Payment


@admin.register(Item)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'description', 'price', 'currency')


@admin.register(Payment)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('user', 'payment_date', 'item', 'amount')


@admin.register(Basket)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('user', 'item')
