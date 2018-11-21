from django.shortcuts import render
from django.http import HttpResponse
from mystore.models import City, Store, Image

def index(request):
    citys = City.objects.all()
    stores = Store.objects.all()
    context = {'citys': citys, 'stores': stores}
    return render(request, 'mystore/index.html', context)
