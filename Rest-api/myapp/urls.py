from django.urls import path
from .models import Comment
from .views import CommentListCreate

urlpatterns = [
    
     path('comments/', CommentListCreate.as_view()),
    
]
