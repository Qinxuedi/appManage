from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^$',first),
    (r'^classify/$',classify),
    (r'^classify/(.+)/$',page),
    (r'^rank/$',rank),
    (r'^my/$',my),
    (r'^today/$',today),
    (r'^today/2015-11-6/$',oneday),
    (r'^login/$',login),
    (r'^register/$',register),
    (r'^logout/$',logout),
    (r'^change_password/$',change_password),
    (r'^search_result/$',search_result),
    #(r'^can_not_be_null/$',temp),
    (r'^introduction/(.+)/$',introduction_app),
    (r'^download/(.+)/$',download_app),
    url(r'^admin/', include(admin.site.urls)),
    (r'^s/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':'app/templates' }),
)
urlpatterns += staticfiles_urlpatterns()