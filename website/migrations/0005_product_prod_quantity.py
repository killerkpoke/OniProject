# Generated by Django 4.1.7 on 2023-03-11 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_product_prod_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_quantity',
            field=models.DecimalField(decimal_places=1, max_digits=10, null=True),
        ),
    ]
