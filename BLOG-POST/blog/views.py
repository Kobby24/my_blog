from django.shortcuts import render
from .models import Article, Admins
from django.http import HttpResponse
from .forms import Login, CreatePost


def home(request):
    post = Article.all()
    return render(request, 'index.html', {"data": post})


def article(request, p_id):
    post = Article.get(p_id)
    context = {'id': p_id, 'post': post}
    return render(request, 'post.html', context)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def admins(request):
    if request.method == "POST":
        form = Login(request.POST)
        if form.is_valid():
            ad_name = form.cleaned_data['admin_name']
            ad_password = form.cleaned_data['password']

            print(ad_name, ad_password)
            is_admin = Admins.verify_ad(ad_name, ad_password)
            if is_admin:
                post = Article.all()
                return render(request, 'index.html', {"data": post, "check": is_admin})
            else:
                return HttpResponse(status=403)
    else:
        form = Login()
    return render(request, 'login.html', {'form': form})


def create(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        print(form.is_valid())
        if form.is_valid():
            post = {
                'title': form.cleaned_data['title'],
                'subtitle': form.cleaned_data['subtitle'],
                'body': form.cleaned_data['body'],
                'url': form.cleaned_data['url']
            }
            Article.create(post)
            return home(request)
        else:
            return HttpResponse(status=404)


    else:
        form = CreatePost()
        return render(request, 'createPost.html', {'form': form, 'mode': 'create'})


def delete(request, p_id):
    if Article.delete(p_id):
        post = Article.all()
        return render(request, 'index.html', {"data": post})
    else:
        return HttpResponse(status=404)


def update(request, p_id):
    post = Article.get(p_id)
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            article_body = {
                'title': form.cleaned_data['title'],
                'subtitle': form.cleaned_data['subtitle'],
                'url': form.cleaned_data['url'],
                'body': form.cleaned_data['body']
            }
            Article.update(p_id,article_body)
            return home(request)

    else:
        form = CreatePost(initial={
            'title': post['title'],
            'subtitle': post['subtitle'],
            'url': post['url'],
            'body': post['body']
        })

    return render(request, 'createPost.html', {'form': form, 'mode': 'update','p_id':p_id})
