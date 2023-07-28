from django.shortcuts import render, redirect

from subscribe.models import Subscribe
from subscribe.forms import SubscribeForm
from django.urls import reverse

# Create your views here.
def subscribe(req):
	subsForm = SubscribeForm()
	ctx = {}
	ctx["form"] = subsForm
	if req.POST:
		subsForm = SubscribeForm(req.POST)
		ctx["form"] = subsForm
		subsForm.save()
		# if subsForm.is_valid():
		# 	print("valid form")
		# 	ctx["form"] = subsForm
		# 	fname = subsForm.cleaned_data["first_name"]
		# 	lname = subsForm.cleaned_data["last_name"]
		# 	email = subsForm.cleaned_data["email"]
		# 	subs = Subscribe(first_name=fname, last_name=lname, email=email)
		# 	subs.save()
		return redirect(reverse("u_tnx"))
		#else:
		#	print("invalidd: ")
	return render(req, 'subscribe/subscribe.html', ctx)

def tnx(req):
	ctx = {}
	return render(req, "subscribe/thanks.html", ctx)