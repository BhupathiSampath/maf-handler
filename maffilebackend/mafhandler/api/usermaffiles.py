from mafhandler.models import MafFile
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from authentication.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
# from users.auth import JSONWebTokenAuthentication
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.db.models.aggregates import Max
from rest_framework import serializers, status


class userfilesserializer(serializers.ModelSerializer):
    class Meta:
        model = MafFile
        fields = '__all__'

        
class usermaffiles(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def get(self, request):
        if request.user is None:
            return Response("SSS")
        data = MafFile.objects.filter(username=request.user)
        # response = json.dump(data)
        print(request.user)
        serializer = userfilesserializer(data, many =True)
        return Response({"data":serializer.data})
