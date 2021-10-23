from django.shortcuts import render, redirect
from WEB_RESTO.models import *

def detailResto(request, id):
    proposer = Proposer.objects.all()
    lesPhotos = Photo.objects.all()
    resto = Resto.objects.all().get(idR=id)

    context = {
        "idR": id,
        "resto": resto,
        "lesPhotos": lesPhotos,
        "proposer": proposer,
    }
    return render(request, './WEB_RESTO/detailResto.html', context)
