# Generated by Django 4.2.7 on 2024-05-08 13:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xpoarena', '0026_event_bronze_sponsor_event_gold_sponsor_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenthistory',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='paymenthistory',
            name='sponsorship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='xpoarena.sponsorship'),
        ),
        migrations.AlterField(
            model_name='paymenthistory',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]