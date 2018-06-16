from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from datetime import datetime
from .forms import PostForm
from .models import Post
from comment.models import Comment

# Create your views here.

@login_required(login_url='/auth/login')
def create_post(request):
	form = PostForm(request.POST or None, request.FILES or None)
	print(form)
	if form.is_valid():
		print("VALID")
		post_instance = form.save(commit=False)
		post_instance.date = datetime.now()
		post_instance.owner = request.user
		post_instance.save()
		return HttpResponseRedirect("/")
	context = {
		'form': form,
		'username': request.user
	}
	return render(request, 'blog/post_create.html', context)
	#return render(request, 'blog/index.html', {'username': auth.get_user(request)})

def post(request, post_id):
	args = {}
	post = Post.objects.get(pk = post_id)
	comments = Comment.objects.all().filter(post=post)
	print(post.image.url)
	args['p_id'] = post.id
	args['image'] = post.image.url
	args['name'] = post.name
	args['description'] = post.description
	args['comments'] = comments
	args['username'] = request.user
	return render(request, 'blog/post.html', args)

def index(request):
	args = {}
	username = auth.get_user(request).username
	args['post_list'] = Post.objects.all()
	if username != 'AnonimusUser':
		args['username'] = username
	else:
		args['username'] = 'Anonimus'
	return render(request, 'blog/index.html', args)
