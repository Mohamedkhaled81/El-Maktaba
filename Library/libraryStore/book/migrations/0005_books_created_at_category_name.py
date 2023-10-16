# Generated by Django 4.2.4 on 2023-09-07 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_alter_books_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='N/A', max_length=30),
        ),
    ]