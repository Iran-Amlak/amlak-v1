# Generated by Django 4.1.2 on 2022-11-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amlak', '0015_remove_archiveuser_need_kharidar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bagh',
            name='area',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='مساحت'),
        ),
        migrations.AlterField(
            model_name='bagh',
            name='hagh_ab',
            field=models.CharField(choices=[('چاه', 'چاه'), ('رودخانه', 'رودخانه'), ('چشمه', 'چشمه'), ('سایر موارد', 'سایر موارد')], max_length=50, verbose_name='حق آب'),
        ),
        migrations.AlterField(
            model_name='bagh',
            name='system_ab',
            field=models.CharField(choices=[('مکانیزه', 'مکانیزه'), ('غرق آبی', 'غرق آبی')], max_length=50, verbose_name='سیستم آبیاری'),
        ),
        migrations.AlterField(
            model_name='maqaze',
            name='area',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='مساحت'),
        ),
        migrations.AlterField(
            model_name='zamin',
            name='area',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='مساحت'),
        ),
    ]
