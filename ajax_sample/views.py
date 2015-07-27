from django.http import HttpResponse
from django.shortcuts import render_to_response, render

from django.utils.encoding import force_text
from django.utils.html import escape

def inputAjaxView(request):
    return HttpResponse(escape(force_text(request.POST.get("echo"))))

def sampleView(request):
    return render(request, 'ajax_sample/normal.html', {})
