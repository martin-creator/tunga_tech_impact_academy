from django.contrib.auth.models import User, Group
from blog.models import Post
from blog_django_api.serializers import PostSerializer, UserSerializer
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes

#  @extend_schema(
#         parameters=[
#             OpenApiParameter(name='username', type=str, location=OpenApiParameter.QUERY, required=True),
#             OpenApiParameter(name='email', type=str, location=OpenApiParameter.QUERY, required=True),
#             OpenApiParameter(name='role', type=str, location=OpenApiParameter.QUERY, required=True),
#             OpenApiParameter(name='password', type=str, location=OpenApiParameter.QUERY, required=True),
#             OpenApiParameter(name='phone_number', type=str, location=OpenApiParameter.QUERY, required=False),
#             OpenApiParameter(name='address', type=str, location=OpenApiParameter.QUERY, required=False),
#             OpenApiParameter(name='job_title', type=str, location=OpenApiParameter.QUERY, required=False),
#             OpenApiParameter(name='department', type=str, location=OpenApiParameter.QUERY, required=False),
#             OpenApiParameter(name='job_status', type=str, location=OpenApiParameter.QUERY, required=False),

#         ],
#         examples=[
#             OpenApiExample(
#                 'Example 1',
#                 summary='User Registration',
#                 description='Register a new user',
#                 value={
#                     "username": "username",
#                     "email": "email",
#                     "role": "role",
#                     "password": "password",
#                     "phone_number": "phone_number",
#                     "address": "address",
#                     "job_title": "job_title",
#                     "department": "department",
#                     "job_status": "job_status"

#                 }
#             )
#         ], 

#         responses={201: OpenApiResponse(response=OpenApiTypes.OBJECT, description='User data')}
#     )


class PostList(APIView):
    """
    List all posts, or create a new post.

    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='title', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='content', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='author', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='status', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='Post Creation',
                description='Create a new post',
                value={
                    "title": "title",
                    "content": "content",
                    "author": "author",
                    "status": "status",
                }
            )
        ],
        responses={201: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Post data')}
    )

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    @extend_schema(
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Post data')}
    )
    
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        responses={204: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Post data')}
    )
    
    def delete(self, request):
        posts = Post.objects.all()
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @extend_schema(
        parameters=[
            OpenApiParameter(name='title', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='content', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='author', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='status', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='Post Update',
                description='Update a post',
                value={
                    "title": "title",
                    "content": "content",
                    "author": "author",
                    "status": "status",
                }
            )
        ],
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Post data')}
    )
    
    def put(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    

class PostDetail(APIView):

    """
    Retrieve, update or delete a post instance.
    
    """
    permission_classes = [IsAuthenticated]

    @extend_schema(
        parameters=[
            OpenApiParameter(name='title', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='content', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='author', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='status', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='Post Update',
                description='Update a post',
                value={
                    "title": "title",
                    "content": "content",
                    "author": "author",
                    "status": "status",
                }
            )
        ],
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Post data')}
    )

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            Response(status=status.HTTP_404_NOT_FOUND)

    @extend_schema(
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Post data')}
    )

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    @extend_schema(
        parameters=[
            OpenApiParameter(name='title', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='content', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='author', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='status', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='Post Update',
                description='Update a post',
                value={
                    "title": "title",
                    "content": "content",
                    "author": "author",
                    "status": "status",
                }
            )
        ],
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Post data')}
    )

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        responses={204: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Post data')}
    )

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# we use only use username', 'first_name', 'last_name', 'email', 'password' for usermosel


class UserRegister(APIView):
    """
    Register a new user, or list all users, or delete all users.
    
    """
    @extend_schema(
        parameters=[
            OpenApiParameter(name='username', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='first_name', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='last_name', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='email', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='password', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='User Registration',
                description='Register a new user',
                value={
                    "username": "username",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "email": "email",
                    "password": "password",
                }
            )
        ],
        responses={201: OpenApiResponse(response=OpenApiTypes.OBJECT, description='User data')}
    )
    def post(self, request):
        user = User.objects.create_user(username=request.data['username'], first_name=request.data['first_name'], last_name=request.data['last_name'], email=request.data['email'], password=request.data['password'])
        user.save()
        return Response(status=status.HTTP_201_CREATED)
    
   
    

class UserLogin(APIView):
    """
    Login a user, or list all users, or delete all users.
    """
    @extend_schema(
        parameters=[
            OpenApiParameter(name='username', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='password', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='User Login',
                description='Login a user',
                value={
                    "username": "username",
                    "password": "password",
                }
            )
        ],
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='User data')}
    )
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user is not None:
            login(request, user)
            # generate a token and retirn it
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
   
    

class UserDetail(APIView):
    @extend_schema(
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='User data')}
    )
    def get(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    @extend_schema(
        parameters=[
            OpenApiParameter(name='username', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='first_name', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='last_name', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='email', type=str, location=OpenApiParameter.QUERY, required=True),
            OpenApiParameter(name='password', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='User Update',
                description='Update a user',
                value={
                    "username": "username",
                    "first_name": "first_name",
                    "last_name": "last_name",
                    "email": "email",
                    "password": "password",
                }
            )
        ],
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='User data')}
    )

    def put(self, request, pk):
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        responses={204: OpenApiResponse(response=OpenApiTypes.OBJECT, description='User data')}
    )

    def delete(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class GroupList(APIView):
    """
    List all groups, or create a new group.
    """
    @extend_schema(
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Group data')}
    )
    def get(self, request):
        groups = Group.objects.all()
        serializer = UserSerializer(groups, many=True)
        return Response(serializer.data)
    
    @extend_schema(
        responses={204: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Group data')}
    )
    def delete(self, request):
        groups = Group.objects.all()
        groups.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @extend_schema(
        parameters=[
            OpenApiParameter(name='name', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='Group Creation',
                description='Create a new group',
                value={
                    "name": "name",
                }
            )
        ],
        responses={201: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Group data')}
    )

    def post(self, request):
        group = Group.objects.create(name=request.data['name'])
        group.save()
        return Response(status=status.HTTP_201_CREATED)
    
    @extend_schema(
        parameters=[
            OpenApiParameter(name='name', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='Group Update',
                description='Update a group',
                value={
                    "name": "name",
                }
            )
        ],
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Group data')}
    )

    def put(self, request):
        groups = Group.objects.all()
        serializer = UserSerializer(groups, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class GroupDetail(APIView):
    """
    Retrieve, update or delete a group instance.
    
    """
    @extend_schema(
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Group data')}
    )
    def get(self, request, pk):
        group = Group.objects.get(pk=pk)
        serializer = UserSerializer(group)
        return Response(serializer.data)
    
    @extend_schema(
        parameters=[
            OpenApiParameter(name='name', type=str, location=OpenApiParameter.QUERY, required=True),
        ],
        examples=[
            OpenApiExample(
                'Example 1',
                summary='Group Update',
                description='Update a group',
                value={
                    "name": "name",
                }
            )
        ],
        responses={200: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Group data')}
    )

    def put(self, request, pk):
        group = Group.objects.get(pk=pk)
        serializer = UserSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @extend_schema(
        responses={204: OpenApiResponse(response=OpenApiTypes.OBJECT, description='Group data')}
    )

    def delete(self, request, pk):
        group = Group.objects.get(pk=pk)
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    
