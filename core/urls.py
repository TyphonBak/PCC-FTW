from django.urls import path, re_path
from core.views import *

urlpatterns = [
    path('', login, name='login'),
    re_path(r'^index/(?P<perfil_logado>\w+)/$', index, name='index'),
    path('cadastro/coordenador', cadastro_coordenador, name='cadastro_coordenador'),
    path('cadastro/aluno', cadastro_aluno, name='cadastro_aluno'),
    path('cadastro/professor', cadastro_professor, name='cadastro_professor'),
    re_path(r'mensagem/(?P<perfil_logado>\w+)/novo$', mensagem_nova, name='mensagem_nova'),
    re_path(r'mensagem/(?P<perfil_logado>\w+)/detalhe$', mensagem_detalhe, name='mensagem_detalhe'),
    re_path(r'mensagem/(?P<perfil_logado>\w+)/enviadas$', mensagens_enviadas, name='mensagens_enviadas'),
    re_path(r'mensagem/(?P<perfil_logado>\w+)/recebidas$', mensagens_recebidas, name='mensagens_recebidas'),
    re_path(r'mensagem/(?P<perfil_logado>\w+)/rascunhos$', mensagens_rascunhos, name='mensagens_rascunhos'),
    re_path(r'^mensagem/(?P<perfil_logado>\w+)$', painel_mensagem, name='painel_mensagem'),
    path('disciplinas/matricula', disciplinas_matricula, name='disciplinas_matricula'),
    path('matricular/', matricular, name='matricular'),
    path('boletim/', boletim_index, name='boletim_index'),
    path('disciplinas/', aluno_disciplina, name='aluno_disciplinas'),
    path('boletim/semestre', boletim_detalhe, name='boletim_detalhe'),
    path('disciplinas/Professor', professor_disciplina, name='professor_disciplina'),
    path('professor/boletim/', professor_boletim, name='professor_boletim'),
    path('professor/', perfil_professor, name='perfil_professor'),
    path('aluno/', perfil_aluno, name='perfil_aluno'),
    path('coordenador/', perfil_coordenador, name='perfil_coordenador'),
]
