# Generated by Django 3.2.6 on 2021-10-06 02:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ship_address', models.TextField(blank=True, null=True)),
                ('order_description', models.TextField(blank=True, null=True)),
                ('total', models.IntegerField(default=0)),
                ('is_completed', models.BooleanField(default=False)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cart.cart')),
            ],
        ),
    ]
