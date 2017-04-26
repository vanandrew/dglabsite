from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .models import lab_member, research, publication
from datetime import datetime

# homepage
def home_page(request):
    return render(request, 'dlabsite/index.html')

# lab member page
def people_page(request):
    # Get all lab members
    members = lab_member.objects.all().order_by('last_name')
    return render(request, 'dlabsite/people.html', {'members': members})

# research
def research_page(request):
    query_research = research.objects.all()
    return render(request, 'dlabsite/research.html', {'query_research': query_research})

# publications
def publications_page(request):
    publications = publication.objects.all().order_by('date')
    lastfiveyears = [datetime.now().year,datetime.now().year-1,datetime.now().year-2,datetime.now().year-3,datetime.now().year-4]
    return render(request, 'dlabsite/publications.html', {'publications': publications,'lastfiveyears': lastfiveyears})

# data
def data_page(request):
    return render(request, 'dlabsite/data.html')

# software
def software_page(request):
    return render(request, 'dlabsite/software.html')
    
# wiki
def wiki_page(request):
    return HttpResponseRedirect('http://www.wikipedia.org')

# participate
def participate_page(request):
    return render(request, 'dlabsite/participate.html')

# careers
def careers_page(request):
    return render(request, 'dlabsite/careers.html')

# contact
def contact_page(request):
    return render(request, 'dlabsite/contact.html')
