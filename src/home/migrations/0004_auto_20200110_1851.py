# Generated by Django 3.0.2 on 2020-01-10 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200110_1839'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productsubcategory',
            old_name='name',
            new_name='subCategoryName',
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
