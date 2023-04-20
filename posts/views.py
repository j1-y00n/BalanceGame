from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
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
    comments = post.comment_set.all()
    comment_form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
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
    if request.user not in post.select1_users.all() and request.user not in post.select2_users.all():
        answer1 = request.POST.get('select1')
        answer2 = request.POST.get('select2')

        if answer1 == post.select1_content:
            post.select1_users.add(request.user)
        else:
            post.select2_users.add(request.user)

    return redirect('posts:detail', post.pk)


@login_required
def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user in post.like_users.all():
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)

    return redirect('posts:detail', post.pk)


@login_required
def comment_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()

    return redirect('posts:detail', post.pk)


@login_required
def comment_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.user == comment.user:
        comment.delete()

    return redirect('posts:detail', post_pk)
