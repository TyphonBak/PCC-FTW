from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def cadastro_coordenador(request):
    return render(request, 'cadastro_coordenador.html')

def mensagem_nova(request):
    return render(request, 'mensagem_nova.html')

def mensagem_detalhe(request):
    return render(request, 'mensagem_detalhe.html')

def mensagens_enviadas(request):
    return render(request, 'mensagens_enviadas.html')

def mensagens_recebidas(request):
    return render(request, 'mensagens_recebidas.html')

def mensagens_rascunho(request):
    return render(request, 'mensagens_rascunhos.html')

def painel_aluno(request):
    return render(request, 'painel_aluno.html')

