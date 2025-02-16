from .models import *

def get_post(post_id):
    post = BlogPost.objects.get(blog_id=post_id)
    return post

def get_all_post():
    posts = BlogPost.objects.all()
    blog_posts = []

    for post in posts:
        blog_posts.append(get_post(post.blog_id))
    return blog_posts

