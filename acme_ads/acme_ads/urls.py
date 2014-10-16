from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    #Ad App Links
    url(r'^$', 'ads.views.home', name='home'),
    url(r'^ads/create/$', 'ads.views.create_ad', name='create_ad'),
    url(r'^ads/$', 'ads.views.ad_list', name='ad_list'),
    url(r'^ads/(?P<id>\d+)/$', 'ads.views.ad_detail', name='ad_detail'),
    url(r'^ads/(?P<id>\d+)/connect/$', 'ads.views.connect_newspaper', name='connect_newspaper'),

    #Newspaper App Links
    url(r'^newspapers/create/$', 'newspapers.views.create_newspaper', name='create_newspaper'),
    url(r'^newspapers/(?P<id>\d+)/$', 'newspapers.views.newspaper_detail', name='newspaper_detail'),
    url(r'^newspapers/$', 'newspapers.views.newspaper_list', name='newspaper_list'),
)
