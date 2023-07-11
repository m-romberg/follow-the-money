from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

### Models for Company app

class Rating(models.Model):
    '''Ratings for companies, 1-10'''
    rating = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]
     )

class Classification(models.Model):
    """Classifications for companies"""
    classification = models.CharField(max_length=50)

class Company(models.Model):
    """Company entry"""
    company = models.CharField(max_length=50)
    ranking = models.ForeignKey(Classification, on_delete=models.CASCADE)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)
    parent_company = models.ForeignKey("self",
                                       on_delete=models.CASCADE,
                                       related_name="parent")
    logo = models.CharField(max_length=200)
    founded = models.DateField()
    num_employees = models.PositiveIntegerField()
    revenue = models.IntegerField()


class Brand(models.Model):
    """Brand entry"""
    brand = models.CharField(max_length=50)
    parent_company = models.ForeignKey(Company, on_delete=models.CASCADE)
    logo = models.CharField(max_length=200)

class Shareholder(models.Model):
    """Shareholder data for companies"""
    shareholder = models.ForeignKey(Company,
                                    on_delete=models.CASCADE,
                                    related_name="shareholder")
    child_company = models.ForeignKey(Company,
                                      on_delete=models.CASCADE,
                                      related_name="child_company")
    source = models.CharField(max_length=200)

class Lawsuit(models.Model):
    """Lawsuits against companies"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    date = models.DateField()
    details =  models.CharField(max_length=300)
    source = models.CharField(max_length=200)