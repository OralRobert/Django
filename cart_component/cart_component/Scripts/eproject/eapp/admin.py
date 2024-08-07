from django.contrib import admin
from .models import Category,Product,Cart

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','description']

admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display=['id','p_name','p_price','p_description','category']
admin.site.register(Product,ProductAdmin)

admin.site.register(Cart)
