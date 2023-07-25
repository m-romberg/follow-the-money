from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


### Models for Company app

DETAILS_DEFAULT = "Additional details currently not available."

class Rating(models.Model):
    '''Ratings for companies, 1-10'''
    rating = models.IntegerField(
        default=5,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ],
        unique=True,
     )
    description =  models.TextField(default="")

    def __str__(self):
        return str(self.rating)

class Classification(models.Model):
    """Classifications for companies"""
    classification = models.CharField(max_length=50)

    def __str__(self):
        return self.classification

class Company(models.Model):
    """Company entry"""
    company = models.CharField(max_length=50)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    parent_company = models.ForeignKey("self",
                                       on_delete=models.CASCADE,
                                       related_name="parent",
                                       default=None,
                                       blank=True,
                                       null=True)
    logo = models.ImageField(max_length = 200,
                             default=None,
                             blank=True,
                             null=True)
    founded = models.DateField()
    num_employees = models.PositiveIntegerField()
    revenue = models.IntegerField()
    details =  models.TextField(default=DETAILS_DEFAULT)
    source = models.URLField(max_length = 200, blank=False, default=None)

    def __str__(self):
        return self.company


class Brand(models.Model):
    """Brand entry"""
    brand = models.CharField(max_length=50)
    parent_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    logo = models.ImageField(max_length = 200,
                             default=None,
                             blank=True,
                             null=True)
    details =  models.TextField(default=DETAILS_DEFAULT)
    source = models.URLField(max_length = 200, blank=False, default=None)

    def __str__(self):
        return self.brand

class Shareholder(models.Model):
    """Shareholder data for companies"""
    shareholder = models.ForeignKey(Company,
                                    on_delete=models.CASCADE,
                                    related_name="shareholder")
    child_company = models.ForeignKey(Company,
                                      on_delete=models.CASCADE,
                                      related_name="child")
    share = models.DecimalField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)],
        max_digits=5,
        decimal_places=2,
        default=0)
    details =  models.TextField(default=DETAILS_DEFAULT)
    source = models.URLField(max_length = 200, blank=False, default=None)

    def __str__(self):
        return f"{self.shareholder}, {self.child_company}"

class Lawsuit(models.Model):
    """Lawsuits against companies"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    details =  models.TextField(default=DETAILS_DEFAULT)
    source = models.URLField(max_length = 200, blank=False, default=None)

    def __str__(self):
        return f"{self.company}, {self.date}"