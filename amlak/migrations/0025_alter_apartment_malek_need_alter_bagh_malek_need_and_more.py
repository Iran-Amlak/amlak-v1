# Generated by Django 4.1.2 on 2022-11-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amlak', '0024_alter_apartment_fitures_alter_khane_fitures_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='malek_need',
            field=models.CharField(choices=[('فروش', 'فروش'), ('اجاره', 'اجاره'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50, verbose_name='نیاز مالک'),
        ),
        migrations.AlterField(
            model_name='bagh',
            name='malek_need',
            field=models.CharField(choices=[('فروش', 'فروش'), ('اجاره', 'اجاره'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50, verbose_name='نیاز مالک'),
        ),
        migrations.AlterField(
            model_name='khane',
            name='malek_need',
            field=models.CharField(choices=[('فروش', 'فروش'), ('اجاره', 'اجاره'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50, verbose_name='نیاز مالک'),
        ),
        migrations.AlterField(
            model_name='maqaze',
            name='malek_need',
            field=models.CharField(choices=[('فروش', 'فروش'), ('اجاره', 'اجاره'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50, verbose_name='نیاز مالک'),
        ),
        migrations.AlterField(
            model_name='mostaghelat',
            name='malek_need',
            field=models.CharField(choices=[('فروش', 'فروش'), ('اجاره', 'اجاره'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50, verbose_name='نیاز مالک'),
        ),
        migrations.AlterField(
            model_name='villa',
            name='malek_need',
            field=models.CharField(choices=[('فروش', 'فروش'), ('اجاره', 'اجاره'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50, verbose_name='نیاز مالک'),
        ),
        migrations.AlterField(
            model_name='zamin',
            name='malek_need',
            field=models.CharField(choices=[('فروش', 'فروش'), ('اجاره', 'اجاره'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50, verbose_name='نیاز مالک'),
        ),
    ]
