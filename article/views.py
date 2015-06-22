from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def basicone(request):
    firststr = "first"
    html = "<html><body>This is %s</body></html>" % firststr
    return HttpResponse(html)

def template_two(request):
    view = "Dmitry"
    t = get_template('mytemplate.html')
    html = t.render(Context({'name':view}))
    return HttpResponse(html)