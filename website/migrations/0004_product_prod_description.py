# Generated by Django 4.1.7 on 2023-03-11 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='prod_description',
            field=models.TextField(blank=True),
        ),
    ]
