from django.urls import path
from blog.views import Blog_view_list
urlpatterns = [
    path('', Blog_view_list, name="home")
]
