from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
# from django.template import loader

from .models import JobPost


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

tmp_list = [
        "alpha", "beta", "omega"
        ]


class TempClass:
    x = 7314


# Create your views here.
def hello(req):
    # template = loader.get_template("hello.html")
    # template = loader.get_template("the_app/hello.html")
    temp_obj = TempClass
    is_authenticated = True
    ctx = {"name": "Djangow", "first_list": tmp_list, "temp_obj": temp_obj, "age":44,
           "is_authed": is_authenticated
           }
    # return HttpResponse(template.render(ctx, req))
    return render(req, "the_app/hello.html", ctx)


def jobs(req):
    """
    html = "<ul>"
    for title in job_titles:
        job_id = job_titles.index(title)
        url = reverse('job_details', args=(job_id,))
        # html += f"<li><a href='job/{job_id}'>{title}</a></li>"
        html += f"<li><a href='{url}'>{title}</a></li>"
    html += "</ul>"
    return HttpResponse(html)
    """
    jobs = JobPost.objects.all()
    ctx = {"jobs": jobs, "count": len(jobs)}
    return render(req, 'the_app/jobs-list.html', ctx)


def job_details(req, id):
    try:
        if id == 100:
            # eturn redirect("/jobs")
            return redirect(reverse('jobs_home'))
        # html_return = f"<h1>title: {job_titles[id]}</h1> <h3> desc: {job_descs[id]}</h3>"
        # return HttpResponse(html_return)
        # ctx = {"job_title": job_titles[id],"job_desc": job_descs[id]}
        job = JobPost.objects.get(id=id)
        ctx = {"job": job}
        return render(req, 'the_app/job-details.html', ctx)
    except:
        return HttpResponseNotFound("Not found")
    
    
