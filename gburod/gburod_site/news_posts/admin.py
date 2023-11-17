from django.contrib import admin
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import News


class NewsAdminForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'content': CKEditorWidget(),
        }


class NewsAdmin(admin.ModelAdmin):
    form = NewsAdminForm


admin.site.register(News, NewsAdmin)
