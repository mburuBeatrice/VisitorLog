from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    # url(r'^$', views.mainpage, name='main'),
    url(r'^$', views.index, name= 'index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<id>\d+)/$',views.detail,name='detail'),
    url(r'^(?P<id>\d+)/update$',views.update,name='update'),
    url(r'^(?P<id>\d+)/delete$',views.delete,name='delete'),
    url(r'^county$', views.county_index, name= 'county'),
    url(r'^county_create/$', views.county_create, name='county_create'),
    url(r'^(?P<id>\d+)/$',views.county_detail,name='county_detail'),
    url(r'^(?P<id>\d+)/county_update$',views.county_update,name='county_update'),
    url(r'^(?P<id>\d+)/county_delete$',views.county_delete,name='county_delete'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)