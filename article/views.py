from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def basicone(request):
    firststr = "first"
    html = "<html><body>This is %s</body></html>" % firststr
    return HttpResponse(html)