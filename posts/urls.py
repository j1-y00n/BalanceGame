from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/answer/<str:answer>/', views.answer, name='answer'),
    path('<int:post_pk>/likes/', views.likes, name='likes'),
    path('<int:post_pk>/comment/', views.comment_create, name='comment_create'),
    path('<int:post_pk>/comment/<int:comment_pk>/delete/',
         views.comment_delete, name='comment_delete'),

]
