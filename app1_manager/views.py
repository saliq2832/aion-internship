from django.shortcuts import render, redirect
from django.http import JsonResponse


from .models import Post

def simple_page(request):
    if request.method == 'POST':
        title = request.POST['title']
        image = request.FILES['image']
        user = request.user
        post = Post.objects.create(title=title, image=image, user=user)
        post.save()
        return render(request, 'success.html')
    return render(request, 'simple_page.html')

def post_list(request):
    posts = Post.objects.all()
    post_list = [{'title': post.title, 'image': post.image.url} for post in posts]
    return JsonResponse({'posts': post_list})

def post_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        user = request.user
        post = Post.objects.create(title=title, image=image, user=user)
        return JsonResponse({'message': 'Post created successfully'})

def post_retrieve(request, pk):
    post = Post.objects.get(pk=pk)
    return JsonResponse({'title': post.title, 'image': post.image.url})

def post_update(request, pk):
    if request.method == 'PUT':
        post = Post.objects.get(pk=pk)
        post.title = request.PUT.get('title')
        post.image = request.FILES.get('image')
        post.save()
        return JsonResponse({'message': 'Post updated successfully'})

def post_delete(request, pk):
    if request.method == 'DELETE':
        Post.objects.get(pk=pk).delete()
        return JsonResponse({'message': 'Post deleted successfully'})