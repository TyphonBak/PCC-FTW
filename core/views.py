from django.shortcuts import render

def alunoNotas(request):
  return render(request,"consulta_de_notas_frequencia.html")

def alunoBoletim(request):
  return render(request, "base(v.1).html")
                 
  
  
