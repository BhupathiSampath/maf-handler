from mafhandler.api.uploadmaffile import maffile
from mafhandler.api.usermaffiles import usermaffiles
from mafhandler.api.editmaffile import editmaffile
from django.urls import path


urlpatterns = [
    path('maffileupload/', maffile.as_view(), name='maffile'),
    path('usermaffiles/', usermaffiles.as_view(), name='usermaffiles'),
    path('editfile/<str:pk>/', editmaffile.as_view(), name='editfile'),
    ]

    