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
    title = forms.CharField(label=" ", widget=forms.Textarea(attrs={
                                "placeholder":"enter title",
                            }
                                                  ))
    decs  = forms.CharField(required=False,
                            widget=forms.Textarea(attrs={
                                "placeholder":"enter decsription",
                                "class":"new-class",
                                "id":"my_id",
                                "rows":20,
                                "cols":100,
                            }
                                                  ))
    price = forms.DecimalField(initial=0.99)