from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static#estas dos lineas son para la ultima parte y poder cargar las imagenes
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^store/', include('store.urls', namespace='store')),# si queremos queremos regresar a un punto anterir quitar el namespace
    #url(r'^$', include('store.urls', namespace='store')),# si queremos queremos regresar a un punto anterir quitar el namespace
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', 'django.contrib.auth.views.login', name='login'),# name='my_login'), # si quiero uar el que veiene por dejecto en django dejar esto asi checjear en la views log_rquired
)
#el sistema de cuentas es independiente del la adminsitracion de la tienda quiza hasta poria tner una app solo para eso por ahora solo concentrarse en el funcionamienteo
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
