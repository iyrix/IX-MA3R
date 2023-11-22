from rest_framework import viewsets, status
from .serializers import ListSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from .models import List
# Create your views here.

class ListViewSet(viewsets.ViewSet):
    serializer_class = ListSerializer

    def list(self, request):
        # users = .getAllUsers()
        # if users:
        #     return Response(users);
        return Response({"Error": "Error fetching user"}, status=400)
    
    def create (self, request):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            response  = List.createList(user_data)
            print("response=========: ", response.status_code)
            return Response({"Message": "List created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
