from .models import *
from django.db.models import Q
def get_post(post_id):
    post = BlogPost.objects.get(blog_id=post_id)
    post.video_url= youtube(post.video_url)

    return post

def get_all_post():
    posts = BlogPost.objects.all().order_by("-blog_id")
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
        event = Events.objects.get(event_id=e_id)
        return event

    else:
        return None




import re

def youtube(url):
    url=str(url)
    match = re.search(r'src="([^"]+)"', url)
    m = match.group(1) if match else None
    if m:
        return m.split('/')[-1]
    else:
        return m

def get_elders():
    elders = Leaders.objects.filter(leader_title='Elder')
    return elders

def get_founder():
    leaders = Leaders.objects.filter(leader_title='Founder')
    return leaders
def get_clergy():
    clergy = Leaders.objects.filter(leader_title='Pastor')
    return clergy

def get_deacons():
    deacons = Leaders.objects.filter(Q(leader_title__icontains="deacon") | Q(leader_title__icontains="deaconess"))
    return deacons
def get_overseers():
    overseers = Leaders.objects.filter(leader_title='Overseer')
    return overseers

def get_workers():
    workers = Leaders.objects.filter(leader_title='Worker')
    return workers


def about_background():
    image = AboutPageBackground.objects.all().latest('image_id')
    return image
