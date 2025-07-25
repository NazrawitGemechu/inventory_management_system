from django import forms
from .models import Supplier,Product,SoldProduct
from django.contrib.auth.models import User
"""
class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput,label="confirm password")
    class Meta:
        model = User
        fields = ['username','password','password_confirm']
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data['password']
        password_confirm = cleaned_data['password_confirm']
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Password do not match!")
        return cleaned_data
        """
class ProductForm(forms.ModelForm):
    supplier = forms.ModelMultipleChoiceField(queryset=Supplier.objects.all(), widget = forms.CheckboxSelectMultiple)
    class Meta:
        model = Product
        exclude = ['created_at','slug']
        labels = {
            "product_name": "Product Name",
            "category" : "Choose type of the product",
            "supplier": "Select one or more suppliers",
            "quantity": "Quantity",
            "threshold": "Minimum quantity",
            "expiry_date": "Expiry Date"
        }
        error_messages = {
            "product_name":{
                "required": "Product name must not be empty!",
                "max_length":"Please enter a name shorter than 50 "
            },
            "category":{
                "required": "Category must be selected"
            },
            "supplier":{
                "required": "Choose atleast one supplier"
            },
            "quantity":{
                "required":"Quantity must not be empty"
            },
            "threshold":{
                "required": "Please enter minimum product quantity required"
            },
            "expiry_date":{
                "required": "Please enter Expiry date"
            }
        }
        
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        exclude =['slug']
        error_messages={
            "supplier_name":{
                "required": "Supplier name cannot be empty"
            },
            "phone_no":{
                "required": "Phone number cannot be empty",
                "max_length": "Phone number can not be more than 10 digit"
            },
            "email":{
                "required": "Email address is required",
                "invalid":"Invalid email format"
            }
        }
        labels = {
            "supplier_name": "Supplier Name",
            "phone_no": "Phone number",
            "email": "Email"
        }
    
class SoldProductForm(forms.ModelForm):
    class Meta:
        model = SoldProduct   
        exclude=['sale']
        labels ={
            "product":"Select products sold",
            "quantity":"Select amunt sold"
        }
        error_messages= {
            "required":{
                "product":"Select atleast one product",
                "quantity":"Quantity cannot be empty"
            },
            "invalid":{
                "quantity":"Quantity cannot be negative"
            }
        }
   
    
    