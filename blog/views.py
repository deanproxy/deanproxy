from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from blog.models import Post, Comment, Tag
from blog.forms import CommentForm, PostForm
import logging

# Login required decorator. Maybe should be moved out but we only care
# about it in the blog stuff right now.
def login_required(func):
	def check_login(request, *args, **kwargs):
		if request.session['logged_in']:
			return func(request, *args, **kwargs)
		else:
			return HttpResponse(status=401)
	return check_login

def index(request):
	posts = Post.objects.order_by('created_at')[:5].reverse()
	return render(request, 'blog/index.html', {'posts': posts})

def show(request, id):
	post = get_object_or_404(Post, pk=id)
	comments = post.comment_set.order_by('created_at').reverse()
	return render(request, 'blog/show.html', {'post':post, 'comments':comments})

def show_by_tag(request, tag):
	tag = get_object_or_404(Tag, pk=tag)
	return render(request, 'blog/index.html', {'posts':tag.post_set.all()})

def search(request):
	query = request.GET['query']
	posts = Post.objects.filter(title__icontains=query, message__icontains=query).order_by('created_at').reverse()
	return render(request, 'blog/index.html', {'posts':posts})


@login_required
def new_post(request):
	return render(request, 'blog/edit.html')

@login_required
def create(request):
	form = PostForm(request.POST)
	if form.is_valid():
		post = form.save()
		post.add_tags(request.POST['tags'])
		return redirect(post.uri())
	else:
		logging.error(form.errors)
	return render(request, 'blog/edit.html', {'post':form.instance})

@login_required
def edit(request, id):
	post = get_object_or_404(Post, pk=id)
	return render(request, 'blog/edit.html', {'post':post})

@login_required
def update(request, id):
	form = PostForm(request.POST, instance=Post.objects.get(pk=id))
	if form.is_valid():
		post = form.save()
		post.add_tags(request.POST['tags'])
		return redirect(post.uri())
	return render(request, 'blog/edit.html', {'post':post})

@login_required
def destroy(request, id):
	post = get_object_or_404(Post, pk=id)
	post.delete()
	return redirect(reverse('blog_url'))


def create_comment(request):
	status = 500
	form = CommentForm(request.POST)
	if form.is_valid():
		comment = form.save()
		send_mail(
			'[deanproxy] New Comment',
			'A new post has been submitted on the post: %s\r\n\r\nhttp://%s/%s' %
				(comment.post.title, settings.DOMAIN_NAME, comment.post.uri()),
			'deanproxy <dean@deanproxy.com>',
			['dean@deanproxy.com']
		)
		status = 200
	return HttpResponse(status=status)

@login_required
def delete_comment(request, id):
	comment = get_object_or_404(Comment, pk=id)
	comment.delete()
	return HttpResponse(status=200)


