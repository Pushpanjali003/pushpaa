from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name    
    

class Product(models.Model):
    cat_name=models.ForeignKey(Category,on_delete=models.CASCADE)
    pr_image=models.ImageField(upload_to="gallery")
    pr_name=models.CharField(max_length=20)
    pr_price=models.IntegerField(default=0)
    pr_des=models.TextField()

    def __str__(self) -> str:
        return self.pr_name