from django.urls import path, include
from blog_django_api.views import PostList, PostDetail, UserDetail, GroupList, GroupDetail, UserLogin, UserRegister

urlpatterns = [
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('groups/', GroupList.as_view()),
    path('groups/<int:pk>/', GroupDetail.as_view()),
    path('login/', UserLogin.as_view()),
    path('register/', UserRegister.as_view()),
]
