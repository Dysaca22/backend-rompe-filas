# Generated by Django 4.2.1 on 2023-06-02 00:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('turn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='turn',
            name='time',
            field=models.CharField(choices=[('08:00 - 10:00', '08:00 - 10:00'), ('10:00 - 12:00', '10:00 - 12:00'), ('16:00 - 18:00', '16:00 - 18:00'), ('12:00 - 14:00', '12:00 - 14:00'), ('18:00 - 20:00', '18:00 - 20:00'), ('14:00 - 16:00', '14:00 - 16:00')], default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='turn',
            name='date',
            field=models.DateField(),
        ),
    ]