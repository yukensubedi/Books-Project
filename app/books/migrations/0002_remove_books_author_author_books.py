# Generated by Django 5.0.1 on 2024-01-21 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(to='books.books'),
        ),
    ]
