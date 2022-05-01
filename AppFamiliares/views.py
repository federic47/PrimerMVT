from django.shortcuts import render,redirect

from .models import Familiar


def list_familiar(request):
    familiares = Familiar.objects.all()
    context = {'familiares':familiares}
    return render(request, 'index.html', context)


def create_familiar(request):
    numeroDeFamiliar = request.POST["numeroDeFamiliar"]
    nombreYapellido = request.POST["nombreYapellido"]
    fechaNacimiento = request.POST["fechaNacimiento"]
    familiar = Familiar(numeroDeFamiliar=numeroDeFamiliar,nombreYapellido=nombreYapellido,fechaNacimiento =fechaNacimiento)
    familiar.save()
    return redirect('/familiar/')
