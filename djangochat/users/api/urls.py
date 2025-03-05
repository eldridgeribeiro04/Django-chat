from django.urls import path

from rest_framework.authtoken import views

from users.api.views import CreateUser, LoginView, LogoutView, UserList, UserDetail

urlpatterns = [
    path('create_usr/', CreateUser.as_view(), name="createuser"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    path('users/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view())
]