from django.shortcuts import render

# Create your views here.
def subscribe(req):
	ctx = {}
	return render(req, 'subscribe/subscribe.html', ctx)