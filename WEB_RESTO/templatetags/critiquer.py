from django import template
from django.db.models import Avg

register = template.Library()

@register.simple_tag
def getCritiqueByIdR(id,critiques):
    lesCritiques = critiques.filter(idR=id)
    return lesCritiques

def getMoyenne(id, critiques):
    lesCritiques = critiques.filter(idR=id)
    moyenne = lesCritiques.aggregate(Avg('note')).get('note__avg')

    if(isinstance(moyenne, type(None))):
        moyenne = 0
    else:
        moyenne = round(moyenne)

    return moyenne


@register.simple_tag
def getLikeByIdR(id, critiques):
    like = getMoyenne(id, critiques)
    return range(like)

@register.simple_tag
def getdislikeByIdR(id, critiques):
    dislike = 5 - getMoyenne(id, critiques)
    return range(dislike)