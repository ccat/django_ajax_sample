from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns("",
    url(r"^input/$", inputView),
    url(r"^$", sampleView),
)
