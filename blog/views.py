from django.shortcuts import render

#return un metodo render che ci fornirà il template blog/post_list.html
def post_list(request):
	return render(request, 'blog/post_list.html', {})

