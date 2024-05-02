from django.shortcuts import render

def index(request):
    dicionario_contexto = {'msgnegrito': "Testando fonte em negrito..."}

    return render(request, 'django/index.html', dicionario_contexto)
