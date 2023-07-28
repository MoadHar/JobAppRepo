from django.shortcuts import render
from .forms import UploadForm, UploadFileForm


# Create your views here.
def upload_image(req):
	if req.method == "POST":
		form = UploadForm(req.POST, req.FILES)
		if form.is_valid():
			form.save()
			saved_object = form.instance
			return render(req, "upload_app/add-image.html", {"form":form, "saved_object": saved_object})
	else:
		form = UploadForm()
		return render(req, "upload_app/add-image.html", {"form":form})


def upload_file(req):
	if req.method == "POST":
		form = UploadFileForm(req.POST, req.FILES)
		if form.is_valid():
			form.save()
			saved_object = form.instance
			return render(req, "upload_app/add-file.html", {"form":form, "saved_object": saved_object})
	else:
		form = UploadFileForm()
		return render(req, "upload_app/add-file.html", {"form":form})