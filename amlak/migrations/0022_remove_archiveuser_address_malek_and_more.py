# Generated by Django 4.1.2 on 2022-11-08 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amlak', '0021_remove_apartment_javaz_villa_bagh_derakht_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='archiveuser',
            name='address_malek',
        ),
        migrations.AlterField(
            model_name='archiveuser',
            name='mobile_malek',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='تلفن خریدار'),
        ),
        migrations.AlterField(
            model_name='archiveuser',
            name='name_malek',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='نام خریدار'),
        ),
    ]
