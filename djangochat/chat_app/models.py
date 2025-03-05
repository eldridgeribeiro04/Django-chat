from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class ChatRoom(models.Model):
    name = models.CharField(max_length=25, null=True, blank=True)
    is_group_chat = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_chatroom_test")
    participants = models.ManyToManyField(User, related_name="chatrooms")
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.is_group_chat:
            participants = self.participants.exclude(id=self.creator.id)
            if participants.count() == 0:
                raise ValidationError("Cannot create a group with yourself.")
        """Ensure group chats have a name"""
        if self.is_group_chat and not self.name:
            raise ValidationError("A group should have a name")
        if not self.is_group_chat and self.name:
            raise ValidationError("Private chats cannot have a name")
        
    def save(self, *args, **kwargs):
        # if not self.pk: # Checking if new user or not.
        self.full_clean()
        super().save(*args, **kwargs)
        self.participants.add(self.creator)
        # print(self.participants.all()) #Testing if the creator is added to participants
        
    def __str__(self):
        if self.is_group_chat:
            return self.name
        else:
            for user in self.participants.all():
                print(user.username)
            # participants = self.participants.exclude(id=self.creator.id)
            # print(participants)
            if self.participants.exists():
                return f"{self.creator}'s private chat with {self.participants.first().username}"
            return "Private chat"
    
    
class Message(models.Model):
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE ,related_name="message")
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    message = models.CharField(max_length=250)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        if self.chat.is_group_chat:
            return f"{self.sender}: message- {self.message} to {self.chat.name}"
        else:
            return f"{self.sender}: message- {self.message} to {self.chat.participants.first().username}"
