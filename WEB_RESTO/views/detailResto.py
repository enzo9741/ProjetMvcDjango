from django.shortcuts import render, redirect
from WEB_RESTO.models import *

def detailResto(request, id):
    resto = Resto.objects.all().get(idR=id)
    proposer = Proposer.objects.all().filter(idR=id)
    lesPhotos = Photo.objects.all().filter(idR=id)
    lesCritiques = Critiquer.objects.all().filter(idR=id)
    lesUtilisateurs = Utilisateur.objects.all()

    context = {
        "idR": id,
        "resto": resto,
        "lesPhotos": lesPhotos,
        "proposer": proposer,
        "lesCritiques": lesCritiques,
        "lesUtilisateurs": lesUtilisateurs,
    }
    return render(request, './WEB_RESTO/detailResto.html', context)
