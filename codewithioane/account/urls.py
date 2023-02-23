from django.urls import path
from account.views import user_register_view, logout_view

app_name = 'account'
urlpatterns = [
    path('register/', user_register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    
]
