from django.db import models

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
