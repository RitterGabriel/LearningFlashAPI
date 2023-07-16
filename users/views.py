from django.contrib.auth import authenticate
from rest_framework import views
from rest_framework.response import Response
from .serializers import UserSerializer
import base64


class UserView(views.APIView):        
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class LoginView(views.APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        credentials = f'{username}:{password}'
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return Response({'key': encoded_credentials}, status=200)
        return Response({'status': 'invalid credentials'}, status=400)
