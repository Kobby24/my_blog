from django.shortcuts import render
from django.http import HttpResponse
from .forms import Login, CreatePost
from .utils import *


def home(request):
    post = get_all_post()
    event = get_event()
    print(event)

    return render(request, 'index.html', {"data": post,'event':event})


def article(request, p_id):

    post = get_post(post_id=p_id)
    context = {'id': p_id, 'post': post}
    return render(request, 'post.html', context)


def about(request):
    return render(request, 'about.html')


def admins(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            ad_name = form.cleaned_data['admin_name']
            ad_password = form.cleaned_data['password']


            is_admin = None
            if is_admin:
                post = None
                return render(request, 'index.html', {"data": post, "check": is_admin})
            else:
                return HttpResponse(status=403)
    else:
        form = Login()
    return render(request, 'login.html', {'form': form})


def create(request):
    if request.method == "POST":
        form = CreatePost(request.POST)

        if form.is_valid():
            post = {
                'title': form.cleaned_data['title'],
                'subtitle': form.cleaned_data['subtitle'],
                'body': form.cleaned_data['body'],
                'url': form.cleaned_data['url']
            }

            return home(request)
        else:
            return HttpResponse(status=404)
    else:
        form = CreatePost()
        return render(request, 'createPost.html', {'form': form, 'mode': 'create'})

# def delete(request, p_id):
#     if None:
#         post = None
#         return render(request, 'index.html', {"data": post})
#     else:
#         return HttpResponse(status=404)


# def update(request, p_id):
#     post = None
#     if request.method == 'POST':
#         form = CreatePost(request.POST)
#         if form.is_valid():
#             article_body = {
#                 'title': form.cleaned_data['title'],
#                 'subtitle': form.cleaned_data['subtitle'],
#                 'url': form.cleaned_data['url'],
#                 'body': form.cleaned_data['body']
#             }
#
#             return home(request)
#
#     else:
#         form = CreatePost(initial={
#             'title': post['title'],
#             'subtitle': post['subtitle'],
#             'url': post['url'],
#             'body': post['body']
#         })
#
#     return render(request, 'createPost.html', {'form': form, 'mode': 'update','p_id':p_id})
