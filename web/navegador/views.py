#from django.views.generic import TemplateView

#class Main(TemplateView):
    #template_name = "about.html"
    
from django.http import HttpResponse

def index(request):
    return HttpResponse("FOOBAR")

def emisor(request):
    return HttpResponse("EMISOR")

def ayuda(request):
    return HttpResponse("AYUDA")
