# Generated by Django 3.2.7 on 2021-10-21 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20211007_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_link',
            field=models.ImageField(default=None, upload_to='static/Product_image/%y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product'),
        ),
    ]