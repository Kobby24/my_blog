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

def get_events():
    events = Events.objects.all()
    event_posts = []
    for event in events:
        event_posts.append(get_event(event.event_id))
    return event_posts

def get_event(e_id=0):
    if e_id==0:
        events = Events.objects.all()
        if len(events) >0:
            get_event(len(events))
        else:
            return None

    else:
        event = Events.objects.get(event_id=e_id)
        return event



# def send_message(name,phone,user_mail,message):
#     send_mail(
#         subject=f"{name}'s Message From Blog. contact:{phone}",
#         message=message,
#         from_email=user_mail,
#         recipient_list=['kobbygilbert@233gmail.com'],fail_silently=False
#
#     )


