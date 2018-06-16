from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Comment
from blog.models import Post

# Create your views here.

@csrf_exempt
@login_required(login_url='/auth/login')
def create_comment(request, post_id):
	args = {}
	post = Post.objects.get(pk = post_id)
	args['image'] = post.image.url
	args['name'] = post.name
	args['description'] = post.description
	args['username'] = post.owner
	if request.POST:
		text = request.POST.get('comment', '')
		if len(text) == 0:
			return render(request, 'blog/post.html', args)
		owner = request.user
		date = datetime.now()
		post = Post.objects.get(pk=post_id)
		likes = 0
		comment = Comment.objects.create(text=text, likes=likes, date=date, post=post, owner=owner)
		comment.save()
		comments = Comment.objects.all().filter(post=post)
		args['comments'] = comments
	return HttpResponseRedirect("/posts/" + str(post.id))
