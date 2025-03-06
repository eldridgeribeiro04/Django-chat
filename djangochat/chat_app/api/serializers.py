from rest_framework import serializers
from chat_app.models import ChatRoom , Message

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'
        depth = 0
        
        
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
        depth = 0
        
    def validate(self, data):
        chat = data['chat']
        sender = data['sender']
        
        if not chat.participants.filter(id=sender.id).exists():
            raise serializers.ValidationError("Only members of the chat can send messages.")

        return data