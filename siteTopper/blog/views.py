from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Piada

def cadastro(request):
    if(request.method == 'POST'):
        inputs = request.POST
        p = Piada()
        p.titulo = inputs['titulo']
        p.conteudo = inputs['conteudo']
        p.categoria = inputs['categoria']
        p.save()
        return redirect('blog:index')
    context = ""
    template = 'cadastro_piada.html'
    return render(request, template, None)

def index(request):
    result = Piada.objects.all()
    for r in result:
        print(r.titulo)
    perdi = [{'titulo': "abacaxi"}, {'titulo': "teste"}, {'titulo': "carro"}, {'titulo': "super"}]
    context = {'piadas': perdi}
    template = 'index.html'
    return render(request, template, context)
