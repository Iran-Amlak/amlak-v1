# Generated by Django 4.1.3 on 2022-11-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amlak', '0025_alter_apartment_malek_need_alter_bagh_malek_need_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='khane', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='archiveuser',
            name='needed_melk',
            field=models.CharField(choices=[('زمین', 'زمین'), ('باغ', 'باغ'), ('ویلا', 'ویلا'), ('آپارتمان', 'آپارتمان'), ('مستغلات', 'مستغلات'), ('خانه', 'خانه'), ('مغازه', 'مغازه')], max_length=50, verbose_name='نوع ملک'),
        ),
        migrations.AlterField(
            model_name='bagh',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='khane', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='khane',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='khane', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='maqaze',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='khane', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='mostaghelat',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='khane', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='villa',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='khane', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='zamin',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='khane', verbose_name='تصویر'),
        ),
    ]
