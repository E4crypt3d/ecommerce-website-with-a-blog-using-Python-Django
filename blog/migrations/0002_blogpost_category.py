# Generated by Django 4.0.2 on 2022-03-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default='', max_length=40),
        ),
    ]
