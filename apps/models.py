from django.db import models


class BlogC(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images')
    category = models.ForeignKey('apps.BlogC', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    blog = models.ForeignKey('apps.Blog', models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey('apps.ProductC', models.CASCADE)
    price = models.PositiveIntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='product_images')

    def __str__(self):
        return self.name


class ProductC(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ProductComment(models.Model):
    product = models.ForeignKey('apps.Product', models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)