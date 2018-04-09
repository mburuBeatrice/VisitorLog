from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$', views.index, name= 'index'),
    url(r'^create/$', views.create, name='create'),
    url(r'^(?P<id>\d+)/$',views.detail,name='detail'),
    url(r'^(?P<id>\d+)/update$',views.update,name='update'),
    url(r'^(?P<id>\d+)/delete$',views.delete,name='delete'),
   
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)