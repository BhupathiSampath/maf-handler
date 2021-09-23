from mafhandler.models import MafFile
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from authentication.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication



class editmaffileserializer(serializers.ModelSerializer):
    # Total_sequenced                 = serializers.IntegerField()
    # Sequenced_last_week             = serializers.IntegerField()
    # Uploaded_IGIB_SFTP              = serializers.IntegerField()
    # Uploaded_NIBMG_DataHub          = serializers.IntegerField()
    # Uploaded_GISAID                 = serializers.IntegerField()
    # Any_collaboration               = serializers.CharField(required=False)
    class Meta:
        model = MafFile
        fields = ["id","username","maf_file",]
    def validate(self, attrs):
        data = self.get_initial()
        maf_file = data.get('maf_file')
        username = data.get('username')
        if username is None:
            raise serializers.ValidationError({"message":"username is required field"})
        if maf_file is None:
            raise serializers.ValidationError({"message":"maf_file is required"})
        return super().validate(attrs)

class editmaffile(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def post(self,request,pk):
        data = MafFile.objects.get(id=pk)
        serializer = editmaffileserializer(data=request.data,instance=data)
        # print(request.successful_authenticator)
        # print(dir(request.user.is_prouser))
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Successfully updated"})
        # return Response({"message":"Please enter required fields"})
        return Response({"message": serializer.errors})