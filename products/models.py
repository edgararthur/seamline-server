from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    

class Promotion(models.Model):
    description = models.TextField()
    discount = models.FloatField()
    # product_set
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField( max_digits=10, decimal_places=2, validators=[MinValueValidator(0)] )
    category = models.ForeignKey( Category, related_name='products', on_delete=models.PROTECT )
    stock = models.PositiveIntegerField(default=0)
    is_customizable = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    variant_name = models.CharField(max_length=100)
    variant_value = models.CharField(max_length=100)
    additional_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class ProductImage(models.Model):
    product = models.ForeignKey( Product, related_name='images', on_delete=models.CASCADE )
    image = models.ImageField(upload_to='products/images')
    alt_text = models.CharField(max_length=100, blank=True)
    is_feature = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Image for {self.product.name}"
