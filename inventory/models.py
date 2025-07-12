from django.db import models
from django.core.validators import MinValueValidator
from django.utils.text import slugify
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=25)
    CATEGORY_CHOICES = [('medicine','Medicine'),('cosmetic','Cosmetic')]
    category = models.CharField(max_length = 10,choices=CATEGORY_CHOICES)
    quantity = models.IntegerField(validators=[MinValueValidator(10)])
    threshold = models.IntegerField()
    expiry_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default = "", null = False,db_index=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product_name} {self.category} {self.quantity}"
    
class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length = 10)
    email = models.EmailField()
    slug = models.SlugField(default ="",null = False,db_index= True)
    products = models.ManyToManyField(Product)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.supplier_name)
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.supplier_name} {self.email} {self.phone_no}"

