# Generated by Django 4.0.2 on 2022-03-11 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogpost_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead1',
            field=models.TextField(default='', max_length=500),
        ),
    ]
