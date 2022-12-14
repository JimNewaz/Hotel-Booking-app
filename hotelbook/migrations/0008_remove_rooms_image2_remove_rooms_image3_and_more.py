# Generated by Django 4.1.3 on 2022-11-25 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotelbook', '0007_rooms_image2_rooms_image3_rooms_image4_rooms_image5'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='image5',
        ),
        migrations.CreateModel(
            name='RoomImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(blank=True, null=True, upload_to='')),
                ('post', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='hotelbook.rooms')),
            ],
        ),
    ]
