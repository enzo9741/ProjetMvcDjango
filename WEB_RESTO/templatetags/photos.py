from django import template

register = template.Library()

@register.simple_tag
def getUnePhotoByIdR(id, lesPhotos):
    photo = lesPhotos.filter(idR=id)[0]
    return photo.cheminP

@register.simple_tag
def getPhotosByIdR(id, lesPhotos):
    photos = lesPhotos.filter(idR=id)
    return photos