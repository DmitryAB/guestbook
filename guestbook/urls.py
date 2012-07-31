from django.conf.urls import patterns, include, url
from guestbook.views import home
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', home),
    # Examples:
    # url(r'^$', 'guestbook.views.home', name='home'),
    # url(r'^guestbook/', include('guestbook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('',
    url(r'^captcha/', include('captcha.urls')),
)
