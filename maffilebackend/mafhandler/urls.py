from mafhandler.api.uploadmaffile import maffile
from django.urls import path


urlpatterns = [
    path('maffileupload/', maffile.as_view(), name='maffile')
    ]