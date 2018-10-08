from django.db import models

# Create your models here.

class asinDetail(models.Model):
    asin = models.CharField(max_length=100, blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
	    return self.asin


class newProductDetail(models.Model):
    asin = models.CharField(max_length=10000, blank=True, null=True)
    title = models.CharField(max_length=1000,blank=True, null=True)
    bp1 = models.CharField(max_length=10000, blank=True, null=True)
    bp2 = models.CharField(max_length=10000, blank=True, null=True)
    bp3 = models.CharField(max_length=10000, blank=True, null=True)
    bp4 = models.CharField(max_length=10000, blank=True, null=True)
    bp5 = models.CharField(max_length=10000, blank=True, null=True)
    bp6 = models.CharField(max_length=10000, blank=True, null=True)
    bp7 = models.CharField(max_length=10000, blank=True, null=True)
    bp8 = models.CharField(max_length=10000, blank=True, null=True)
    comments = models.CharField(max_length=10000, blank=True, null=True)


    def __str__(self):
	    return self.asin


class oldProductDetail(models.Model):
    asin = models.CharField(max_length=10000, blank=True, null=True)
    current_Title = models.CharField(max_length=1000,blank=True, null=True)
    revised_Title = models.CharField(max_length=1000,blank=True, null=True)


    def __str__(self):
	    return self.asin
