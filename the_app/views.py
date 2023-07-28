from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# from django.urls import reverse
# from django.template import loader

from .models import JobPost


# Create your views here.

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
    print('in view.jobs: ', jobs)
    return render(req, 'the_app/jobs-list.html', ctx)


def job_details(req, id):
    try:
        # html_return = f"<h1>title: {job_titles[id]}</h1> <h3> desc: {job_descs[id]}</h3>"
        # return HttpResponse(html_return)
        # ctx = {"job_title": job_titles[id],"job_desc": job_descs[id]}
        job = JobPost.objects.get(id=id)
        print(f"job {job.id} : {job}")
        ctx = {"job": job}
        return render(req, 'the_app/job-details.html', ctx)
    except Exception as e:
        print(e)
        return HttpResponseNotFound("Not found")
    
    
