# Generated by Django 4.2.4 on 2023-09-07 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0007_alter_books_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.subcategory'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subset', to='book.category'),
        ),
    ]