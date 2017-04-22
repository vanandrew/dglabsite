from django.shortcuts import render
from django.http import JsonResponse
from .models import news_item, lab_member, research, publication

# homepage
def home_page(request):
    # get all news items
    query_news_items = news_item.objects.all().order_by('date')
    return render(request, 'dlabsite/index.html', {'query_news_items': query_news_items})

# lab member page
def people_page(request):
    # Get all lab members
    query_lab_members = lab_member.objects.all().order_by('last_name')
    return render(request, 'dlabsite/people.html', {'query_lab_members': query_lab_members})

# research
def research_page(request):
    query_research = research.objects.all()
    return render(request, 'dlabsite/research.html', {'query_research': query_research})

# publications
def publications_page(request):
    query_publications = publication.objects.all().order_by('idx')
    return render(request, 'dlabsite/publications.html', {'query_publications': query_publications})

# resources
def resources_page(request):
    return render(request, 'dlabsite/resources.html')

# opportunities
def opportunities_page(request):
    return render(request, 'dlabsite/opportunities.html')

# contact
def contact_page(request):
    return render(request, 'dlabsite/contact.html')
