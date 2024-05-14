from rest_framework import serializers
from tunga_django_blog.models import Post
from django.contrib.auth.models import User, Group


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

