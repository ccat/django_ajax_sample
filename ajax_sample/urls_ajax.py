from django.conf.urls import patterns, include, url

from views import *

urlpatterns = patterns("",
    url(r"^input/$", inputAjaxView,name="ajax_ample_ajax"),
)
