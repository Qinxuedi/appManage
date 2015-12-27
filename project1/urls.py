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
    (r'^classify/(.*?)/(.*?)/$',classify),
    (r'^rank/(.*?)/$',rank),
    (r'^my/$',my),
    (r'^today/$',today),
    (r'^today/2015-11-6/$',oneday),
<<<<<<< HEAD
    (r'^login/$',login),
=======
    (r'^login/$',logins),
>>>>>>> G
    (r'^register/$',register),
    (r'^logout/$',logout),
    (r'^change_password/$',change_password),
    (r'^search_result/$',search_result),
<<<<<<< HEAD
    (r'^search_comment/$',search_comment),
    (r'^introduction/',introduction_app),
    (r'^get_page/',get_page),
    (r'^get_platform_init/',get_platform_init),
=======
    (r'^search_comment/(.*?)/(.*?)/$',search_comment),
    (r'^introduction/',introduction_app),
    (r'^get_page/',get_page),
>>>>>>> G
    #(r'^get_app/',get_app),
    url(r'^admin/', include(admin.site.urls)),
    (r'^s/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':'app/templates' }),
)
urlpatterns += staticfiles_urlpatterns()