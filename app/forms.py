from cProfile import label
from logging import PlaceHolder
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import views
import datetime
from django_quill.forms import QuillFormField
from django_quill.widgets import QuillWidget

###########Creacion de usuario##########



class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password'}))
    password2 = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar Password', 'class': 'form-control', 'data-toggle': 'password', 'id': 'confirm-password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'image']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
                                 required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'form-control',
                                                                }))
    password = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                    'class': 'form-control',
                                                                    }))
    
    class Meta:
        model = User
        fields = ['username', 'password']


class CategoryForm(forms.ModelForm):
    description = forms.CharField(widget=QuillWidget(attrs={'class': 'form-control ', 'placeholder': 'Description'}), required=False)

    class Meta:
        
        model = Category
        fields = ['image','name', 'slug', 'parent_category', 'date', 'description', 'status', 'meta_title', 'meta_description']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control ', 'placeholder': 'Image'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug'}),
            'parent_category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Parent Category'}),
            'date': forms.DateInput(attrs={'class': 'form-control ,form-control flatpickr', 'placeholder': 'Date'}),
            'status': forms.Select(attrs={'class': 'form-control , form-check-input , form-check form-check-inline', 'placeholder': 'Status'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'meta_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
            'description': forms.CharField(widget=QuillWidget(attrs={'class': 'form-control', 'placeholder': 'Description' })),
        } 

class ProductForm(forms.ModelForm):
    description = forms.CharField(widget=QuillWidget(attrs={'class': 'form-control ', 'placeholder': 'Description'}), required=False)
    class Meta:
        
        model = Product
        fields = ['name','category', 'weigth', 'units','images','price','sale_price','description','meta_title','meta_description','status','in_stock','code','sku']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'category': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Category'}),
            'weigth': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Weight'}),
            'units': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Units'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$0'}),
            'sale_price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '$0'}),
            'meta_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meta Title'}),
            'meta_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meta Description'}),
            'status': forms.Select(attrs={'class': 'form-control , form-check-input , form-check form-check-inline', 'placeholder': 'Status'}),
            'in_stock': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'In Stock'}),
            'description': forms.CharField(widget=QuillWidget(attrs={'class': 'form-control' , 'placeholder': 'Description' })),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'sku': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU'}),
            'images' : forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Images'}),

        }

class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2','image'] 
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'image': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}), 
        }