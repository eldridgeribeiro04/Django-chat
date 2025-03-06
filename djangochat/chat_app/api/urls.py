from django.urls import path
from chat_app.api.views import ChatRoomAPIView, MessageAPIView, ChatRoomDetail, MessageDetail

urlpatterns = [
    path('chatroom/', ChatRoomAPIView.as_view()),
    path('message/', MessageAPIView.as_view()),
    
    path('chatroom/<int:pk>/', ChatRoomDetail.as_view()),
    path('message/<int:pk>/', MessageDetail.as_view()),
]
