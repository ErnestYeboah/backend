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
    