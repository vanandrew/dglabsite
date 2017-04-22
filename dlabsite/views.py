from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect
from .models import lab_member, research, publication

# homepage
def home_page(request):
    return render(request, 'dlabsite/index.html')

# lab member page
def people_page(request):
    # Get all lab members
    current_members = lab_member.objects.filter(alumni=False).order_by('last_name')
    past_members = lab_member.objects.filter(alumni=True).order_by('last_name')
    return render(request, 'dlabsite/people.html', {'current_members': current_members, 'past_members': past_members,})

# research
def research_page(request):
    query_research = research.objects.all()
    return render(request, 'dlabsite/research.html', {'query_research': query_research})

# publications
def publications_page(request):
    query_publications = publication.objects.all().order_by('idx')
    return render(request, 'dlabsite/publications.html', {'query_publications': query_publications})

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
