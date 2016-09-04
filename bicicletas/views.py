from django.shortcuts import render
from .models import Bicicleta


def listar(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'bicicletas/listar.html', {'bicicletas': bicicletas})
