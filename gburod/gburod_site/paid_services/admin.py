from django.contrib import admin
from .models import PricePdfDoc


@admin.register(PricePdfDoc)
class PricePdfDocAdmin(admin.ModelAdmin):
    list_display = ('title', 'file_size', 'published', 'publication_date')
    list_editable = ('published',)
    list_filter = ('published', 'publication_date')
    search_fields = ('title',)
    date_hierarchy = 'publication_date'
