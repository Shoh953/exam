from django import forms
from .models import Blog, BlogC, Product, ProductC
from django.contrib.auth.models import User


class BlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        BlogC.objects.all(),
        to_field_name='id',
        empty_label=None,
        required=True
    )

    class Meta:
        model = Blog
        exclude = ('created_at',)


class ProductForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        ProductC.objects.all(),
        to_field_name='id',
        empty_label=None,
        required=True
    )

    class Meta:
        model = Blog
        exclude = ('created_at',)