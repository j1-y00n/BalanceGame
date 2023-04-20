from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:detail', post_pk=post.pk)

    else:
        form = PostForm()

    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


def answer(request, post_pk, answer):
   
    post = Post.objects.get(pk=post_pk)
    # if request.user not in post.select1_users.all() and request.user not in post.select2_users.all():
    #     if answer not in post.select1_posts.all():
    #         post.select2_users.add(request.user)
    #     else:
    #         post.select1_users.add(request.user)

    if request.user not in post.select1_users.all():
        post.select1_users.add(request.user)
        # answer = select1_content
        answer = request.POST.get('select1')
    #     if 
    # if request.user in post.select2_users.all():
    #     select2_content=answer

    return redirect('posts:detail', post.pk)
