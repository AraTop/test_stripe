from django.urls import path
from users import views
from .views import LoginView, LogoutView
from users.apps import UsersConfig


app_name = UsersConfig.name

urlpatterns = [
   path('login/', LoginView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
   path('register/', views.RegisterView.as_view(), name='register'),
   path('profile/', views.ProfileView.as_view(), name='profile'),
]
