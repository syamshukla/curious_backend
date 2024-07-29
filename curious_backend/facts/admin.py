from django.contrib import admin

# Register your models here.
from .models import Facts
class FactsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['id']}),
        (None,               {'fields': ['body']}),
        (None,               {'fields': ['category']}),
    ]
    list_display = ('id', 'body', 'category')
admin.site.register(Facts, FactsAdmin)


from .models import Categories
class CategoriesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['id']}),
        (None,               {'fields': ['name']}),
    ]
    list_display = ('id', 'name')
admin.site.register(Categories, CategoriesAdmin)
