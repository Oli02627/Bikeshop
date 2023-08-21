from django.contrib import admin
from .models import Category,Brand,Size,Colour,Product
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(Size)

class ProductAdmin(admin.ModelAdmin):
    list_display=('id', 'title','brand','colour','size','price','status')
admin.site.register(Product, ProductAdmin)
