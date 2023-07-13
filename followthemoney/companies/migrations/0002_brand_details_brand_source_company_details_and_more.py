# Generated by Django 4.2.3 on 2023-07-13 23:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='details',
            field=models.TextField(default='Additional details currently not available.'),
        ),
        migrations.AddField(
            model_name='brand',
            name='source',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='company',
            name='details',
            field=models.TextField(default='Additional details currently not available.'),
        ),
        migrations.AddField(
            model_name='company',
            name='source',
            field=models.URLField(default=None),
        ),
        migrations.AddField(
            model_name='rating',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='shareholder',
            name='details',
            field=models.TextField(default='Additional details currently not available.'),
        ),
        migrations.AlterField(
            model_name='brand',
            name='logo',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(max_length=200, upload_to=''),
        ),
        migrations.AlterField(
            model_name='lawsuit',
            name='details',
            field=models.TextField(default='Additional details currently not available.'),
        ),
        migrations.AlterField(
            model_name='lawsuit',
            name='source',
            field=models.URLField(default=None),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(default=5, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='child_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='companies.company'),
        ),
        migrations.AlterField(
            model_name='shareholder',
            name='source',
            field=models.URLField(default=None),
        ),
    ]