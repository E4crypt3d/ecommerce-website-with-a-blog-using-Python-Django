# Generated by Django 4.0.2 on 2022-03-05 17:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buybest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='updateorder',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]