# Generated by Django 4.2.7 on 2024-03-11 13:47

from django.db import migrations, models
import xpoarena.models


class Migration(migrations.Migration):

    dependencies = [
        ('xpoarena', '0016_alter_game_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=xpoarena.models.upload_to, verbose_name='Image'),
        ),
    ]