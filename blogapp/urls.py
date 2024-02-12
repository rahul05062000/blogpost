from django.urls import path, include
from . import views

urlpatterns = [
    path('postlist',views.postlist),
    path('CreatePost',views.CreatePost_f),
    path('create_comment',views.create_comment),
    path('create_user',views.UserProfile_f),
    path('Login',views.Login),
    path('PostandComment',views.PostandComment),
    path('update_post',views.update_post),
    path('delete_post',views.delete_post),

]