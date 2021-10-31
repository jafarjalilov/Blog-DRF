from django.urls import path
from .views import PostList, PostDetail

app_name = 'blog_api'

urlpatterns = [
    path('', PostList, name='post_list'), #.as_view()
    path('<int:pk>/', PostDetail, name='post_detail'), #.as_view()
]