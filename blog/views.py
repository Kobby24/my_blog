import uuid

from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

from django.http import HttpResponse
from .forms import Login, CreatePost
from .utils import *

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import BlogPost,Like  # Replace with your actual model

from django.http import JsonResponse

def home(request):
    post = get_all_post()

    event = get_events()
    response = render(request, 'index.html', {"data": post,'event':event})

    anonymous_user_id = get_anonymous_user_id(request)
    response.set_cookie('anonymous_user_id', anonymous_user_id, max_age=31536000)

    return response


def article(request, p_id):
    post = get_post(post_id=p_id)
    context = {'id': p_id, 'post': post}
    return render(request, 'post.html', context)


def about(request):
    founder = get_founder()
    clergy = get_clergy()
    elder = get_elders()
    deacon = get_deacons()
    worker = get_workers()
    context = {
        "first_leader": founder if founder else None,  # Handle empty QuerySet
        "clergy": clergy if clergy else None,
        'elder':elder if elder else None,
        'deacons':deacon if deacon else None,
        'worker':worker if worker else None
    }
    return render(request, 'about.html',context)


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




def get_anonymous_user_id(request):
    anonymous_user_id = request.COOKIES.get('anonymous_user_id')
    if not anonymous_user_id:
        anonymous_user_id = str(uuid.uuid4())

    return anonymous_user_id
def login_(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Try to get the 'next' parameter from either GET or POST
        next_url = request.GET.get('next') or request.POST.get('next')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(next_url) if next_url else redirect('user_form')  # Redirect to next URL or default
        else:
            return HttpResponse(status=403)  # Or render with an error message

    next_url = request.GET.get('next', '')  # Preserve 'next' parameter for redirection
    return render(request, 'registration/login.html', {'next': next_url})

def signup(request):
    return render(request,"signin.html")


@csrf_exempt
def like_post(request, post_id):
    if request.method == "POST":
        post = get_object_or_404(BlogPost, blog_id=post_id)

        # Get anonymous user ID from cookies
        anonymous_user_id = get_anonymous_user_id(request)

        # Check if this user has already liked the post
        if Like.objects.filter(anonymous_user_id=anonymous_user_id, post=post).exists():
            return JsonResponse({"status": "already_liked", "like_count": post.like_count})

        # Increase like count
        post.like_count += 1
        post.save()

        # Save the like in the database
        Like.objects.create(anonymous_user_id=anonymous_user_id, post=post)

        return JsonResponse({"status": "liked", "like_count": post.like_count})

    return JsonResponse({"status": "error"}, status=400)




