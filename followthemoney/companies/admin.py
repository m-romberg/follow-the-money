from django.contrib import admin

from .models import Rating, Classification, Company, Shareholder, Brand, Lawsuit
# Register your models here.

admin.site.register(Rating)
admin.site.register(Classification)
admin.site.register(Company)
admin.site.register(Shareholder)
admin.site.register(Brand)
admin.site.register(Lawsuit)