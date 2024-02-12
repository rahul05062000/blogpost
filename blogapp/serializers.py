from rest_framework import serializers
from .models import Post
class Post_s(serializers.Serializer):
    Title = serializers.CharField(required=True)
    Body = serializers.CharField(required=True)
    created_at=serializers.CharField(required=True)
    userid=serializers.CharField(required=True)

    class Meta:
        fields = '__all__'
        
class CommentSerializer_s(serializers.Serializer):
    post_id = serializers.CharField(required=True)
    user_id = serializers.CharField(required=True)
    content=serializers.CharField(required=True)
    created_at=serializers.CharField(required=True)

    class Meta:
        fields = '__all__'
        
class UserProfile_s(serializers.Serializer):
    name = serializers.CharField(required=True)
    lastname = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    password=serializers.CharField(required=True)

    class Meta:
        fields = '__all__'



class Login_s(serializers.Serializer):
    email = serializers.CharField(required=True)
    password=serializers.CharField(required=True)

    class Meta:
        fields = '__all__'



class PostandComment_s(serializers.Serializer):
    id = serializers.CharField(required=True)


    class Meta:
        fields = '__all__'




class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'created_at', 'user_id']



