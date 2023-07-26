from django.shortcuts import render

from subscribe.models import Subscribe

# Create your views here.
def subscribe(req):
	ctx = {}
	if req.POST:
		fname = req.POST["firstname"]
		lname = req.POST["lastname"]
		email = req.POST["email"]
		print("this is a POST method request:", fname, lname, email)
		if email =="" or fname == "" or lname =="":
			ctx["email_empty"] = "email or fname or lname not entered"
		else:
			subsribe = Subscribe(first_name=fname, last_name=lname, email=email)
			subsribe.save()

	return render(req, 'subscribe/subscribe.html', ctx)