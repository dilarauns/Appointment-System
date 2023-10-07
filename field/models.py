from django.db import models
class Randevu(models.Model):
    tarih = models.CharField(max_length=50)
    numara = models.CharField(max_length=10)
    isim=models.CharField(max_length=50)
    soyisim=models.CharField(max_length=50)





