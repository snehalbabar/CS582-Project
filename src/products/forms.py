from django import forms

from .models import product

class ProductForm(forms.ModelForm):
    class Meta:
        model = product
        fields = [
            'title',
            'decs',
            'price'
        ]


class RawProductForm(forms.Form):
    title = forms.CharField()
    decs  = forms.CharField()
    price = forms.DecimalField()