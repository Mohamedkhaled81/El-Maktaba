# Generated by Django 4.2.4 on 2023-09-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_books_slug_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='slug',
            field=models.SlugField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(blank=True, default=None),
        ),
    ]
