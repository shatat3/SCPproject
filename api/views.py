from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserSerializer
from .models import UsersModel, MealsModel
from rest_framework.views import APIView
from .serializer import UserSerializer
from rest_framework import status
from django.http import Http404

class UsersList(APIView):
    def get(self, request, format=None):
        users = UsersModel.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UsersDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return UsersModel.objects.get(pk=pk)
        except UsersModel.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_api = self.get_object(pk)
        serializer = UserSerializer(user_api)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = UserSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


