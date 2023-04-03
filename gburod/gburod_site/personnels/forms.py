from django import forms
from django.forms import ModelForm, Textarea

from .models import Rating, Comment


class RatingForm(forms.ModelForm):
    score = forms.IntegerField(
        label='Рейтинг',
        widget=forms.NumberInput(attrs={
            'min': 1,
            'max': 5,
            'step': 1,
            'class': 'form-control'
        })
    )

    class Meta:
        model = Rating
        fields = ('score',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={'rows': 5})
        }
