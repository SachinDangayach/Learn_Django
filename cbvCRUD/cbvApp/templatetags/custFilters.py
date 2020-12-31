from django import template
register=template.Library()

@register.filter(name='myLower')
def custLower(value):
    result=value[0].lower()+'*'+value[1:]
    return result

#register.filter("myLower",custLower)

@register.filter(name='myAppend')
def custAppend(value,arg):
    result=str(arg)+value
    return result
