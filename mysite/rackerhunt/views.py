#Create your views here.
from django.template import Context, loader
from django.shortcuts import render_to_response, get_object_or_404
from rackerhunt.models import Jobs, github_results, user_details
from django.http import HttpResponse
from django.http import Http404
#from /Users/donn6386/Downloads/rackerladies/mysite 
import pullData, user_details1
 
def index(request): 
    job_list = Jobs.objects.all().order_by('-id')[:5]
    return render_to_response('rackerhunt/index.html', {'job_list': job_list}) 
 
def detail(request, jobs_id):
    #p = get_object_or_404(Jobs, pk=jobs_id)
    job_list = Jobs.objects.all().order_by('-id')[:5]
    pullData.github_results(jobs_id)
    result_list = github_results.objects.all().order_by('-id')[:5]
    return render_to_response('rackerhunt/detail.html', {'result_list': result_list})
    #return HttpResponse("You're looking at job %s." % jobs_id)

def results(request, jobs_id):
    user_details1.user_details(jobs_id)
    user = user_details.objects.all().order_by('-id')[:5]
    return render_to_response('rackerhunt/results.html', {'user': user})
    #return HttpResponse("You're looking at the results of job %s." % jobs_id)

def vote(request, jobs_id):
    return HttpResponse("You're voting on poll %s." % jobs_id)
