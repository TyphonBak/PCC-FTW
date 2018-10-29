from django.urls import path
from core.views import *

urlpatterns = [
    path('', login, name='login'),
    path('index/', index, name='index'),
    path('cadastro/coordenador', cadastro_coordenador, name='cadastro_coordenador'),
    path('cadastro/aluno', cadastro_aluno, name='cadastro_aluno'),
    path('cadastro/professor', cadastro_professor, name='cadastro_professor'),
    path('mensagem/novo', mensagem_nova, name='mensagem_nova'),
    path('mensagem/detalhe', mensagem_detalhe, name='mensagem_detalhe'),
    path('mensagem/enviadas', mensagens_enviadas, name='mensagens_enviadas'),
    path('mensagem/recebidas', mensagens_recebidas, name='mensagens_recebidas'),
    path('mensagem/rascunhos', mensagens_rascunhos, name='mensagens_rascunhos'),
    path('mensagem/', painel_aluno, name='painel_aluno'),
    path('disciplinas/matricula', disciplinas_matricula, name='disciplinas_matricula'),
    path('matricular/', matricular, name='matricular'),
]
