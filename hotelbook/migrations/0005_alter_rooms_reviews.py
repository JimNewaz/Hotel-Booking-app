# Generated by Django 4.1.3 on 2022-11-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbook', '0004_alter_rooms_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='reviews',
            field=models.CharField(default=None, max_length=100),
        ),
    ]