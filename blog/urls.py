"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.urls.conf import include
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostList,PostCreate,PostDetails, PostUpdate, getPostDetails, saveComment



staff_patterns = [

    path('', views.dashboard, name='staff'),
    path('feedback', views.showFeedback, name='feedback'),
    path('categories',views.showCategory,name='categories'),
    path('store/categories',views.storeCategory,name='store_category'),
    path('categories/form',views.categoryForm,name='add_category'),
    path('delete/category <id>',views.deleteCategory,name='delete_category'),
    path('delete/feedback <id>',views.deleteFeedback,name='delete_feedback'),
    path('posts',PostList.as_view(),name='posts'),
    path('create/post',PostCreate.as_view(),name='add_post'),
    path('view/post/<pk>',PostDetails.as_view(),name='view_post'),
    path('update/post/<pk>',PostUpdate.as_view(),name='update_post'),


]

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('post-detail/', views.postDetail, name="post-detail"),
    path('staff/',include(staff_patterns)),
    path ('save/feedback',views.saveFeedback, name = "save_feedback"),
    path('posts/details/<id>',views.getPostDetails,name="post_detail"),
    path('save/comment/<id>',views.saveComment,name="save_comment")

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)