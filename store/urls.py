from django.conf.urls import patterns, url
from store import views

urlpatterns = patterns('',
    url(r'^$', views.listProducts2, name='listProducts'),#se supone q esto termina asi store/ lo cual en las url de abajo no e necesita poner /product/ solo product/
    url(r'^product/(?P<product_id>\d+)/$', views.detailProduct, name='detailProduct'),#/store/product/2/
    url(r'^order/(?P<purchaseorder_id>\d+)/$', views.detailPurchaseOrder, name='detailPurchaseOrder'),#/store/order/2/
    url(r'^addproduct/$', views.addProduct, name='addProduct'),
    url(r'^destaddproduct/$', views.destAddProduct, name='destAddProduct'),
    url(r'^carrito/$', views.carrito, name='carrito'),
    url(r'^process/$', views.destLogin, name='destLogin'),
    url(r'^logout/$', views.logoutView, name='logout'),
    url(r'^signup/$', views.signUp, name='signUp'),
    url(r'^destSignUp/$', views.destSignUp, name='destSignUp'),
    url(r'^user/(?P<user_id>\d+)/$', views.perfil, name='perfil'),#/store/product/2/
    url(r'^coment/$', views.destComent, name='destComent'),
    url(r'^carrito/$', views.carrito, name='carrito'),
)
