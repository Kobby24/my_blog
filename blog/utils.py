from .models import *
from django.core.mail import send_mail
def get_post(post_id):
    post = BlogPost.objects.get(blog_id=post_id)
    return post

def get_all_post():
    posts = BlogPost.objects.all()
    blog_posts = []

    for post in posts:
        blog_posts.append(get_post(post.blog_id))
    return blog_posts

def send_message(name,phone,user_mail,message):
    send_mail(
        subject=f"{name}'s Message From Blog. contact:{phone}",
        message=message,
        from_email=user_mail,
        recipient_list=['kobbygilbert@233gmail.com'],fail_silently=False

    )


