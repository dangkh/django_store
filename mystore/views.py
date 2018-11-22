from django.shortcuts import render, redirect
from django.http import HttpResponse
from mystore.models import City, Store, Image
from random import randint
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

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


def register(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('/')
    else:
      form = UserCreationForm()

      args = {'form': form}
      return render(request, 'mystore/register.html', args)


def user_detail(request):
    arg = {'user': request.user}
    return render(request, 'mystore/user_detail.html', arg)

def user_edit_detail(request):
    if request.method == 'POST':
      form = UserChangeForm(request.POST, instance = request.user)
      if form.is_valid():
        form.save()
        return redirect('profile')
    else:
      form = UserChangeForm(instance = request.user)
      args = {'form': form}
      return render(request, 'mystore/edit_detail.html', args)
