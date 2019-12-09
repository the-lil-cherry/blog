from django.shortcuts import render

# Create your views here.
def home(request):
    nome = 'Anna'
    lista = ['Matheus', 'Murilo', 'Nathally', 'Giovana' ]
    contexto = {
        'nome':nome,
        'publicacao':lista
    }
    return render(request, 'home.html', contexto)
