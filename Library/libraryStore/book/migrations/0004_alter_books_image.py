# Generated by Django 4.2.4 on 2023-09-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_books_slug_alter_category_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
    ]