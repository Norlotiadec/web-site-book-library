from django.urls import path
from .views import home, profile, BookLoginView, BookLogoutView, ChangeUserInfoView, BookChangePasswordView, \
    RegisterUserView, RegisterDone, BookDeleteView

app_name = 'library'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/login/', BookLoginView.as_view(), name='login'),
    path('accounts/logout/', BookLogoutView.as_view(), name='logout'),
    path('accounts/profile/', profile, name='profile'),
    path('accounts/profile/change/', ChangeUserInfoView.as_view(), name='change_info'),
    path('accounts/password/change/', BookChangePasswordView.as_view(), name='change_password'),
    path('accounts/register/done/', RegisterDone.as_view(), name='register_done'),
    path('accounts/register/', RegisterUserView.as_view(), name='register_user'),
    path('account/profile/delete/', BookDeleteView.as_view(), name='delete_user'),
]