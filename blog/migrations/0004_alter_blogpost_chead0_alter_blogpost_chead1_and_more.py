# Generated by Django 4.0.2 on 2022-03-11 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_category_alter_blogpost_chead1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='chead0',
            field=models.TextField(default='', max_length=600),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead1',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead2',
            field=models.TextField(default='', max_length=600),
        ),
    ]