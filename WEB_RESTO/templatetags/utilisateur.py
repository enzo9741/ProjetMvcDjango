from django import template

register = template.Library()

@register.simple_tag
def getUtilisateurByMailU(mail, lesUtilisateurs):
    utilsateur = lesUtilisateurs.filter(mailU=mail)[0]
    return utilsateur