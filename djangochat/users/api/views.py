# Import from REST API
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import permissions

# Django Imports
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

# Import from within this project
from users.api.serializers import CreateUserSerializer, UserSerializer


class CreateUser(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = CreateUserSerializer
    
    def perform_create(self, serializer):
        user = serializer.save()
        Token.objects.get_or_create(user=user)
        
# Creating a token when user is created 
# from django.dispatch import receiver
# from django.db.models.signals import post_save
# from django.conf import settings

# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
    
# For generating tokens after a user has been created
# from django.contrib.auth.models import User

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)
        
        
class LoginView(ObtainAuthToken):
    
    def post(self , request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        token, created = Token.objects.get_or_create(user=user)
        print(request.stream)
        return Response({
            'token': token.key,
            'user': user.username
        })
        
        
class LogoutView(APIView):
     
     permission_classes = [permissions.IsAuthenticated]
     
     def post(self, request):
        try:  
            request.user.auth_token.delete()
            return Response({"message": "Successfully logged out"}, status=200)
        except Exception:
            return Response({"message": "Something went wrong"}, status=500)
        

# Retrieving all and single users

class UserList(ListAPIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class UserDetail(RetrieveAPIView):
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer