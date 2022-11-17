# Generated by Django 4.1.2 on 2022-10-26 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amlak', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentbuy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='apartment-buy'),
        ),
        migrations.AddField(
            model_name='apartmentsell',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='apartment-sell'),
        ),
        migrations.AddField(
            model_name='villabuy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='villa_buy'),
        ),
        migrations.AddField(
            model_name='villasell',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='villa-sell'),
        ),
        migrations.AddField(
            model_name='zaminbuy',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='zamin_buy'),
        ),
        migrations.AddField(
            model_name='zaminsell',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='zamin-sell'),
        ),
    ]
