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

    # Добавляем clean_score для валидации рейтинга
    def clean_score(self):
        score = self.cleaned_data.get('score')

        if score is None:
            raise forms.ValidationError('Пожалуйста, поставьте рейтинг.')

        return score

    class Meta:
        model = Rating
        fields = ('score',)


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'comment_email', 'author')
        widgets = {
            'text': Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'comment_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
        }
        # widgets = {
        #     'text': Textarea(attrs={
        #         'rows': 5,
        #     })
        # }
