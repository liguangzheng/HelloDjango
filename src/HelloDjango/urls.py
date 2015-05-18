# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from views import nothings
from TestOne.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
    ('^$', nothings),
    ('^helloworld$', helloWorld),
    ('^showtime$', showTime),
    (r'^time/plus/(\d{1,3})/$', showPlusTime),
    (r'^admin/', include(admin.site.urls)),
)
