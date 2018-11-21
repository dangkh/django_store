from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class City(models.Model):
    city_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.city_name


class Store(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=200)
    store_address = models.CharField(max_length=200)
    store_description = models.CharField(max_length=400)
    def __str__(self):
        return self.store_name

class Image(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    image = models.ImageField(height_field=500, width_field=500, max_length=100)
    def __str__(self):
        return self.image


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default ='')

def create_profile(sender, **kwargs):
    if kwargs['created']:
      user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender = User)
