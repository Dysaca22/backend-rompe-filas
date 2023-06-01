# Generated by Django 4.2.1 on 2023-06-01 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualify',
            name='comment',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='qualify',
            name='rate',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (5, '5'), (3, '3'), (4, '4')]),
        ),
    ]
