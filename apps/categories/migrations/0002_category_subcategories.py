# Generated by Django 4.2.1 on 2023-07-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subcategories',
            field=models.ManyToManyField(blank=True, to='categories.category'),
        ),
    ]
