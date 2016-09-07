from .models import Bicicleta
from django.shortcuts import render, get_object_or_404
from .forms import BicicletaForm
from django.shortcuts import redirect


def listar(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, 'bicicletas/listar.html', {'bicicletasList': bicicletas})


def bicicleta_detail(request, pk):
    bicicleta = get_object_or_404(Bicicleta, pk=pk)
    return render(request, 'bicicletas/bicicleta_detail.html', {'bicicleta': bicicleta})


def bicicleta_new(request):
    if request.method == "POST":
        form = BicicletaForm(request.POST)
        if form.is_valid():
            bicicleta = form.save(commit=False)
            bicicleta.save()
            return redirect('listar')
    else:
        form = BicicletaForm()
    return render(request, 'bicicletas/bicicleta_edit.html', {'form': form})


def bicicleta_edit(request, pk):
    bicicleta = get_object_or_404(Bicicleta, pk=pk)
    if request.method == "POST":
        form = BicicletaForm(request.POST, instance=bicicleta)
        if form.is_valid():
            bicicleta = form.save(commit=False)
            bicicleta.save()
            return redirect('listar')
    else:
        form = BicicletaForm(instance=bicicleta)
    return render(request, 'bicicletas/bicicleta_edit.html', {'form': form})


def bicicleta_delete(request, id):
    Bicicleta.objects.get(pk=id).delete()
    return redirect('listar')