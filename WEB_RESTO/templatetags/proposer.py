from django import template

register = template.Library()

@register.simple_tag
def getProposerByIdR(id, proposer):
    cuisineProposer = proposer.filter(idR=id)
    return cuisineProposer