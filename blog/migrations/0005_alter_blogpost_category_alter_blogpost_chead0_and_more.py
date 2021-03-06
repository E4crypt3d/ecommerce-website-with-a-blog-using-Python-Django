# Generated by Django 4.0.2 on 2022-03-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blogpost_chead0_alter_blogpost_chead1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='category',
            field=models.CharField(choices=[('Design', 'Design'), ('World', 'World'), ('Eduction', 'Eduction'), ('Art', 'Art'), ('History', 'History'), ('Random', 'Random')], default='Random', max_length=15),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead0',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='chead2',
            field=models.TextField(max_length=600),
        ),
    ]
