from django.urls import path, include
from authentication.api.userregistration import registerview
from authentication.api.userlogin import UserLoginView
from authentication.api.userview import userview, editprofile
from authentication.api.logut import logoutview


urlpatterns = [
    path('registration/', registerview.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user/', userview.as_view(), name='user'),
    path('editprofile/<str:pk>/', editprofile.as_view(), name='editprofile'),
    path('logout/', logoutview.as_view(), name='logout'),
]