from django.urls import path
import post.views

app_name = 'post'

urlpatterns = [
    path('', post.views.post_list, name='post_list'),
    path('new',post.views.post_new, name='post_new'),
    path('edit/<int:pk>/',post.views.post_edit,name='post_edit'),
    path('delete/<int:pk>/',post.views.post_delete, name='post_delete'),
    path('like',post.views.post_like, name='post_like'),
    path('bookmark',post.views.post_bookmark, name='post_bookmark'),
    path('comment/new', post.views.comment_new, name='comment_new'),
    path('comment/delete', post.views.comment_delete, name='comment_delete'),
    path('explore/tags/<tag>/', post.views.post_list, name='post_search'),
    path('<int:pk>',post.views.post_detail, name='post_detail'),
    path('<username>/list/detail',post.views.my_post_list, name='my_post_list'),
]