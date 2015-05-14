from django.conf.urls import patterns, include, url
from views import nothings
from TestOne.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns("",
    ('^$', nothings),
    ('^helloworld$', helloWorld),
    ('^showtime$', showTime),
    (r'^time/plus/(\d{1,3})/$', showPlusTime),
)
