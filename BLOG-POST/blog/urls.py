from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('article/<p_id>', views.article, name='article'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('admins/',views.admins, name='admins'),
    path('create/',views.create,name='create'),
    # path('delete/<int:p_id>', views.delete, name='delete'),
    # path('update/<p_id>',views.update,name='update')
    # path('posts/',views.post_list,name='post_list'),
    # path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    # path('posts/create/', views.create_post, name='create_post'),
    # path('posts/<int:post_id>/update/', views.update_post, name='update_post'),
    # path('posts/<int:post_id>/delete/', views.delete_post, name='delete_post'),
]

