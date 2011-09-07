from django.http import HttpResponse
from django.shortcuts import render

def code(request):
	return render(request, 'base/code.html')

def about(request):
	return render(request, 'base/about.html')

def music(request):
	return render(request, 'base/music.html')
