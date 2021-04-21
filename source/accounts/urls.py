from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from accounts.views import  RegisterView, UserDetailView, UserListView, UserChangeView, UserPasswordChangeView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/create/', RegisterView.as_view(), name='create'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('accounts/users/', UserListView.as_view(), name='users-list'),
    path('<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('<int:pk>/password_change', UserPasswordChangeView.as_view(), name='password_change')
]