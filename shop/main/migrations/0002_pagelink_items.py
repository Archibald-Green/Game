# Generated by Django 4.1.7 on 2023-04-02 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagelink',
            name='items',
            field=models.ManyToManyField(blank=True, to='main.item'),
        ),
    ]
