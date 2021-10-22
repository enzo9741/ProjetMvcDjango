from django.shortcuts import render, redirect

def detailResto(request, idR):
    context = {
        "idR": idR,
    }
    return render(request, './WEB_RESTO/detailResto.html', context)
