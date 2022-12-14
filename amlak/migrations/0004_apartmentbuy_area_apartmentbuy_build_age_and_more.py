# Generated by Django 4.1.2 on 2022-10-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amlak', '0003_apartmentbuy_malek_mobile_apartmentsell_malek_mobile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentbuy',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentbuy',
            name='build_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentbuy',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='apartmentbuy',
            name='floor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentbuy',
            name='room',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentbuy',
            name='status',
            field=models.CharField(blank=True, choices=[('موجود', 'موجود'), ('نا موجود', 'ناموجود')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='apartmentsell',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentsell',
            name='build_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentsell',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='apartmentsell',
            name='floor',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentsell',
            name='room',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='apartmentsell',
            name='status',
            field=models.CharField(blank=True, choices=[('موجود', 'موجود'), ('نا موجود', 'ناموجود')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='villabuy',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='villabuy',
            name='build_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='villabuy',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='villabuy',
            name='room',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='villabuy',
            name='status',
            field=models.CharField(blank=True, choices=[('موجود', 'موجود'), ('نا موجود', 'ناموجود')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='villasell',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='villasell',
            name='build_age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='villasell',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='villasell',
            name='room',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='villasell',
            name='status',
            field=models.CharField(blank=True, choices=[('موجود', 'موجود'), ('نا موجود', 'ناموجود')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='zaminbuy',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='zaminbuy',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='zaminbuy',
            name='status',
            field=models.CharField(blank=True, choices=[('موجود', 'موجود'), ('نا موجود', 'ناموجود')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='zaminsell',
            name='area',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='zaminsell',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='zaminsell',
            name='status',
            field=models.CharField(blank=True, choices=[('موجود', 'موجود'), ('نا موجود', 'ناموجود')], max_length=50, null=True),
        ),
    ]
