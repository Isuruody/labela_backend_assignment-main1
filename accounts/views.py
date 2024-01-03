from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from .models import CustomUser
from .serializers import UserSerializer, SignupSerializer, LoginSerializer, LogoutSerializer

class SignupView(generics.CreateAPIView):
    """
    API view for user registration (Signup).
    """
    serializer_class = SignupSerializer

class LoginView(APIView):
    """
    API view for user login.
    """
    def post(self, request, *args, **kwargs):
        """
        Handles user login by validating provided credentials and generating tokens.
        """
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Retrieve user based on validated email
        user = CustomUser.objects.get(email=serializer.validated_data['email'])
        
        # Generate RefreshToken and Access Token for the user
        refresh = RefreshToken.for_user(user)
        
        # Return tokens in the response
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        })

class LogoutView(APIView):
    """
    API view for user logout.
    """
    def post(self, request, *args, **kwargs):
        """
        Handles user logout by invalidating provided refresh token.
        """
        serializer = LogoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            # Invalidate the provided refresh token
            refresh_token = serializer.validated_data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()
        except Exception as e:
            # Handle exceptions for invalid tokens
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Return success message for a successful logout
        return Response({'success': 'User logged out successfully'})
