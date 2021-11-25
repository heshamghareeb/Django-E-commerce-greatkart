from django.db import models
from category.models import Category
# Create your models here.
from django.urls import reverse
class Product(models.Model):
    """Model definition for Product."""
    product_name = models.CharField(max_length = 150, unique=True)
    slug = models.SlugField(max_length = 50, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    modified_date = models.DateField(auto_now=True)
    
    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
        
    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        """Unicode representation of Product."""
        return self.product_name
