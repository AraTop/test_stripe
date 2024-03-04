from django.http import HttpResponseServerError
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Item, Basket, Payment
from project import settings
from django.views.generic import ListView, DetailView, CreateView, UpdateView
import stripe
import datetime


class MainListView(ListView):
    model = Item
    template_name = 'main/main.html'


@method_decorator(login_required, name='dispatch')
class PaymentRetrieveView(View):
    template_name = 'main/retrieve_payment.html'

    def get(self, request, payment_intent_id):
        try:
            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            payment_info = {
                "id": payment_intent.id,
                "amount": payment_intent.amount,
                "currency": payment_intent.currency,
            }
            return render(request, self.template_name, {'payment_info': payment_info})
        except stripe.error.StripeError as e:
            print(f"Ошибка Stripe: {e}")
            return HttpResponseServerError("Ошибка Stripe")


@method_decorator(login_required, name='dispatch')
class PaymentCreateView(View):
    template_name = 'main/create_payment.html'

    def get(self, request, item_pk):
        item = Item.objects.filter(id=item_pk).first()
        return render(request, self.template_name, {'item': item})

    def post(self, request, item_pk):
        item = Item.objects.filter(id=item_pk).first()
        amount = item.price * 100 # $10.00
        currency = item.currency

        stripe.api_key = settings.STRIPE_SECRET_KEY
        payment_intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        )
        payment_intent_id = payment_intent.id
        payment = Payment(
        user=request.user,
        payment_date=datetime.date.today(),
        item=item,
        amount=amount
        )
        payment.save()

        # После обработки формы выполняем редирект на страницу с информацией о платеже
        return redirect('main:ret', payment_intent_id=payment_intent_id)

@login_required
def add_basket(request, item_id):
    item = Item.objects.get(pk=item_id)
    basket = Basket.objects.get_or_create(
    user=request.user,
    item=item
    )
    return redirect('main:main')

def baskets(request):
    user = request.user
    total_amount = 0
    baskets = Basket.objects.filter(user=user).all()
    for basket in baskets:
        if basket.item.currency == 'USD':  
            total_amount += basket.item.price
        else:
            if basket.item.currency == 'AUD':
                sum_ = basket.item.price
                total_amount += sum_ * 0.7

            elif basket.item.currency == 'NZD':
                sum_ = basket.item.price
                total_amount += sum_ * 0.61

            elif basket.item.currency == 'SGD':
                sum_ = basket.item.price
                total_amount += sum_ * 0.8

            elif basket.item.currency == 'RON':
                sum_ = basket.item.price
                total_amount += sum_ * 0.3

            elif basket.item.currency == 'CAD':
                sum_ = basket.item.price
                total_amount += sum_ * 0.8
    
    return render(request, 'main/baskets.html', {'baskets': baskets, 'total_amount': total_amount})


@method_decorator(login_required, name='dispatch')
class BasketCreateView(View):
    template_name = 'main/create_basket.html'

    def get(self, request):
        user = request.user
        baskets = Basket.objects.filter(user=user).all()
        return render(request, self.template_name, {'items': baskets})

    def post(self, request):
        user = request.user
        baskets = Basket.objects.filter(user=user).all()
        total_amount = 0

        for basket in baskets:
            if basket.item.currency == 'USD':  
                total_amount += basket.item.price
            else:
                if basket.item.currency == 'AUD':
                    sum_ = basket.item.price
                    total_amount += sum_ * 0.7

                elif basket.item.currency == 'NZD':
                    sum_ = basket.item.price
                    total_amount += sum_ * 0.61

                elif basket.item.currency == 'SGD':
                    sum_ = basket.item.price
                    total_amount += sum_ * 0.8

                elif basket.item.currency == 'RON':
                    sum_ = basket.item.price
                    total_amount += sum_ * 0.3

                elif basket.item.currency == 'CAD':
                    sum_ = basket.item.price
                    total_amount += sum_ * 0.8

            amount = basket.item.price # $10.00

            payment = Payment(
            user=request.user,
            payment_date=datetime.date.today(),
            item=basket.item,
            amount=amount
            )
            payment.save()

        stripe.api_key = settings.STRIPE_SECRET_KEY
        payment_intent = stripe.PaymentIntent.create(
            amount=int(total_amount * 100),
            currency='usd',
        )
        payment_intent_id = payment_intent.id
        baskets.delete()
        return redirect('main:ret', payment_intent_id=payment_intent_id)
