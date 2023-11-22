from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from rest_framework.response import Response
from botocore.exceptions import ClientError

class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer
    
    def list(self, request):
        users = User.getAllUsers()
        if users:
            return Response(users);
        return Response({"Error": "Error fetching user"}, status=400)

    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            response  = User.createUser(user_data)
            if(response):
                return response;
            return Response({"Message": "Successfull"}, status=201)
        return Response(serializer.errors, status=400)
    
    def destroy(self, request, pk=None):
        if pk:
            try:
                User.deleteUser(pk)
                return Response({"Message": "User successfully deleted"}, status=201)
            except ClientError as e:
                return Response({"Error": "e"}, status=400)
        
    def update(self, request, pk=None):
        data = request.data
        if pk and data:
            try:
                User.updateUser(pk, data);
                return Response({"Message": "User successfully updated"}, status=201)
            except ClientError as e:
                return Response({"Error": "e"}, status=400)