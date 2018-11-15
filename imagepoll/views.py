from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Item,Category

# Create your views here.
def index(request):
    template = loader.get_template('imagepoll/index.html')

    context = {
        'categories': Category.objects.all()
    }
    return HttpResponse(template.render(context,request))

def itemdetail(request,item_id):
    try:
        itm = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        itm = None

    template = loader.get_template('imagepoll/itemdetail.html')
    context = {
        'item': itm
    }
    return HttpResponse(template.render(context,request))
