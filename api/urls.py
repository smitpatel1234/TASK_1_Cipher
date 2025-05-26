from django.urls import path
from .views import get_user
from .views import post_type_plain  
urlpatterns = [
    path('get_user/',get_user,name='get_user'),
    path('post_type_plain/', post_type_plain, name='post_type_plain'),
]