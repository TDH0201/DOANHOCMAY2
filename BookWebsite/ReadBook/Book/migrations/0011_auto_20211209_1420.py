# Generated by Django 3.2.9 on 2021-12-09 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0010_auto_20211209_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='createdDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='lastUpdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='createdDate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='lastUpdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
