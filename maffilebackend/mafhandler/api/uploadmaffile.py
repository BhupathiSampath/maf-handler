from genericpath import exists
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from mafhandler.models import *
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import os

class maffileserializer(serializers.ModelSerializer):
    def doesFileExists(filePathAndName):
        return os.path.exists(filePathAndName)
    
    class Meta:
        model = MafFile
        fields = ["id","username","maf_file",]
    

    
    def validate(self, attrs):
        data = self.get_initial()
        maf_file = data.get('maf_file')
        username = data.get('username')
        if username is None:
            raise serializers.ValidationError({"message":"username is required field"})
        if maffile is None:
            raise serializers.ValidationError({"message":"maf_file is required field"})
        if MafFile.objects.filter(maf_file=maf_file).exists():
            raise serializers.ValidationError({"message":"file already existed"})
        return super().validate(attrs)
class maffile(APIView):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def post(self,request):
        serializer = maffileserializer(data =request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # return Response({"message":"Please enter required fields"})
        return Response({'message': serializer.errors})