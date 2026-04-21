from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError



# REGISTER CREATE NEW USER/ACCOUNT POST

@api_view(['POST'])
@permission_classes([AllowAny]) # anyone can register — no token needed

def register(request):
    
    # Getting username and password from request
    username = request.data.get('username')
    password = request.data.get('password')
    
    # Checking if both are provided
    if not username or not password:
        return Response({'Error':'username and password required'},status=status.HTTP_400_BAD_REQUEST)
    
    # checking if username is already taken
    if User.objects.filter(username=username).exists():
        return Response({"Error":"username already taken"},status=status.HTTP_400_BAD_REQUEST)
    
    # Create the User  
    user = User.objects.create_user(username=username,password=password)
    
    return Response({"Message":"Account Created Successfully"},status=status.HTTP_201_CREATED)
    

#LOGOUT - JWT AUTHENTICATION 

@api_view(['POST'])
@permission_classes([IsAuthenticated])

def logout(request):
    try:
        refresh_token = request.data.get('refresh')
        token = RefreshToken(refresh_token)
        token.blacklist()
        return Response({"Message":"Logged out Successfully"},status=status.HTTP_200_OK)
    
    except TokenError:
        return Response({"Error":"Invalid Token"},status=status.HTTP_400_BAD_REQUEST)
    
    
        


    
    
    
    
    
    