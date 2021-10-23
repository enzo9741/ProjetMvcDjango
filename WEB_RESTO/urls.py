from django.urls import path
from WEB_RESTO.views.listeRestos import *
from WEB_RESTO.views.detailResto import *

urlpatterns = [
    path('Resto', listRestos, name='resto'),
    path('Resto/Detail/<int:id>', detailResto, name='detail'),
]