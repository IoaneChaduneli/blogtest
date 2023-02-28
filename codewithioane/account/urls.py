from django.urls import path
from account.views import user_register_view, logout_view, login_view, account_update_view

app_name = 'account'
urlpatterns = [
    path('register/', user_register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
    path('account/', account_update_view, name='account')
    
]
