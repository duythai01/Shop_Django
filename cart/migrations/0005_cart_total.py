# Generated by Django 3.2.7 on 2021-10-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_delete_variation'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='total',
            field=models.FloatField(default=0),
        ),
    ]