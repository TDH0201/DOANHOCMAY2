# Generated by Django 3.2.9 on 2021-12-02 15:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastUpdate', models.DateTimeField(auto_now=True)),
                ('lastUpdater', models.CharField(default='', max_length=255)),
                ('createdDate', models.DateTimeField(auto_now_add=True)),
                ('createdDater', models.CharField(default='', max_length=255)),
                ('authorName', models.CharField(max_length=255)),
                ('address', models.CharField(default='SOME STRING', max_length=255)),
                ('email', models.CharField(default='SOME STRING', max_length=255)),
                ('emailChecked', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='book',
            name='createdDate',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2021, 12, 2, 15, 50, 2, 480570, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='createdDater',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='book',
            name='lastUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='book',
            name='lastUpdater',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='imgBook',
            field=models.CharField(default='SOME STRING', max_length=255),
        ),
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Book.author'),
        ),
    ]