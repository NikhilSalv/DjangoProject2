from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def index(request):
    return HttpResponse("hello again")

@csrf_exempt

def job_list(request):
    if request.method == "GET":
        # result = []
        
        # jobs = Job.objects.all()

        # for job in jobs:
        #     data = {
        #         "company" : job.company,
        #         "description" : job.description
        #     }
        #     result.append(data)

        # return HttpResponse(result)

        jobs = Job.objects.all()

        return render(request,'portfolio/index.html',{"jobs":jobs})
    
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        company = data['company']
        description = data['description']

        job = Job(company = company, description = description)
        job.save()

        return HttpResponse("company added successfully ")
    

    if request.method == "DELETE":
        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)
        company = data['company']

        job = Job.objects.filter(company = company).delete()
        # job.save()

        return HttpResponse("company deleted successfully ")


