from rest_framework import generics

from chat_app.models import ChatRoom, Message
from chat_app.api.serializers import ChatRoomSerializer, MessageSerializer


class ChatRoomAPIView(generics.ListCreateAPIView):
    
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class MessageAPIView(generics.ListCreateAPIView):
    
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    
    
class ChatRoomDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    
    
class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
        