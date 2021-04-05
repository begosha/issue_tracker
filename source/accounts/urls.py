from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from accounts.views import login_view, logout_view

urlpatterns = [
    path('accounts/login/', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout')
]