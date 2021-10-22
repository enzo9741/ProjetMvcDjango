from django.shortcuts import render
from WEB_RESTO.models import Resto
from WEB_RESTO.models import Photo

def listRestos(request):
    lesRestos = Resto.objects.all()
    lesPhotos = Photo.objects.all()

    context = {
        "lesRestos": lesRestos,
        "lesPhotos": lesPhotos,
    }
    return render(request, './WEB_RESTO/listRestos.html', context)
