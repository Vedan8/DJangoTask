from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .tasks import send_welcome_email


class PublicHelloView(APIView): # View for a api which can be accessed by all the users
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "This is a public endpoint."})


class ProtectedDataView(APIView): #Only authenticated uses can access this api.
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"data": "This is protected data. You are logged in."})

class RegisterView(APIView): # Registering the user and sending mail to them using celery with it.
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password or not email:
            return Response({"error": "Missing fields"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        send_welcome_email.delay(email)  
        return Response({"message": "User registered successfully."})
