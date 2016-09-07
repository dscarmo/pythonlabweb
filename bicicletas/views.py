from .models import Bicicleta
from django.shortcuts import render, get_object_or_404


def listar(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'bicicletas/listar.html', {'bicicletasList': bicicletas})


def bicicleta_detail(request, pk):
    bicicleta = get_object_or_404(Bicicleta, pk=pk)
    return render(request, 'bicicletas/bicicleta_detail.html', {'bicicleta': bicicleta})

