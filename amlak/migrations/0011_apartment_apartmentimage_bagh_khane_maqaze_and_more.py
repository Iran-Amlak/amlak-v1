# Generated by Django 4.1.2 on 2022-10-29 20:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('amlak', '0010_apartmentbuy_image_villabuy_image_villasell_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malek_name', models.CharField(blank=True, max_length=50, null=True)),
                ('malek_address', models.TextField(blank=True, null=True)),
                ('malek_mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('necessary_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bar_zamin', models.CharField(blank=True, max_length=20, null=True)),
                ('gozar', models.CharField(blank=True, max_length=40, null=True)),
                ('sanad', models.CharField(choices=[('سند تک برگ', 'سند تک برگ'), ('سند قدیمی', 'سند قدیمی'), ('سند شاعی', 'سند شاعی'), ('فاقد سند', 'فاقد سند')], max_length=50)),
                ('position', models.CharField(choices=[('شمالی', 'شمالی'), ('شرقی', 'شرقی'), ('جنوبی', 'جنوبی'), ('غربی', 'غربی'), ('تودلی شمالی', 'تودلی شمالی'), ('تودلی شرقی', 'تودلی شرقی'), ('تودلی جنوبی', 'تودلی جنوبی'), ('تودلی غربی', 'تودلی غربی')], max_length=50)),
                ('karbari', models.CharField(choices=[('مسکونی', 'مسکونی'), ('صنعتی', 'صنعتی'), ('تجاری', 'تجاری'), ('کشاورزی', 'کشاورزی'), ('اداری', 'اداری'), ('سایر', 'سایر')], max_length=50)),
                ('dastrsi', models.CharField(choices=[('آسفالت', 'آسفالت'), ('خاکی', 'خاکی'), ('خاکی قدیمی', 'خاکی قدیمی'), ('عدم دسترسی', 'عدم دسترسی'), ('سایر موارد', 'سایر موارد')], max_length=50)),
                ('topography', models.CharField(choices=[('شیب دار', 'شیب دار'), ('تپه ماهور', 'تپه ماهور'), ('مسطح', 'مسطح')], max_length=50)),
                ('javaz', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد'), ('مراحل اداری اخذ جواز', 'مراحل اداری اخذ جواز')], max_length=50)),
                ('baft', models.CharField(choices=[('شهری', 'شهری'), ('روستایی', 'روستایی'), ('خارج بافت', 'خارج بافت'), ('قسمتی در بافت', 'قسمتی در بافت'), ('قابلیت الحاق به بافت', 'قابلیت الحاق به بافت')], max_length=50)),
                ('view', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('malek_need', models.CharField(choices=[('فروش', 'فروش'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50)),
                ('features', models.CharField(choices=[('مشجر', 'مشجر'), ('درخشان مشجر', 'درخشان مشجر'), ('فضا سازی شده', 'فضا سازی شده'), ('فاقد ویژگی خاص', 'فاقد ویژگی خاص')], max_length=50)),
                ('edit', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=50)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('area_building', models.CharField(blank=True, max_length=100, null=True)),
                ('type_building', models.CharField(blank=True, max_length=100, null=True)),
                ('build_age', models.CharField(blank=True, max_length=100, null=True)),
                ('floor_count', models.CharField(blank=True, max_length=100, null=True)),
                ('floor', models.CharField(blank=True, max_length=50, null=True)),
                ('vahed_count', models.CharField(blank=True, max_length=50, null=True)),
                ('asansor', models.CharField(blank=True, max_length=50, null=True)),
                ('vahed', models.CharField(blank=True, max_length=100, null=True)),
                ('nama_building', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='zamin')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('kaf', models.CharField(choices=[('سنگ', 'سنگ'), ('سرامیک', 'سرامیک'), ('سایر', 'سایر')], max_length=50)),
                ('bam', models.CharField(choices=[('اسپانش', 'اسپانش'), ('شیروانی', 'شیروانی'), ('مسطح سنتی', 'مسطح سنتی')], max_length=50)),
                ('kichen', models.CharField(choices=[('اپن', 'اپن'), ('زیر اپن', 'زیر اپن'), ('کلوز', 'کلوز')], max_length=50)),
                ('garmayesh', models.CharField(choices=[('بخاری', 'بخاری'), ('موتور خانه', 'موتور خانه'), ('فن گویل', 'فن کوِیل'), ('چیلر', 'چیلر')], max_length=50)),
                ('system_garmayesh', models.CharField(choices=[('از کف', 'از کف'), ('بخاری', 'بخاری'), ('رادیاتور', 'رادیاتور'), ('شومینه', 'شومینه')], max_length=50)),
                ('sarmayesh', models.CharField(choices=[('کولر آبی', 'کولر آبی'), ('کولر گازی', 'کولر گازی'), ('فن کویل', 'فن کویل')], max_length=50)),
                ('parking', models.CharField(choices=[('مسقف', 'مسقف'), ('فضا باز', 'فضا باز'), ('ندارد', 'ندارد')], max_length=50)),
                ('fitures', models.CharField(choices=[('سونا', 'سونا'), ('استخر سرپوشیده', 'استخر سر پوشیده'), ('استخر باز', 'استخر باز')], max_length=50)),
                ('zelzele', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('javaz_villa', models.CharField(choices=[('نقشه؟', 'نقشه؟'), ('عدم', 'عدم'), ('پایان کار', 'پایان کار')], max_length=50)),
                ('mechanic_biulding', models.CharField(choices=[('ستون ها', 'ستون ها'), ('رازر ها', 'رازر ها'), ('سایر', 'سایر')], max_length=50)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ApartmentImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='apartment')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlak.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='Bagh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malek_name', models.CharField(blank=True, max_length=50, null=True)),
                ('malek_address', models.TextField(blank=True, null=True)),
                ('malek_mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('necessary_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bar_zamin', models.CharField(blank=True, max_length=20, null=True)),
                ('gozar', models.CharField(blank=True, max_length=40, null=True)),
                ('sanad', models.CharField(choices=[('سند تک برگ', 'سند تک برگ'), ('سند قدیمی', 'سند قدیمی'), ('سند شاعی', 'سند شاعی'), ('فاقد سند', 'فاقد سند')], max_length=50)),
                ('position', models.CharField(choices=[('شمالی', 'شمالی'), ('شرقی', 'شرقی'), ('جنوبی', 'جنوبی'), ('غربی', 'غربی'), ('تودلی شمالی', 'تودلی شمالی'), ('تودلی شرقی', 'تودلی شرقی'), ('تودلی جنوبی', 'تودلی جنوبی'), ('تودلی غربی', 'تودلی غربی')], max_length=50)),
                ('karbari', models.CharField(choices=[('مسکونی', 'مسکونی'), ('صنعتی', 'صنعتی'), ('تجاری', 'تجاری'), ('کشاورزی', 'کشاورزی'), ('اداری', 'اداری'), ('سایر', 'سایر')], max_length=50)),
                ('dastrsi', models.CharField(choices=[('آسفالت', 'آسفالت'), ('خاکی', 'خاکی'), ('خاکی قدیمی', 'خاکی قدیمی'), ('عدم دسترسی', 'عدم دسترسی'), ('سایر موارد', 'سایر موارد')], max_length=50)),
                ('topography', models.CharField(choices=[('شیب دار', 'شیب دار'), ('تپه ماهور', 'تپه ماهور'), ('مسطح', 'مسطح')], max_length=50)),
                ('javaz', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد'), ('مراحل اداری اخذ جواز', 'مراحل اداری اخذ جواز')], max_length=50)),
                ('baft', models.CharField(choices=[('شهری', 'شهری'), ('روستایی', 'روستایی'), ('خارج بافت', 'خارج بافت'), ('قسمتی در بافت', 'قسمتی در بافت'), ('قابلیت الحاق به بافت', 'قابلیت الحاق به بافت')], max_length=50)),
                ('view', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('malek_need', models.CharField(choices=[('فروش', 'فروش'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50)),
                ('features', models.CharField(choices=[('مشجر', 'مشجر'), ('درخشان مشجر', 'درخشان مشجر'), ('فضا سازی شده', 'فضا سازی شده'), ('فاقد ویژگی خاص', 'فاقد ویژگی خاص')], max_length=50)),
                ('edit', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=50)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('area', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='zamin')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('hagh_ab', models.CharField(choices=[('چاه', 'چاه'), ('رودخانه', 'رودخانه'), ('چشمه', 'چشمه'), ('سایر موارد', 'سایر موارد')], max_length=50)),
                ('system_ab', models.CharField(choices=[('مکانیزه', 'مکانیزه'), ('غرق آبی', 'غرق آبی')], max_length=50)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Khane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malek_name', models.CharField(blank=True, max_length=50, null=True)),
                ('malek_address', models.TextField(blank=True, null=True)),
                ('malek_mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('necessary_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bar_zamin', models.CharField(blank=True, max_length=20, null=True)),
                ('gozar', models.CharField(blank=True, max_length=40, null=True)),
                ('sanad', models.CharField(choices=[('سند تک برگ', 'سند تک برگ'), ('سند قدیمی', 'سند قدیمی'), ('سند شاعی', 'سند شاعی'), ('فاقد سند', 'فاقد سند')], max_length=50)),
                ('position', models.CharField(choices=[('شمالی', 'شمالی'), ('شرقی', 'شرقی'), ('جنوبی', 'جنوبی'), ('غربی', 'غربی'), ('تودلی شمالی', 'تودلی شمالی'), ('تودلی شرقی', 'تودلی شرقی'), ('تودلی جنوبی', 'تودلی جنوبی'), ('تودلی غربی', 'تودلی غربی')], max_length=50)),
                ('karbari', models.CharField(choices=[('مسکونی', 'مسکونی'), ('صنعتی', 'صنعتی'), ('تجاری', 'تجاری'), ('کشاورزی', 'کشاورزی'), ('اداری', 'اداری'), ('سایر', 'سایر')], max_length=50)),
                ('dastrsi', models.CharField(choices=[('آسفالت', 'آسفالت'), ('خاکی', 'خاکی'), ('خاکی قدیمی', 'خاکی قدیمی'), ('عدم دسترسی', 'عدم دسترسی'), ('سایر موارد', 'سایر موارد')], max_length=50)),
                ('topography', models.CharField(choices=[('شیب دار', 'شیب دار'), ('تپه ماهور', 'تپه ماهور'), ('مسطح', 'مسطح')], max_length=50)),
                ('javaz', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد'), ('مراحل اداری اخذ جواز', 'مراحل اداری اخذ جواز')], max_length=50)),
                ('baft', models.CharField(choices=[('شهری', 'شهری'), ('روستایی', 'روستایی'), ('خارج بافت', 'خارج بافت'), ('قسمتی در بافت', 'قسمتی در بافت'), ('قابلیت الحاق به بافت', 'قابلیت الحاق به بافت')], max_length=50)),
                ('view', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('malek_need', models.CharField(choices=[('فروش', 'فروش'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50)),
                ('features', models.CharField(choices=[('مشجر', 'مشجر'), ('درخشان مشجر', 'درخشان مشجر'), ('فضا سازی شده', 'فضا سازی شده'), ('فاقد ویژگی خاص', 'فاقد ویژگی خاص')], max_length=50)),
                ('edit', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=50)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('area_building', models.CharField(blank=True, max_length=100, null=True)),
                ('type_building', models.CharField(blank=True, max_length=100, null=True)),
                ('build_age', models.CharField(blank=True, max_length=100, null=True)),
                ('floor_count', models.CharField(blank=True, max_length=100, null=True)),
                ('nama_building', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='zamin')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('kaf', models.CharField(choices=[('سنگ', 'سنگ'), ('سرامیک', 'سرامیک'), ('سایر', 'سایر')], max_length=50)),
                ('bam', models.CharField(choices=[('اسپانش', 'اسپانش'), ('شیروانی', 'شیروانی'), ('مسطح سنتی', 'مسطح سنتی')], max_length=50)),
                ('kichen', models.CharField(choices=[('اپن', 'اپن'), ('زیر اپن', 'زیر اپن'), ('کلوز', 'کلوز')], max_length=50)),
                ('garmayesh', models.CharField(choices=[('بخاری', 'بخاری'), ('موتور خانه', 'موتور خانه'), ('فن گویل', 'فن کوِیل'), ('چیلر', 'چیلر')], max_length=50)),
                ('system_garmayesh', models.CharField(choices=[('از کف', 'از کف'), ('بخاری', 'بخاری'), ('رادیاتور', 'رادیاتور'), ('شومینه', 'شومینه')], max_length=50)),
                ('sarmayesh', models.CharField(choices=[('کولر آبی', 'کولر آبی'), ('کولر گازی', 'کولر گازی'), ('فن کویل', 'فن کویل')], max_length=50)),
                ('parking', models.CharField(choices=[('مسقف', 'مسقف'), ('فضا باز', 'فضا باز'), ('ندارد', 'ندارد')], max_length=50)),
                ('fitures', models.CharField(choices=[('سونا', 'سونا'), ('استخر سرپوشیده', 'استخر سر پوشیده'), ('استخر باز', 'استخر باز')], max_length=50)),
                ('zelzele', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('javaz_villa', models.CharField(choices=[('نقشه؟', 'نقشه؟'), ('عدم', 'عدم'), ('پایان کار', 'پایان کار')], max_length=50)),
                ('mechanic_biulding', models.CharField(choices=[('ستون ها', 'ستون ها'), ('رازر ها', 'رازر ها'), ('سایر', 'سایر')], max_length=50)),
                ('sokonat', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=50)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Maqaze',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malek_name', models.CharField(blank=True, max_length=50, null=True)),
                ('malek_address', models.TextField(blank=True, null=True)),
                ('malek_mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('necessary_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bar_zamin', models.CharField(blank=True, max_length=20, null=True)),
                ('gozar', models.CharField(blank=True, max_length=40, null=True)),
                ('sanad', models.CharField(choices=[('سند تک برگ', 'سند تک برگ'), ('سند قدیمی', 'سند قدیمی'), ('سند شاعی', 'سند شاعی'), ('فاقد سند', 'فاقد سند')], max_length=50)),
                ('position', models.CharField(choices=[('شمالی', 'شمالی'), ('شرقی', 'شرقی'), ('جنوبی', 'جنوبی'), ('غربی', 'غربی'), ('تودلی شمالی', 'تودلی شمالی'), ('تودلی شرقی', 'تودلی شرقی'), ('تودلی جنوبی', 'تودلی جنوبی'), ('تودلی غربی', 'تودلی غربی')], max_length=50)),
                ('karbari', models.CharField(choices=[('مسکونی', 'مسکونی'), ('صنعتی', 'صنعتی'), ('تجاری', 'تجاری'), ('کشاورزی', 'کشاورزی'), ('اداری', 'اداری'), ('سایر', 'سایر')], max_length=50)),
                ('dastrsi', models.CharField(choices=[('آسفالت', 'آسفالت'), ('خاکی', 'خاکی'), ('خاکی قدیمی', 'خاکی قدیمی'), ('عدم دسترسی', 'عدم دسترسی'), ('سایر موارد', 'سایر موارد')], max_length=50)),
                ('topography', models.CharField(choices=[('شیب دار', 'شیب دار'), ('تپه ماهور', 'تپه ماهور'), ('مسطح', 'مسطح')], max_length=50)),
                ('javaz', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد'), ('مراحل اداری اخذ جواز', 'مراحل اداری اخذ جواز')], max_length=50)),
                ('baft', models.CharField(choices=[('شهری', 'شهری'), ('روستایی', 'روستایی'), ('خارج بافت', 'خارج بافت'), ('قسمتی در بافت', 'قسمتی در بافت'), ('قابلیت الحاق به بافت', 'قابلیت الحاق به بافت')], max_length=50)),
                ('view', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('malek_need', models.CharField(choices=[('فروش', 'فروش'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50)),
                ('features', models.CharField(choices=[('مشجر', 'مشجر'), ('درخشان مشجر', 'درخشان مشجر'), ('فضا سازی شده', 'فضا سازی شده'), ('فاقد ویژگی خاص', 'فاقد ویژگی خاص')], max_length=50)),
                ('edit', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=50)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('area', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='zamin')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('sarqofli', models.CharField(blank=True, max_length=100, null=True)),
                ('malekiat', models.CharField(blank=True, max_length=100, null=True)),
                ('karbari_khas', models.CharField(choices=[('کارگاهی', 'کارگاهی'), ('تجاری', 'تجاری'), ('موقعیت تجاری', 'موقعیت تجاری'), ('سایر موارد', 'سایر موارد')], max_length=50)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mostaghelat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malek_name', models.CharField(blank=True, max_length=50, null=True)),
                ('malek_address', models.TextField(blank=True, null=True)),
                ('malek_mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('necessary_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bar_zamin', models.CharField(blank=True, max_length=20, null=True)),
                ('gozar', models.CharField(blank=True, max_length=40, null=True)),
                ('sanad', models.CharField(choices=[('سند تک برگ', 'سند تک برگ'), ('سند قدیمی', 'سند قدیمی'), ('سند شاعی', 'سند شاعی'), ('فاقد سند', 'فاقد سند')], max_length=50)),
                ('position', models.CharField(choices=[('شمالی', 'شمالی'), ('شرقی', 'شرقی'), ('جنوبی', 'جنوبی'), ('غربی', 'غربی'), ('تودلی شمالی', 'تودلی شمالی'), ('تودلی شرقی', 'تودلی شرقی'), ('تودلی جنوبی', 'تودلی جنوبی'), ('تودلی غربی', 'تودلی غربی')], max_length=50)),
                ('karbari', models.CharField(choices=[('مسکونی', 'مسکونی'), ('صنعتی', 'صنعتی'), ('تجاری', 'تجاری'), ('کشاورزی', 'کشاورزی'), ('اداری', 'اداری'), ('سایر', 'سایر')], max_length=50)),
                ('dastrsi', models.CharField(choices=[('آسفالت', 'آسفالت'), ('خاکی', 'خاکی'), ('خاکی قدیمی', 'خاکی قدیمی'), ('عدم دسترسی', 'عدم دسترسی'), ('سایر موارد', 'سایر موارد')], max_length=50)),
                ('topography', models.CharField(choices=[('شیب دار', 'شیب دار'), ('تپه ماهور', 'تپه ماهور'), ('مسطح', 'مسطح')], max_length=50)),
                ('javaz', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد'), ('مراحل اداری اخذ جواز', 'مراحل اداری اخذ جواز')], max_length=50)),
                ('baft', models.CharField(choices=[('شهری', 'شهری'), ('روستایی', 'روستایی'), ('خارج بافت', 'خارج بافت'), ('قسمتی در بافت', 'قسمتی در بافت'), ('قابلیت الحاق به بافت', 'قابلیت الحاق به بافت')], max_length=50)),
                ('view', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('malek_need', models.CharField(choices=[('فروش', 'فروش'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50)),
                ('features', models.CharField(choices=[('مشجر', 'مشجر'), ('درخشان مشجر', 'درخشان مشجر'), ('فضا سازی شده', 'فضا سازی شده'), ('فاقد ویژگی خاص', 'فاقد ویژگی خاص')], max_length=50)),
                ('edit', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=50)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('area_building', models.CharField(blank=True, max_length=100, null=True)),
                ('type_building', models.CharField(blank=True, max_length=100, null=True)),
                ('build_age', models.CharField(blank=True, max_length=100, null=True)),
                ('floor_count', models.CharField(blank=True, max_length=100, null=True)),
                ('nama_building', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='zamin')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('kaf', models.CharField(choices=[('سنگ', 'سنگ'), ('سرامیک', 'سرامیک'), ('سایر', 'سایر')], max_length=50)),
                ('bam', models.CharField(choices=[('اسپانش', 'اسپانش'), ('شیروانی', 'شیروانی'), ('مسطح سنتی', 'مسطح سنتی')], max_length=50)),
                ('kichen', models.CharField(choices=[('اپن', 'اپن'), ('زیر اپن', 'زیر اپن'), ('کلوز', 'کلوز')], max_length=50)),
                ('garmayesh', models.CharField(choices=[('بخاری', 'بخاری'), ('موتور خانه', 'موتور خانه'), ('فن گویل', 'فن کوِیل'), ('چیلر', 'چیلر')], max_length=50)),
                ('system_garmayesh', models.CharField(choices=[('از کف', 'از کف'), ('بخاری', 'بخاری'), ('رادیاتور', 'رادیاتور'), ('شومینه', 'شومینه')], max_length=50)),
                ('sarmayesh', models.CharField(choices=[('کولر آبی', 'کولر آبی'), ('کولر گازی', 'کولر گازی'), ('فن کویل', 'فن کویل')], max_length=50)),
                ('parking', models.CharField(choices=[('مسقف', 'مسقف'), ('فضا باز', 'فضا باز'), ('ندارد', 'ندارد')], max_length=50)),
                ('fitures', models.CharField(choices=[('سونا', 'سونا'), ('استخر سرپوشیده', 'استخر سر پوشیده'), ('استخر باز', 'استخر باز')], max_length=50)),
                ('zelzele', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('javaz_villa', models.CharField(choices=[('نقشه؟', 'نقشه؟'), ('عدم', 'عدم'), ('پایان کار', 'پایان کار')], max_length=50)),
                ('mechanic_biulding', models.CharField(choices=[('ستون ها', 'ستون ها'), ('رازر ها', 'رازر ها'), ('سایر', 'سایر')], max_length=50)),
                ('mojtama_apartment', models.CharField(blank=True, max_length=100, null=True)),
                ('floor', models.CharField(blank=True, max_length=50, null=True)),
                ('asansor', models.CharField(blank=True, max_length=50, null=True)),
                ('varase', models.CharField(blank=True, max_length=50, null=True)),
                ('num_malek', models.CharField(blank=True, max_length=50, null=True)),
                ('others', models.CharField(blank=True, max_length=100, null=True)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malek_name', models.CharField(blank=True, max_length=50, null=True)),
                ('malek_address', models.TextField(blank=True, null=True)),
                ('malek_mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('necessary_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bar_zamin', models.CharField(blank=True, max_length=20, null=True)),
                ('gozar', models.CharField(blank=True, max_length=40, null=True)),
                ('sanad', models.CharField(choices=[('سند تک برگ', 'سند تک برگ'), ('سند قدیمی', 'سند قدیمی'), ('سند شاعی', 'سند شاعی'), ('فاقد سند', 'فاقد سند')], max_length=50)),
                ('position', models.CharField(choices=[('شمالی', 'شمالی'), ('شرقی', 'شرقی'), ('جنوبی', 'جنوبی'), ('غربی', 'غربی'), ('تودلی شمالی', 'تودلی شمالی'), ('تودلی شرقی', 'تودلی شرقی'), ('تودلی جنوبی', 'تودلی جنوبی'), ('تودلی غربی', 'تودلی غربی')], max_length=50)),
                ('karbari', models.CharField(choices=[('مسکونی', 'مسکونی'), ('صنعتی', 'صنعتی'), ('تجاری', 'تجاری'), ('کشاورزی', 'کشاورزی'), ('اداری', 'اداری'), ('سایر', 'سایر')], max_length=50)),
                ('dastrsi', models.CharField(choices=[('آسفالت', 'آسفالت'), ('خاکی', 'خاکی'), ('خاکی قدیمی', 'خاکی قدیمی'), ('عدم دسترسی', 'عدم دسترسی'), ('سایر موارد', 'سایر موارد')], max_length=50)),
                ('topography', models.CharField(choices=[('شیب دار', 'شیب دار'), ('تپه ماهور', 'تپه ماهور'), ('مسطح', 'مسطح')], max_length=50)),
                ('javaz', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد'), ('مراحل اداری اخذ جواز', 'مراحل اداری اخذ جواز')], max_length=50)),
                ('baft', models.CharField(choices=[('شهری', 'شهری'), ('روستایی', 'روستایی'), ('خارج بافت', 'خارج بافت'), ('قسمتی در بافت', 'قسمتی در بافت'), ('قابلیت الحاق به بافت', 'قابلیت الحاق به بافت')], max_length=50)),
                ('view', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('malek_need', models.CharField(choices=[('فروش', 'فروش'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50)),
                ('features', models.CharField(choices=[('مشجر', 'مشجر'), ('درخشان مشجر', 'درخشان مشجر'), ('فضا سازی شده', 'فضا سازی شده'), ('فاقد ویژگی خاص', 'فاقد ویژگی خاص')], max_length=50)),
                ('edit', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=50)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('area', models.CharField(blank=True, max_length=100, null=True)),
                ('area_building', models.CharField(blank=True, max_length=100, null=True)),
                ('type_building', models.CharField(blank=True, max_length=100, null=True)),
                ('build_age', models.CharField(blank=True, max_length=100, null=True)),
                ('floor_count', models.CharField(blank=True, max_length=100, null=True)),
                ('nama_building', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='zamin')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('kaf', models.CharField(choices=[('سنگ', 'سنگ'), ('سرامیک', 'سرامیک'), ('سایر', 'سایر')], max_length=50)),
                ('bam', models.CharField(choices=[('اسپانش', 'اسپانش'), ('شیروانی', 'شیروانی'), ('مسطح سنتی', 'مسطح سنتی')], max_length=50)),
                ('kichen', models.CharField(choices=[('اپن', 'اپن'), ('زیر اپن', 'زیر اپن'), ('کلوز', 'کلوز')], max_length=50)),
                ('garmayesh', models.CharField(choices=[('بخاری', 'بخاری'), ('موتور خانه', 'موتور خانه'), ('فن گویل', 'فن کوِیل'), ('چیلر', 'چیلر')], max_length=50)),
                ('system_garmayesh', models.CharField(choices=[('از کف', 'از کف'), ('بخاری', 'بخاری'), ('رادیاتور', 'رادیاتور'), ('شومینه', 'شومینه')], max_length=50)),
                ('sarmayesh', models.CharField(choices=[('کولر آبی', 'کولر آبی'), ('کولر گازی', 'کولر گازی'), ('فن کویل', 'فن کویل')], max_length=50)),
                ('parking', models.CharField(choices=[('مسقف', 'مسقف'), ('فضا باز', 'فضا باز'), ('ندارد', 'ندارد')], max_length=50)),
                ('fitures', models.CharField(choices=[('سونا', 'سونا'), ('استخر سرپوشیده', 'استخر سر پوشیده'), ('استخر باز', 'استخر باز')], max_length=50)),
                ('zelzele', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('javaz_villa', models.CharField(choices=[('نقشه؟', 'نقشه؟'), ('عدم', 'عدم'), ('پایان کار', 'پایان کار')], max_length=50)),
                ('mechanic_biulding', models.CharField(choices=[('ستون ها', 'ستون ها'), ('رازر ها', 'رازر ها'), ('سایر', 'سایر')], max_length=50)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='VillaImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='villa')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('villa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlak.villa')),
            ],
        ),
        migrations.CreateModel(
            name='Zamin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('malek_name', models.CharField(blank=True, max_length=50, null=True)),
                ('malek_address', models.TextField(blank=True, null=True)),
                ('malek_mobile', models.CharField(blank=True, max_length=12, null=True)),
                ('necessary_mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('post_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bar_zamin', models.CharField(blank=True, max_length=20, null=True)),
                ('gozar', models.CharField(blank=True, max_length=40, null=True)),
                ('sanad', models.CharField(choices=[('سند تک برگ', 'سند تک برگ'), ('سند قدیمی', 'سند قدیمی'), ('سند شاعی', 'سند شاعی'), ('فاقد سند', 'فاقد سند')], max_length=50)),
                ('position', models.CharField(choices=[('شمالی', 'شمالی'), ('شرقی', 'شرقی'), ('جنوبی', 'جنوبی'), ('غربی', 'غربی'), ('تودلی شمالی', 'تودلی شمالی'), ('تودلی شرقی', 'تودلی شرقی'), ('تودلی جنوبی', 'تودلی جنوبی'), ('تودلی غربی', 'تودلی غربی')], max_length=50)),
                ('karbari', models.CharField(choices=[('مسکونی', 'مسکونی'), ('صنعتی', 'صنعتی'), ('تجاری', 'تجاری'), ('کشاورزی', 'کشاورزی'), ('اداری', 'اداری'), ('سایر', 'سایر')], max_length=50)),
                ('dastrsi', models.CharField(choices=[('آسفالت', 'آسفالت'), ('خاکی', 'خاکی'), ('خاکی قدیمی', 'خاکی قدیمی'), ('عدم دسترسی', 'عدم دسترسی'), ('سایر موارد', 'سایر موارد')], max_length=50)),
                ('topography', models.CharField(choices=[('شیب دار', 'شیب دار'), ('تپه ماهور', 'تپه ماهور'), ('مسطح', 'مسطح')], max_length=50)),
                ('javaz', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد'), ('مراحل اداری اخذ جواز', 'مراحل اداری اخذ جواز')], max_length=50)),
                ('baft', models.CharField(choices=[('شهری', 'شهری'), ('روستایی', 'روستایی'), ('خارج بافت', 'خارج بافت'), ('قسمتی در بافت', 'قسمتی در بافت'), ('قابلیت الحاق به بافت', 'قابلیت الحاق به بافت')], max_length=50)),
                ('view', models.CharField(choices=[('عالی', 'عالی'), ('خوب', 'خوب'), ('متوسط', 'متوسط'), ('بد', 'بد')], max_length=50)),
                ('malek_need', models.CharField(choices=[('فروش', 'فروش'), ('تهاتر', 'تهاتر'), ('مشارکت', 'مشارکت'), ('معاوضه', 'معاوضه')], max_length=50)),
                ('features', models.CharField(choices=[('مشجر', 'مشجر'), ('درخشان مشجر', 'درخشان مشجر'), ('فضا سازی شده', 'فضا سازی شده'), ('فاقد ویژگی خاص', 'فاقد ویژگی خاص')], max_length=50)),
                ('edit', models.CharField(choices=[('دارد', 'دارد'), ('ندارد', 'ندارد')], max_length=50)),
                ('price', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('area', models.PositiveIntegerField(blank=True, null=True)),
                ('description', models.TextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='zamin')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('superuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ZaminImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='zamin')),
                ('modified', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('zamin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='amlak.zamin')),
            ],
        ),
        migrations.RemoveField(
            model_name='apartmentbuyimage',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='apartmentsell',
            name='superuser',
        ),
        migrations.RemoveField(
            model_name='apartmentsellimage',
            name='apartment',
        ),
        migrations.RemoveField(
            model_name='villabuy',
            name='user',
        ),
        migrations.RemoveField(
            model_name='villabuyimage',
            name='villa',
        ),
        migrations.RemoveField(
            model_name='villasell',
            name='superuser',
        ),
        migrations.RemoveField(
            model_name='villasellimage',
            name='villa',
        ),
        migrations.RemoveField(
            model_name='zaminbuy',
            name='user',
        ),
        migrations.RemoveField(
            model_name='zaminbuyimage',
            name='zamin',
        ),
        migrations.RemoveField(
            model_name='zaminsell',
            name='superuser',
        ),
        migrations.RemoveField(
            model_name='zaminsellimage',
            name='zamin',
        ),
        migrations.DeleteModel(
            name='ApartmentBuy',
        ),
        migrations.DeleteModel(
            name='ApartmentBuyImage',
        ),
        migrations.DeleteModel(
            name='ApartmentSell',
        ),
        migrations.DeleteModel(
            name='ApartmentSellImage',
        ),
        migrations.DeleteModel(
            name='VillaBuy',
        ),
        migrations.DeleteModel(
            name='VillaBuyImage',
        ),
        migrations.DeleteModel(
            name='VillaSell',
        ),
        migrations.DeleteModel(
            name='VillaSellImage',
        ),
        migrations.DeleteModel(
            name='ZaminBuy',
        ),
        migrations.DeleteModel(
            name='ZaminBuyImage',
        ),
        migrations.DeleteModel(
            name='ZaminSell',
        ),
        migrations.DeleteModel(
            name='ZaminSellImage',
        ),
    ]
