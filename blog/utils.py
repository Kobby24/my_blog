from .models import *
from django.core.mail import send_mail
def get_post(post_id):
    post = BlogPost.objects.get(blog_id=post_id)
    post.video_url= youtube(post.video_url)

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
    events = Events.objects.all()
    if len(events) >0:
        event = Events.objects.get(event_id=len(events))
        return event

    else:
        return None




import re

def youtube(url):
    url=str(url)
    """Extracts the src URL using regex."""
    match = re.search(r'src="([^"]+)"', url)
    m = match.group(1) if match else None
    if m:
        return m.split('/')[-1]
    else:
        return m


