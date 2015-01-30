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

class Carrito(models.Model):#los precios del carrito open se deben actulizar constanmente, si esta closed no actualizar ya esta en orde por tanto solo falta el pago, deberia haber un tiempor maximo de espera
    products = models.ManyToManyField(Product, through='Condition', through_fields=('carrito', 'producto'))
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default = 0)
    date = models.DateTimeField("date when generate")#no deberia haber fecha ya que no importa cuando es creado puede haber un carrito muy antiguo con un item, el precio no debe anternese por que si la promcion no esta activa ya no vale corregir
    user = models.ForeignKey(User)
    #status = models.CharField(max_length=10, default="open")#open or closed aunque deberia ser solo true o false
    status = models.CharField(max_length=6, default="open")#open or closed aunque deberia ser solo true o false
    def actualizarCarrito(self):
        conditions = Condition.objects.filter(carrito=self)
        for con in conditions:
            con.actualizarPrice()
        self.calculateTotal()
    def calculateTotal(self):#se debe hacer la llamda a esta funcion constamente los precios deben actualizarse,pero debe acutualozrse el precio con el especil price del producto
        productos = self.products.all()
        acum = 0
        for p in productos:
            condit = Condition.objects.get(carrito=self, producto=p)
            acum += condit.price*condit.cantidad
        self.total_price = acum
        return self.total_price
    def __unicode__(self):
        return u"%s" % self.id

class Order(models.Model):
    carrito = models.ForeignKey(Carrito)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, default = 0)
    status = models.CharField(max_length=100)
    date = models.DateTimeField("date when generate")
    voucher = models.IntegerField(default = 0)
    user = models.ForeignKey(User)
    direccion = models.CharField(max_length=300)
    def totalPrice(self):
        total_price = carrito.total_price
        return self.total_price
    def closeCarrito(self):
        carrito.status = "closed"
        #asignar un nuevo carrito al usuario, no se si sea buena idea hacer esto aqui, pero es facil de hacer en otro lado, por ahora se hara asi
        
        
    def __unicode__(self):
        return u"%s" % self.id

class Condition(models.Model):
    producto = models.ForeignKey(Product)
    carrito = models.ForeignKey(Carrito)
    cantidad = models.IntegerField(default = 1)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)
    def calculateTotal(self):
        return self.price * self.cantidad
    def actualizarPrice(self):
        if(producto.special_price != 0):
            price = producto.special_price
        else:
            price = producto.price
        return price

class coment(models.Model):
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    coment = models.CharField(max_length=1000)
    rank = models.IntegerField(default = 0)
    date = models.DateTimeField("date when comented")
    def __unicode__(self):
        return u"%s" % self.id


# Create your models here.
