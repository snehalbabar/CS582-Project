from django import forms

from .models import product

class ProductForm(forms.ModelForm):
    title = forms.CharField( widget=forms.Textarea(attrs={
                                "placeholder":"enter title",
                            }))
    email =  forms.EmailField()
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
    class Meta:
        model = product
        fields = [
            'title',
            'decs',
            'price'
        ]
    
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if "abc" in title :
            return title
        else:
            raise forms.ValidationError("this is not vaild email")
    
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        if not email.endswith('edu') :
            raise forms.ValidationError("this is not vaild title")
        return email
            


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