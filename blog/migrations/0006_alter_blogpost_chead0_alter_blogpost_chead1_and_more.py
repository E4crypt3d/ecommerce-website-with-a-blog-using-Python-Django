# Generated by Django 4.0.2 on 2022-03-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blogpost_category_alter_blogpost_chead0_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='chead0',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead1',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead2',
            field=models.TextField(max_length=1500),
        ),
    ]
