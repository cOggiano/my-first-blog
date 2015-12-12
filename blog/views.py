from django.shortcuts import render
from django.utils import timezone
from .models import Post

#return un metodo render che ci fornirà il template blog/post_list.html
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

