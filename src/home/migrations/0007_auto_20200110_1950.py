# Generated by Django 3.0.2 on 2020-01-10 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200110_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='title',
        ),
        migrations.AlterField(
            model_name='product',
            name='categoryId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='home.ProductCategory'),
        ),
        migrations.AlterField(
            model_name='product',
            name='subCategoryId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='subCategory', to='home.ProductSubCategory'),
        ),
        migrations.AlterField(
            model_name='productsubcategory',
            name='productCategoryId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='productCategory', to='home.ProductCategory'),
        ),
    ]