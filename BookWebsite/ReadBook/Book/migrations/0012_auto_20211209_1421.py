# Generated by Django 3.2.9 on 2021-12-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0011_auto_20211209_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='createdDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='createdDate',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]