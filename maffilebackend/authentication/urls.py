from django.urls import path, include
from authentication.api.userregistration import registerview
from authentication.api.userlogin import UserLoginView
from authentication.api.userview import userview


urlpatterns = [
    path('registration/', registerview.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user/', userview.as_view(), name='user'),
]