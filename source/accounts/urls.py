from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from accounts.views import  RegisterView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/create/', RegisterView.as_view(), name='create')
]