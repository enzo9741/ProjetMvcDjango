from django import template

register = template.Library()

@register.simple_tag
def getPhotoByIdR(id, lesPhotos):
    photo = lesPhotos.filter(idR=id)[0]
    return photo.cheminP