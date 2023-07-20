from django.shortcuts import redirect
# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.template import loader

job_titles = [
        "job1 title",
        "job2 title",
        "job3 title",
        ]
job_descs = [
        "job1 decription",
        "job2 desc",
        "job3 dessssk"
        ]


# Create your views here.
def hello(req):
    template = loader.get_template("hello.html")
    ctx = {}
    return HttpResponse(template.render(ctx, req))


def jobs(req):
    html = "<ul>"
    for title in job_titles:
        job_id = job_titles.index(title)
        url = reverse('job_details', args=(job_id,))
        # html += f"<li><a href='job/{job_id}'>{title}</a></li>"
        html += f"<li><a href='{url}'>{title}</a></li>"
    html += "</ul>"
    return HttpResponse(html)


def job_details(req, id):
    try:
        if id == 100:
            # eturn redirect("/jobs")
            return redirect(reverse('jobs_home'))
        html_return = f"<h1>title: {job_titles[id]}</h1>desc: {job_descs[id] }<h3></h3>"
        return HttpResponse(html_return)
    except:
        return HttpResponseNotFound("Not found")
