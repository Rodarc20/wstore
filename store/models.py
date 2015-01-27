from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    nombre = models.CharField(max_length=200)
    marca = models.CharField(max_length=30)
    description = models.CharField(max_length=500)#quiza deba ser mas grande
    spec = models.CharField(max_length=1000)#las especificaciones tambien deberian ser mas grandes
    price = models.DecimalField(max_digits=7, decimal_places=2)
    special_price = models.DecimalField(max_digits=7, decimal_places = 2)
    image = models.ImageField(upload_to='products')# este lo deamos para despues ya que aun no se como trabajare las imagenes o las subire
    rank = models.IntegerField(default=0)
    stock = models.CharField (max_length=30)
    product_type = models.CharField(max_length=30)
    def __unicode__(self):
        return self.nombre

class PurchaseOrder(models.Model):
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=9, decimal_places=2)
    date = models.DateTimeField("date when generate")
    status = models.CharField(max_length=100)
    voucher = models.IntegerField(default = 0)
    user = models.ForeignKey(User)
    direccion = models.CharField(max_length=300)
    def calculateTotal(self):
        productos = self.products.all()
        acum = 0
        for p in productos:
            acum += p.special_price#si el precio especial es digual que cero se debe usar el precio normal agregar eso una vez que funcione esto
        self.total_price = acum
        return self.total_price
    def __unicode__(self):
        return u"%s" % self.id

class coment(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    coment = models.CharField(max_length=1000)
    rank = models.IntegerField(default = 0)
    date = models.DateTimeField("date when comented")
    def __unicode__(self):
        return u"%s" % self.id


# Create your models here.
