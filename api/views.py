# api/views.py
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import logout
from rest_framework.authtoken.models import Token


class UserListCreateView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'email': user.email,
            'username': user.username
        })

class UserLogoutView(APIView):
    # This view handles user logout
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Perform logout logic here
        logout(request)
        return Response({'detail': 'Successfully logged out.'}, status=status.HTTP_200_OK)
