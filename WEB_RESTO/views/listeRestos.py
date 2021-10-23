from django.shortcuts import render
from WEB_RESTO.models import *

def listRestos(request):
    lesRestos = Resto.objects.all()
    lesPhotos = Photo.objects.all()
    proposer = Proposer.objects.all()
    lesTypeCuisine = Typecuisine.objects.all()

    context = {
        "lesRestos": lesRestos,
        "lesPhotos": lesPhotos,
        "proposer": proposer,
        "lesTypeCuisine": lesTypeCuisine,
    }
    return render(request, './WEB_RESTO/listRestos.html', context)
