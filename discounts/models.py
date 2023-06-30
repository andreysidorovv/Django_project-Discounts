from django.db import models

class Discount(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    discount_percentage = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class SpecialOffer(models.Model):
    objects = None
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    discount_percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.title









