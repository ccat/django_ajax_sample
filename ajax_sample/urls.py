from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns("",
    url(r"^$", sampleView,name="ajax_ample_view"),
)
