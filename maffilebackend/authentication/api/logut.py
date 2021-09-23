from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class logoutview(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication
    def post(self, request):
        response = Response()
        response.delete_cookie('c_uid')
        response.data ={
            "message": "Logged out successfully"
        }
        return response