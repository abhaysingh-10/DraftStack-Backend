from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


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
    
    # Create token for this User
    token = Token.objects.create(user=user)
    
    return Response({"Message":"Account Created Successfully",
                     "token":token.key, #send token back
                     },status=status.HTTP_201_CREATED)
    
    
# LOGIN- get TOKEN  POST

@api_view(['POST'])
@permission_classes([AllowAny]) # anyone can register — no token needed

def login(request):
    
    # get username password from request
    username = request.data.get('username')
    password = request.data.get('password')
    
    # checking if both are provided
    if not username or not password:
        return Response({"Error":"Username and password are required"},status=status.HTTP_400_BAD_REQUEST)
    
    # checking if user exists
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({"Error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
    
    # checking if password is correct or not 
    # using check_password it matches the hashed password  present in the DB
     
    if not user.check_password(password):
        return Response({"Error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
    
    # get or create token 
    # get_or_create - if token exists return it, if not create new one
    token , created = Token.objects.get_or_create(user= user)
    
    return Response(
        {
            "Message":"Login Successful",
            "token": token.key,
            
        },
        status=status.HTTP_200_OK
        )
    
    
# LOGOUT - DELETE THE TOKEN

@api_view(["POST"])
def logout(request):
    
    # Delete token from DB - next time user must login again to get new token
    request.user.auth_token.delete()
    return Response({"Message":"Logout Successfully"},status=status.HTTP_200_OK)
    
    
    
    
    
    
    