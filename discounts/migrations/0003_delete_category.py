# Generated by Django 4.2.1 on 2023-06-28 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discounts', '0002_remove_discount_categories'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
