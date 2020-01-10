from django.db import models

class Product(models.Model):
    name = models.CharField("Product Name",max_length = 255)
    description = models.CharField("Description",max_length= 500)
    category = models.CharField("Category Name",max_length=50,default = '')
    create_at = models.DateTimeField("Created Date")
# Create your models here.
