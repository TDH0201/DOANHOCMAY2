# Generated by Django 3.2.9 on 2021-12-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0012_auto_20211209_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='createdDater',
            field=models.CharField(default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='createdDater',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
