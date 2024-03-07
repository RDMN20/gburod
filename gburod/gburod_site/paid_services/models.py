from django.db import models
from django.template.defaultfilters import filesizeformat
from django.utils import timezone


class PricePdfDoc(models.Model):
    title = models.CharField(max_length=100)
    price_pdf_file = models.FileField(upload_to='price-lists/')
    published = models.BooleanField(default=True)
    publication_date = models.DateTimeField(default=timezone.now)

    class Meta:
        # Указываем порядок сортировки: сначала опубликованные документы,
        # затем по дате публикации
        ordering = ['-published', 'publication_date']
        verbose_name = 'Price PDF Document'
        verbose_name_plural = 'Price PDF Documents'

    def __str__(self):
        return self.title

    def file_size(self):
        return filesizeformat(self.price_pdf_file.size)
