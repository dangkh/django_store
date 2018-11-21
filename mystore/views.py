from django.shortcuts import render
from django.http import HttpResponse
from mystore.models import City, Store, Image
from random import randint

def index(request):

    citys = City.objects.all()
    stores = Store.objects.all()
    city = []
    store = []
    if stores:
      random_index2 = randint(0, stores.count() - 1)
      store = stores[random_index2]
    if citys:
      random_index1 = randint(0, citys.count() - 1)
      city = citys[random_index1]

    context = {'city': city, 'store': store}
    return render(request, 'mystore/index.html', context)
