from django.template import RequestContext, loader
from django.http import HttpResponse

def emisores(request):
    template = loader.get_template('navegador/emisores.html')
    context = RequestContext(request, { })
    return HttpResponse(template.render(context))

def ayudas(request):
    template = loader.get_template('navegador/ayudas.html')
    context = RequestContext(request, { })
    return HttpResponse(template.render(context))

def ayudas_beneficiarios(request):
    template = loader.get_template('navegador/ayudas_beneficiarios.html')
    context = RequestContext(request, { })
    return HttpResponse(template.render(context))
