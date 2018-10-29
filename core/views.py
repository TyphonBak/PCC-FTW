from django.shortcuts import render, redirect


def perfil_professor(request):
    
    context = {
        'perfil_logado': 'Professor'
    }

    return render(request, 'index.html', context)

def perfil_aluno(request):
    
    context = {
        'perfil_logado': 'Aluno'
    }

    return render(request, 'index.html', context)

def perfil_coordenador(request):
    
    context = {
        'perfil_logado': 'Coordenador'
    }

    return render(request, 'index.html', context)

# Create your views here.
def login(request):
    return render(request, 'login.html')

def index(request, perfil_logado):

    context = {
        'perfil_logado': perfil_logado
    }

    return render(request, 'index.html', context)

def cadastro_coordenador(request):

    context = {
        'perfil_logado': 'Coordenador'
    }

    return render(request, 'cadastro_coordenador.html', context)

def cadastro_aluno(request):

    context = {
        'perfil_logado': 'Coordenador'
    }

    return render(request, 'cadastro_aluno.html', context)

def cadastro_professor(request):

    context = {
        'perfil_logado': 'Coordenador'
    }

    return render(request, 'cadastro_professor.html', context)

def mensagem_nova(request, perfil_logado):

    context = {
        'perfil_logado': perfil_logado
    }

    return render(request, 'mensagem_nova.html', context)

def mensagem_detalhe(request, perfil_logado):

    context = {
        'perfil_logado': perfil_logado
    }

    return render(request, 'mensagem_detalhe.html', context)

def mensagens_enviadas(request, perfil_logado):

    context = {
        'perfil_logado': perfil_logado
    }

    return render(request, 'mensagens_enviadas.html', context)

def mensagens_recebidas(request, perfil_logado):

    context = {
        'perfil_logado': perfil_logado
    }

    return render(request, 'mensagens_recebidas.html', context)

def mensagens_rascunhos(request, perfil_logado):

    context = {
        'perfil_logado': perfil_logado
    }

    return render(request, 'mensagens_rascunhos.html', context)

def painel_mensagem(request, perfil_logado):

    context = {
        'perfil_logado': perfil_logado
    }

    return render(request, 'painel_mensagem.html', context)

def matricula_aluno(request):

    context = {
        'perfil_logado': 'Aluno'
    }

    return render(request, 'matricula_aluno.html', context)

def matricular(request):

    context = {
        'perfil_logado': 'Aluno'
    }

    return render(request, "matricular.html", context)

def disciplinas_matricula(request):

    context = {
        'perfil_logado': 'Aluno'
    }

    return render(request, "disciplinas_matricula.html", context)

def boletim_index(request):

    context = {
        'perfil_logado': 'Aluno'
    }

    return render(request, 'aluno_boletim.html', context)

def boletim_detalhe(request):

    context = {
        'perfil_logado': 'Aluno'
    }

    return render(request, 'aluno_boletim_detalhe.html', context)

def professor_boletim(request):
    
    context = {
        'perfil_logado': 'Professor'
    }

    return render(request, 'professor_boletim.html', context)

def professor_disciplina(request):

    context = {
        'perfil_logado': 'Professor'
    }

    return render(request, 'disciplina_conteudo.html', context)

def aluno_disciplina(request):

    context = {
        'perfil_logado': 'Aluno'
    }

    return render(request, 'disciplina_conteudo.html', context)