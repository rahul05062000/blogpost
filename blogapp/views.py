from .serializers import *
from .models import *
import json
from rest_framework.decorators import api_view
from rest_framework import status as stus
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from datetime import datetime
from django.core.serializers import serialize




@api_view(['POST'])
def postlist(request):
    try: 
            data=Post.objects.all()
            data=serialize('json', data)
            data=json.loads(data)
            for i in data:
                 print(i)
            if data :
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'data':data,
                    'message': 'Data successFully fetched '
                }
                return Response(json_data, status=stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'count': 0,
                    'data': [],
                    'message': 'Data not Fetched',
                }
                return Response(json_data, status=stus.HTTP_200_OK)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['POST'])
def CreatePost_f(request):
    try:
        serializer = Post_s(data=request.data)
        if  serializer.is_valid():
            title = serializer.validated_data.get('Title')
            body = serializer.validated_data.get('Body')
            created_at = serializer.validated_data.get('created_at')
            user_id = serializer.validated_data.get('userid')
            post = Post(title=title, body=body, created_at=created_at, user_id=user_id)
            post.save()

            if post :
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'message': 'Data Saved Successfully '
                }
                return Response(json_data, status=stus.HTTP_200_OK)
            else:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'count': 0,
                    'data': [],
                    'message': 'Data not Fetched',
                }
                return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error --------:", e)
        json_data = {
            'status_code': 400,
            'status': 'Fail',
            'Reason': e,
            'Remark': 'landed in exception',
        }
        raise APIException(json_data, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)
     


@api_view(['POST'])
def create_comment(request):
    try:
        serializer=CommentSerializer_s(data=request.data)
        if serializer.is_valid():
            post_id = serializer.validated_data.get('post_id')
            user_id = serializer.validated_data.get('user_id')
            content = serializer.validated_data.get('content')
            created_at=datetime.now()
            comment=Comment(post_id=post_id,user_id=user_id,content=content,created_at=created_at)
            comment.save()

            # Create the comment
            # comment = Comment.objects.create(post_id=post_id, user_id=user_id, content=content)

            json_data = {
                'status_code': 200,
                'status': 'Success',
                'message': 'Comment saved successfully.'
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error: ", e)
        json_data = {
            'status_code': 500,
            'status': 'Fail',
            'Reason': str(e),
            'Remark': 'Landed in exception',
        }
        return Response(json_data, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def UserProfile_f(request):
    try:
        serializer=UserProfile_s(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            lastname = serializer.validated_data.get('lastname')
            email =serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user_profile = UserProfile(name=name, lastname=lastname, email=email, password=password)
            user_profile.save()

            json_data = {
                'status_code': 200,
                'status': 'Success',
                'message': 'User Created successfully.'
            }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error: ", e)
        json_data = {
            'status_code': 500,
            'status': 'Fail',
            'Reason': str(e),
            'Remark': 'Landed in exception',
        }
        return Response(json_data, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def Login(request):
    try:
        serializer=Login_s(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            
            # Query the database to find a user with the provided email and password
            try:
                user_profile = UserProfile.objects.get(email=email, password=password)
                # User exists, return success response
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'user_profile':user_profile,
                    'message': 'User logged in successfully.'
                }
                return Response(json_data, status=stus.HTTP_200_OK)
            except UserProfile.DoesNotExist:
                json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'message': 'Invalid Credentials.'
                }
            return Response(json_data, status=stus.HTTP_200_OK)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error: ", e)
        json_data = {
            'status_code': 500,
            'status': 'Fail',
            'Reason': str(e),
            'Remark': 'Landed in exception',
        }
        return Response(json_data, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
def PostandComment(request):
    try:
        serializer=PostandComment_s(data=request.data)
        if serializer.is_valid():
            id = serializer.validated_data.get('id')
            post=Post.objects.get(id=id) 
            comments=Comment.objects.filter(user_id=id)
            json_data = {
                    'status_code': 200,
                    'status': 'Success',
                    'Comments': comments,
                    'Post':post,
                }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
        else:
            json_data = {
                'status_code': 300,
                'status': 'Fail',
                'Reason': serializer.errors,
                'Remark': 'Send valid data'
            }
            return Response(json_data, status=stus.HTTP_300_MULTIPLE_CHOICES)
    except Exception as e:
        print("Error: ", e)
        json_data = {
            'status_code': 500,
            'status': 'Fail',
            'Reason': str(e),
            'Remark': 'Landed in exception',
        }
        return Response(json_data, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['POST'])
def update_post(request, post_id):
    try:
        # Get the post instance to update
        post = Post.objects.get(pk=post_id)
        
        # Validate and deserialize request data
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            # Save the updated post
            serializer.save()
            return Response({'status': 'Success', 'message': 'Post updated successfully.'}, status=stus.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=stus.HTTP_400_BAD_REQUEST)
    except Post.DoesNotExist:
        # Handle case where the post does not exist
        return Response({'status': 'Fail', 'message': 'Post not found.'}, status=stus.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Handle other exceptions
        print("Error: ", e)
        return Response({'status': 'Fail', 'message': 'Error occurred while processing the request.'}, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)

    

@api_view(['DELETE'])
def delete_post(request, post_id):
    try:
        # Get the post instance to delete
        post = Post.objects.get(pk=post_id)
        
        # Delete the post
        post.delete()
        
        return Response({'status': 'Success', 'message': 'Post deleted successfully.'}, status=stus.HTTP_200_OK)
    except Post.DoesNotExist:
        # Handle case where the post does not exist
        return Response({'status': 'Fail', 'message': 'Post not found.'}, status=stus.HTTP_404_NOT_FOUND)
    except Exception as e:
        # Handle other exceptions
        print("Error: ", e)
        return Response({'status': 'Fail', 'message': 'Error occurred while processing the request.'}, status=stus.HTTP_500_INTERNAL_SERVER_ERROR)
    



