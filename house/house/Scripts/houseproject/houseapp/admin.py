from django.contrib import admin
from.models import Category,Property,Shortlist

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','description']
admin.site.register(Category,CategoryAdmin)

class PropertyAdmin(admin.ModelAdmin):
    list_display=['id','owner_name','price','bhk','contact','city','address','category']
admin.site.register(Property,PropertyAdmin)


admin.site.register(Shortlist)
