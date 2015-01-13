from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader
from store.models import Product, PurchaseOrder
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def listProducts(request):
    #esta vista mostrara los ultims productos agregados a la tienda
    #debido a que aun nle he puto fechas a os productos se ordenaran por precio
    if(request.user.is_authenticated()):
        latest_product_list = Product.objects.order_by('-price')[:5]
    else:
        latest_product_list = Product.objects.order_by('-price')[:2]
    #template = loader.get_template('store/listProducts.html')
    #context = RequestContext(request, {
    #    'latest_product_list': latest_product_list,
    #})
    #return HttpResponse(template.render(context))
    #---------------------------------- Primera forma
    #output = ', '.join([p.nombre for p in latest_product_list])
    #return HttpResponse(output)
    #other way
    context = {'latest_product_list': latest_product_list}
    return render(request, 'store/listProducts.html', context)

def listProducts2(request):
    if(request.user.is_authenticated()):
        latest_product_list = Product.objects.order_by('-price')[:5]
    else:
        latest_product_list = Product.objects.order_by('-price')[:2]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'store/listProducts2.html', context)
def detailProduct(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404
    return render(request, 'store/detailProduct.html', {'product': product})
    #return HttpResponse("Estas viendo el producto %s." % product_id)

def detailPurchaseOrder(request, purchaseorder_id):
    order = get_object_or_404(PurchaseOrder, pk=purchaseorder_id)
    return render(request, 'store/detailPurchaseOrder.html', {'order': order})
    #response = "Estas viendo la orden de compra %s"
    #return HttpResponse(response % purchaseorder_id)
# Create your views here.
@login_required# no se usa parametros para usar el que vene por defecto en django
def addProduct(request):
    if request.user.is_authenticated():
        if request.user.is_superuser:
            return render(request, 'store/addProduct.html')
        else:
            return render(request, 'store/signUp.html')#deberia sr una vista que te indique de que no eres admin

def destAddProduct(request):
    p = Product(nombre=request.POST['nombre'], marca=request.POST['marca'], description=request.POST['descripcion'], spec=request.POST['especificaciones'], price=request.POST['precio'], special_price=request.POST['precioEspecial'], rank=request.POST['valoracion'], stock=request.POST['stock'], product_type=request.POST['tipo'])
    p.save()
    #deberia ir a la pagina de detalle del producto recientemente creado y no a la lista de los produtos, probar por ahora la lista de los productos
    #return HttpResponseRedirect(reverse('store:listProducts'))
    return HttpResponseRedirect(reverse('store:detailProduct', args=(p.id,)))

#@login_required(login_url='/accounts/login/$')
@login_required# no se usa parametros para usar el que vene por defecto en django
def carrito(request):
    latest_product_list = Product.objects.order_by('nombre')[:5]
    context = {'latest_product_list': latest_product_list}
    return render(request, 'store/listProducts.html', context)

def destLogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            #deberia redireccinar a una pagina por ahora mostrare el destLogin.html
            return render(request, 'store/destLogin.html')
        else:
            return render(request, 'store/addProduct.html')
    else:
        return render(request, 'store/signUp.html')

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('store:listProducts'))

def perfil(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'store/user.html', {'user': user})
    
def signUp(request):
    return render(request, 'store/signUp.html')
def destSignUp(request):
    u = User(username=request.POST['username'], first_name=request.POST['firstname'], last_name=request.POST['lastname'], email=request.POST['email'])
    u.set_password(request.POST['password'])
    u.save()
    return HttpResponseRedirect(reverse('store:perfil', args=(u.id,)))
