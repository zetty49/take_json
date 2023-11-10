from django.contrib import admin
from app.models import Filters, FiltredData


@admin.register(Filters)
class FiltersAdmin(admin.ModelAdmin):
    list_display = ('f1', 'f2', 'f3', 'f4')

@admin.register(FiltredData)
class FilteredDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_code', 'price', 'image', 'currency', 'qty')
    search_fields = ('name', 'product_code', 'price', 'image', 'currency', 'qty')
    list_filter = ('name', 'product_code', 'price', 'image', 'currency', 'qty')