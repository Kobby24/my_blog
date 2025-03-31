from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('article/<p_id>', views.article, name='article'),
    path('about/', views.about, name='about'),
    path('admins/', views.admins, name='admins'),
    path('like/<int:post_id>/', views.like_post, name='like_post'),
    path('login_/',views.login_,name='login_'),
    path('signup',views.signup,name="signup")
]

