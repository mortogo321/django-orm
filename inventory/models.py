from django.db import models

from .abstracts import BaseModel


class Brand(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Category(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name


class Product(BaseModel):
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    is_active = models.BooleanField(default=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Stock(BaseModel):
    units = models.BigIntegerField()

    product = models.OneToOneField(Product, on_delete=models.CASCADE)
