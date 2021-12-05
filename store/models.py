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


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager,self).filter(variation_category='color', is_active=True)

    def sizes(self):
                return super(VariationManager,self).filter(variation_category='size', is_active=True)

    
variation_category_choice = (
    ('color','color'),
    ('size','size'),
)
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category = models.CharField(max_length = 150, choices=variation_category_choice)
    variation_value = models.CharField(max_length = 150)
    is_active = models.BooleanField(default=True)
    created_date = models.DateField(auto_now=True)
    
    
    objects = VariationManager()
    class Meta:
        verbose_name = ("Variation")
        verbose_name_plural = ("Variations")

    def __str__(self):
        return self.variation_value


