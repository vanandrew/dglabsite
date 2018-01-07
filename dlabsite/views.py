from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .models import (lab_member, publication, job_listing,
    current_study, data_listing, software_listing)
from datetime import datetime
import json
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# homepage
def home_page(request):
    return render(request, 'dlabsite/index.html')

# load surface data
def load_pial_data(request):
    with open(os.path.join(BASE_DIR,'static','dlabsite','js','lh.pial.json'),'r') as datafile:
        data = json.load(datafile);
    with open(os.path.join(BASE_DIR,'static','dlabsite','js','rh.pial.json'),'r') as datafile:
        data2 = json.load(datafile);
    return JsonResponse({'data':data, 'data2':data2})

# lab member page
def people_page(request):
    # Get all lab members
    members = lab_member.objects.all().order_by('last_name')
    return render(request, 'dlabsite/people.html', {'members': members})

# research
def research_page(request):
    return render(request, 'dlabsite/research.html')

# publications
def publications_page(request):
    publications = publication.objects.all().order_by('-date')
    dateobjs = publication.objects.dates('date','year',order='DESC')
    years = [date.year for date in dateobjs]
    return render(request, 'dlabsite/publications.html', {'publications': publications, 'years': years})

# data
def data_page(request):
    data = data_listing.objects.all().order_by('title')
    return render(request, 'dlabsite/data.html', {'data': data})

# software
def software_page(request):
    software = software_listing.objects.all().order_by('title')
    return render(request, 'dlabsite/software.html', {'software': software})

# directions
def directions_page(request):
    return render(request, 'dlabsite/directions.html')

# participate
def participate_page(request):
    currentstudies = current_study.objects.all().order_by('title')
    return render(request, 'dlabsite/participate.html', {'currentstudies': currentstudies})

# careers
def careers_page(request):
    jobpostings = job_listing.objects.all().order_by('-post_date')
    return render(request, 'dlabsite/careers.html', {'jobpostings': jobpostings})

# contact
def contact_page(request):
    return render(request, 'dlabsite/contact.html')
