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
        
   
   
   
   
    """
    fields = ['product_name','category','supplier','quantity','threshold','expiry_date']
     name = forms.CharField(label="Product Name:"max_length = 50)
    CHOICES = [
        ('medicne',"Medicne"),
        ('cosmetic','Cosmetic')
    ]
    category = forms.ChoiceField(label = "Choose type of product"choices=[CHOICES])
    
    quantity = forms.IntegerField(label="Quantity")
    threshold = forms.IntegerField(label="Minimum quntity")
    exp = forms.DateField(label = "Expiry Date")
    """
   
    
    