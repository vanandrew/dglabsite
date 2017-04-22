from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'dlabsite'
urlpatterns = [
    url(r'^$', views.home_page, name='homepage'),
    url(r'^lab_members', views.people_page, name='people'),
    url(r'^research', views.research_page, name='research'),
    url(r'^publications', views.publications_page, name='publications'),
    url(r'^data', views.data_page, name='data'),
    url(r'^software', views.software_page, name='software'),
    url(r'^wiki', views.wiki_page, name='wiki'),
    url(r'^participate', views.participate_page, name='participate'),
    url(r'^careers', views.careers_page, name='careers'),
    url(r'^contact', views.contact_page, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
