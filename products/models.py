from django.db import models

# Create your models here.
class Product(models.Model) :

    CATEGORY_CHOICES = [
        ("clothing", "clothing"),
        ("shoes", "shoes"),
        ("watches", "watches"),
        ("jewelry", "jewelry"),
        ("headwear", "headwear"),
    ]

    productName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES , default="clothing")
    description = models.CharField(max_length=255 )
    thumbnail = models.ImageField(blank=True , null=True)

    def __str__(self):
        return self.productName
    

class Favorite(models.Model) :
        productName = models.CharField(max_length=255)
        price = models.DecimalField(max_digits=10 , decimal_places=2)
        thumbnail = models.URLField(blank=True , null=True)
        date_added = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.productName


class Cart(models.Model) :
   
    productName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    category = models.CharField()
    quantity = models.IntegerField()
    color = models.CharField(max_length=100)
    thumbnail = models.URLField(blank=True , null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # ✅ computed fieldt=0.00) 
    date_added = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-calculate total_price when saving
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)    

    def __str__(self):
        return self.productName    