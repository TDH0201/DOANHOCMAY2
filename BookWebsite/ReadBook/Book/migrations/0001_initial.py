# Generated by Django 3.2.9 on 2021-12-02 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookName', models.CharField(max_length=255)),
                ('description', models.CharField(default='SOME STRING', max_length=255)),
                ('contents', models.CharField(default='SOME STRING', max_length=255)),
                ('overview', models.CharField(default='SOME STRING', max_length=255)),
                ('imgBook', models.ImageField(default=None, upload_to='Book/%y/%m')),
            ],
        ),
    ]
