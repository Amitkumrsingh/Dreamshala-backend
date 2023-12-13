# api/views.py
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import logout

class UserListCreateView(ObtainAuthToken):
    # This view handles user sign-in (login) using the ObtainAuthToken view
    # It returns an authentication token upon successful login
    pass

class UserLogoutView(APIView):
    # This view handles user logout
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Perform logout logic here
        logout(request)
        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
