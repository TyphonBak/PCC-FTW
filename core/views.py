from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')

def cadastro_coordenador(request):
    return render(request, 'cadastro_coordenador.html')

def cadastro_aluno(request):
    return render(request, 'cadastro_aluno.html')

def cadastro_professor(request):
    return render(request, 'cadastro_professor.html')

def mensagem_nova(request):
    return render(request, 'mensagem_nova.html')

def mensagem_detalhe(request):
    return render(request, 'mensagem_detalhe.html')

def mensagens_enviadas(request):
    return render(request, 'mensagens_enviadas.html')

def mensagens_recebidas(request):
    return render(request, 'mensagens_recebidas.html')

def mensagens_rascunhos(request):
    return render(request, 'mensagens_rascunhos.html')

def painel_aluno(request):
    return render(request, 'painel_aluno.html')

def matricula_aluno(request):
    return render(request, 'matricula_aluno.html')

def matricular(request):
    return render(request, "matricular.html")

def disciplinas_matricula(request):
    return render(request, "disciplinas_matricula.html")

def boletim_index(request):
    return render(request, 'aluno_boletim.html')

def boletim_detalhe(request):
    return render(request, 'aluno_boletim_detalhe.html')

