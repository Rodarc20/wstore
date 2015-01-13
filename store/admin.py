from django.contrib import admin
from store.models import Product, PurchaseOrder

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'total_price', 'status')

admin.site.register(Product)
admin.site.register(PurchaseOrder, PurchaseOrderAdmin)


# Register your models here.
