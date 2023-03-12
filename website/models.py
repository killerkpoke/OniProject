from django.db import models
from django import forms


class Category(models.Model):
    cat_name = models.CharField(max_length=100, blank=True)
    cat_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.cat_name

    class Meta:
        ordering = ('cat_name', )


class Product(models.Model):
    prod_name = models.CharField(max_length=300, blank=True)
    prod_description = models.TextField(blank=True)
    prod_quantity = models.DecimalField(
        max_digits=10, decimal_places=1, null=True)
    prod_image = models.ImageField(upload_to='images/')
    prod_price = models.DecimalField(
        max_digits=10, decimal_places=2)

    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.prod_name

    class Meta:
        ordering = ('pk', )


class About(models.Model):
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description

    class Meta:
        ordering = ('pk', )


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    address = forms.CharField(max_length=200, required=True)
    city = forms.CharField(max_length=200, required=True)
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
