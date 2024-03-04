from django.urls import path
from main import views
from .apps import MainConfig

app_name = MainConfig.name


urlpatterns = [
   path('', views.MainListView.as_view(), name='main'),
   path('item/<int:item_pk>/', views.PaymentCreateView.as_view(), name='create_payment'),
   path('items/', views.BasketCreateView.as_view(), name='create_basket'),
   path('buy/<str:payment_intent_id>/', views.PaymentRetrieveView.as_view(), name='ret'),
   path('add-to-cart/<int:item_id>/', views.add_basket, name='add_basket'),
   path('baskets/', views.baskets, name='baskets'),
]