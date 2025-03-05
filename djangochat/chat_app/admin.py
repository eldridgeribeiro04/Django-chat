from django.contrib import admin

from chat_app.models import Message, ChatRoom
# Register your models here.

admin.site.register(ChatRoom)
admin.site.register(Message)