from django.shortcuts import render

# Create your views here.
def professor_disciplina(request):
    return render(request, "professor_disc.html")