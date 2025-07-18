from django import forms
from .models import Supplier,Product
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
    
    
   
    
    