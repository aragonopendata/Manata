#from django.views.generic import TemplateView

#class Main(TemplateView):
    #template_name = "about.html"
    
from django.http import HttpResponse

def main(request):
    return HttpResponse("FOOBAR")