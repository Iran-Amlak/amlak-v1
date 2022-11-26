from django.db import models
from user_auth.models import User
from extensions.utils import jalali_converter

derakht_type = (
    ('مثمر', 'مثمر'),
    ('سایر', 'سایر'),
)

system_amniat = (
    ('دوربین', 'دوربین'),
    ('دزدگیر', 'دزدگیر'),
    ('حفاظ', 'حفاظ'),
    ('سایر', 'سایر'),
)


sanad_status = (
    ('سند تک برگ', 'سند تک برگ'),
    ('سند قدیمی', 'سند قدیمی'),
    ('سند مشاعی', 'سند مشاعی'),
    ('مبایعه نامه', 'مبایعه نامه'),
    ('سایر', 'سایر'),
)

position_status = (
    ('شمالی', 'شمالی'),
    ('شرقی', 'شرقی'),
    ('جنوبی', 'جنوبی'),
    ('غربی', 'غربی'),
    ('تودلی شمالی', 'تودلی شمالی'),
    ('تودلی شرقی', 'تودلی شرقی'),
    ('تودلی جنوبی', 'تودلی جنوبی'),
    ('تودلی غربی', 'تودلی غربی'),
    ('دو کله', 'دو کله'),
    ('سه بر', 'سه بر'),
    ('دوبر', 'دوبر'),
    ('جزیره ای', 'جزیره ای'),
)

karbari_status = (
    ('مسکونی', 'مسکونی'),
    ('صنعتی', 'صنعتی'),
    ('تجاری', 'تجاری'),
    ('کشاورزی', 'کشاورزی'),
    ('اداری', 'اداری'),
    ('سایر', 'سایر'),
)

dastrsi_status = (
    ('آسفالت', 'آسفالت'),
    ('خاکی', 'خاکی'),
    ('خاکی قدیمی', 'خاکی قدیمی'),
    ('عدم دسترسی', 'عدم دسترسی'),
    ('سایر موارد', 'سایر موارد'),
)

topography_status = (
    ('شیب دار', 'شیب دار'),
    ('تپه ماهور', 'تپه ماهور'),
    ('مسطح', 'مسطح'),
    ('سایر', 'سایر'),
)

javaz_status = (
    ('دارد', 'دارد'),
    ('ندارد', 'ندارد'),
    ('مراحل اداری اخذ جواز', 'مراحل اداری اخذ جواز'),
)

baft_status = (
    ('شهری', 'شهری'),
    ('روستایی', 'روستایی'),
    ('خارج بافت', 'خارج بافت'),
    ('قسمتی در بافت', 'قسمتی در بافت'),
    ('قابلیت الحاق به بافت', 'قابلیت الحاق به بافت'),
)

view_status = (
    ('عالی', 'عالی'),
    ('خوب', 'خوب'),
    ('متوسط', 'متوسط'),
    ('بد', 'بد'),
)

malek_need_status = (
    ('فروش', 'فروش'),
    ('اجاره', 'اجاره'),
    ('تهاتر', 'تهاتر'),
    ('مشارکت', 'مشارکت'),
    ('معاوضه', 'معاوضه'),
)

features_status = (
    ('مشجر', 'مشجر'),
    ('درختان مثمر', 'درختان مثمر'),
    ('فضا سازی شده', 'فضا سازی شده'),
    ('فاقد ویژگی خاص', 'فاقد ویژگی خاص'),
    ('سایر موارد', 'سایر موارد'),
)

edit_status = (
    ('دارد', 'دارد'),
    ('ندارد', 'ندارد'),
)

hagh_ab_status = (
    ('چاه', 'چاه'),
    ('رودخانه', 'رودخانه'),
    ('چشمه', 'چشمه'),
    ('سایر موارد', 'سایر موارد'),
)

system_ab_status = (
    ('مکانیزه', 'مکانیزه'),
    ('غرق آبی', 'غرق آبی'),
)

bam_status = (
    ('اسپانیش', 'اسپانیش'),
    ('شیروانی', 'شیروانی'),
    ('مسطح سنتی', 'مسطح سنتی'),
    ('روف گاردن', 'روف گاردن'),
    ('سایر موارد', 'سایر موارد'),
)

kaf_status = (
    ('سنگ', 'سنگ'),
    ('سرامیک', 'سرامیک'),
    ('سایر', 'سایر'),
)

kichen_status = (
    ('اپن', 'اپن'),
    ('نیمه اپن', 'نیمه اپن'),
    ('کلوز', 'کلوز'),
)

garmayesh_status = (
    ('خورشیدی', 'خورشیدی'),
    ('موتور خانه', 'موتور خانه'),
    ('پکیج', 'پکیج'),
    ('چیلر', 'چیلر'),
)

system_garmayesh_status = (
    ('از کف', 'از کف'),
    ('بخاری', 'بخاری'),
    ('رادیاتور', 'رادیاتور'),
    ('شومینه', 'شومینه'),
    ('فن کویل', 'فن کوِیل'),
)

sarmayesh_status = (
    ('کولر آبی', 'کولر آبی'),
    ('کولر گازی', 'کولر گازی'),
    ('فن کویل', 'فن کویل'),
)

parking_status = (
    ('مسقف', 'مسقف'),
    ('فضا باز', 'فضا باز'),
    ('ندارد', 'ندارد'),
)
 
other_fitures = (
    ('سونا', 'سونا'),
    ('استخر سرپوشیده', 'استخر سر پوشیده'),
    ('استخر گرم', 'استخر گرم'),
    ('استخر سرد', 'استخر سرد'),
)

zelzele_status = (
    ('عالی', 'عالی'),
    ('خوب', 'خوب'),
    ('متوسط', 'متوسط'),
    ('بد', 'بد'),
)

javaz_villa_status = (
    ('دفترچه ساخت', 'دفترچه ساخت'),
    ('عدم خلاف', 'عدم خلاف'),
    ('پایان کار', 'پایان کار'),
)

mechanic_biulding_status = (
    ('فلزی', 'فلزی'),
    ('بتنی', 'بتنی'),
    ('نیمه اسکلت', 'نیمه اسکلت'),
    ('سایر', 'سایر'),
)

karbari_khas_status = (
    ('کارگاهی', 'کارگاهی'),
    ('تجاری', 'تجاری'),
    ('موقعیت تجاری', 'موقعیت تجاری'),
    ('سایر موارد', 'سایر موارد'),
)

sokonat_status = (
    ('دارد', 'دارد'),
    ('ندارد', 'ندارد'),
)

melk_status = (
    ('زمین', 'زمین'),
    ('باغ', 'باغ'),
    ('ویلا', 'ویلا'),
    ('آپارتمان', 'آپارتمان'),
    ('مستغلات', 'مستغلات'),
    ('خانه', 'خانه'),
    ('مغازه', 'مغازه'),
)

class Khane(models.Model):
    superuser = models.ForeignKey(User, on_delete=models.CASCADE)
    malek_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام مالک") 
    malek_mobile = models.CharField(max_length=12, blank=True, null=True, verbose_name="تلفن مالک") 
    necessary_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن ضروری") 
    post_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="کد پستی") 
    area = models.CharField(max_length=100, blank=True, null=True, verbose_name="مساحت") 
    bar_zamin = models.CharField(max_length=20, blank=True, null=True, verbose_name="بر زمین") 
    gozar = models.CharField(max_length=40, blank=True, null=True, verbose_name="گذر") 
    sanad = models.CharField(max_length=50, choices=sanad_status, verbose_name="سند") 
    position = models.CharField(max_length=50, choices=position_status, verbose_name="موقعیت") 
    karbari = models.CharField(max_length=50, choices=karbari_status, verbose_name="کاربری") 
    dastrsi = models.CharField(max_length=50, choices=dastrsi_status, verbose_name="دسترسی") 
    topography = models.CharField(max_length=50, choices=topography_status, verbose_name="توپوگرافی") 
    javaz = models.CharField(max_length=50, choices=javaz_status, verbose_name="جواز") 
    ensheabat = models.CharField(max_length=100, verbose_name="انشعابات") 
    baft = models.CharField(max_length=50, choices=baft_status, verbose_name="بافت") 
    view = models.CharField(max_length=50, choices=view_status, verbose_name="چشم انداز") 
    malek_need = models.CharField(max_length=50, choices=malek_need_status, verbose_name="نیاز مالک") 
    features = models.CharField(max_length=50, choices=features_status, verbose_name="ویژگی ها") 
    edit = models.CharField(max_length=50, choices=edit_status, verbose_name="وضعیت اصلاحی") 
    price = models.CharField(max_length=100, null=True, blank=True, verbose_name="قیمت") 
    title = models.CharField(max_length=100, null=True, verbose_name="عنوان") 
    address = models.TextField(null=True, verbose_name="آدرس") 
    area_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="متراژ") 
    type_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="نوع ساخت") 
    build_age = models.CharField(max_length=100, blank=True, null=True, verbose_name="سال ساخت") 
    floor_count = models.CharField(max_length=100, blank=True, null=True, verbose_name="تعدا طبقات") 
    nama_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="نمای ساختمان") 
    description = models.TextField(null=True, verbose_name="توضیحات")   
    image_1 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_2 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_3 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_4 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_5 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_6 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_7 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_8 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_9 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_10 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    modified = models.DateTimeField(auto_now=True, null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    kaf = models.CharField(max_length=50, choices=kaf_status, verbose_name="کف") 
    bam = models.CharField(max_length=50, choices=bam_status, verbose_name="بام")
    kichen = models.CharField(max_length=50, choices=kichen_status, verbose_name="آشپزخانه") 
    garmayesh = models.CharField(max_length=50, choices=garmayesh_status, verbose_name="گرمایش") 
    system_garmayesh = models.CharField(max_length=50, choices=system_garmayesh_status, verbose_name="سیستم گرمایش") 
    sarmayesh = models.CharField(max_length=50, choices=sarmayesh_status, verbose_name="سرمایش") 
    parking = models.CharField(max_length=50, choices=parking_status, verbose_name="پارکینگ") 
    fitures = models.CharField(max_length=100, verbose_name="سایر ویژگی های خاص") 
    zelzele = models.CharField(max_length=50, choices=zelzele_status, verbose_name="طراحی ضد زلزله") 
    javaz_villa = models.CharField(max_length=50, choices=javaz_villa_status, verbose_name="وضعیت جواز") 
    mechanic_biulding = models.CharField(max_length=50, choices=mechanic_biulding_status, verbose_name="مکانیک ساختمان") 
    sokonat = models.CharField(max_length=50, choices=sokonat_status, verbose_name="سکونت") 

    def __str__(self):
        return self.superuser.mobile +" "+ self.address


class Mostaghelat(models.Model) :
    superuser = models.ForeignKey(User, on_delete=models.CASCADE)
    malek_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام مالک") 
    malek_mobile = models.CharField(max_length=12, blank=True, null=True, verbose_name="تلفن مالک") 
    necessary_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن ضروری") 
    post_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="کد پستی") 
    area = models.CharField(max_length=100, blank=True, null=True, verbose_name="مساحت") 
    bar_zamin = models.CharField(max_length=20, blank=True, null=True, verbose_name="بر زمین") 
    gozar = models.CharField(max_length=40, blank=True, null=True, verbose_name="گذر") 
    sanad = models.CharField(max_length=50, choices=sanad_status, verbose_name="سند") 
    position = models.CharField(max_length=50, choices=position_status, verbose_name="موقعیت") 
    karbari = models.CharField(max_length=50, choices=karbari_status, verbose_name="کاربری") 
    dastrsi = models.CharField(max_length=50, choices=dastrsi_status, verbose_name="دسترسی") 
    topography = models.CharField(max_length=50, choices=topography_status, verbose_name="توپوگرافی") 
    javaz = models.CharField(max_length=50, choices=javaz_status, verbose_name="جواز") 
    ensheabat = models.CharField(max_length=100, verbose_name="انشعابات") 
    baft = models.CharField(max_length=50, choices=baft_status, verbose_name="بافت") 
    view = models.CharField(max_length=50, choices=view_status, verbose_name="چشم انداز") 
    malek_need = models.CharField(max_length=50, choices=malek_need_status, verbose_name="نیاز مالک") 
    features = models.CharField(max_length=50, choices=features_status, verbose_name="ویژگی ها") 
    edit = models.CharField(max_length=50, choices=edit_status, verbose_name="وضعیت اصلاحی") 
    price = models.CharField(max_length=100, null=True, blank=True, verbose_name="قیمت") 
    title = models.CharField(max_length=100, null=True, verbose_name="عنوان") 
    address = models.TextField(null=True, verbose_name="آدرس")
    area_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="متراژ") 
    type_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="نوع ساخت") 
    build_age = models.CharField(max_length=100, blank=True, null=True, verbose_name="سال ساخت") 
    floor_count = models.CharField(max_length=100, blank=True, null=True, verbose_name="تعدا طبقات") 
    nama_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="نمای ساختمان") 
    description = models.TextField(null=True, verbose_name="توضیحات")  
    image_1 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_2 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_3 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_4 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_5 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_6 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_7 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_8 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_9 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_10 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر")  
    modified = models.DateTimeField(auto_now=True, null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    kaf = models.CharField(max_length=50, choices=kaf_status, verbose_name="کف") 
    bam = models.CharField(max_length=50, choices=bam_status, verbose_name="بام")
    kichen = models.CharField(max_length=50, choices=kichen_status, verbose_name="آشپزخانه") 
    garmayesh = models.CharField(max_length=50, choices=garmayesh_status, verbose_name="گرمایش") 
    system_garmayesh = models.CharField(max_length=50, choices=system_garmayesh_status, verbose_name="سیستم گرمایش") 
    sarmayesh = models.CharField(max_length=50, choices=sarmayesh_status, verbose_name="سرمایش") 
    parking = models.CharField(max_length=50, choices=parking_status, verbose_name="پارکینگ")
    zelzele = models.CharField(max_length=50, choices=zelzele_status, verbose_name="طراحی ضد زلزله") 
    javaz_villa = models.CharField(max_length=50, choices=javaz_villa_status, verbose_name="وضعیت جواز") 
    mechanic_biulding = models.CharField(max_length=50, choices=mechanic_biulding_status, verbose_name="مکانیک ساختمان")
    floor = models.CharField(max_length=50, blank=True, null=True, verbose_name="طبقه") 
    asansor = models.CharField(max_length=50, blank=True, null=True, verbose_name="آسانسور") 
    varase = models.CharField(max_length=50, blank=True, null=True, verbose_name="ورثه") 
    num_malek = models.CharField(max_length=50, blank=True, null=True, verbose_name="تعداد مالک") 
    others = models.CharField(max_length=100, blank=True, null=True, verbose_name="سایر موارد") 

    def __str__(self):
        return self.superuser.mobile +" "+ self.address


class Apartment(models.Model) :
    superuser = models.ForeignKey(User, on_delete=models.CASCADE)
    malek_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام مالک") 
    malek_mobile = models.CharField(max_length=12, blank=True, null=True, verbose_name="تلفن مالک") 
    necessary_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن ضروری") 
    post_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="کد پستی") 
    area = models.CharField(max_length=100, blank=True, null=True, verbose_name="مساحت")
    bar_zamin = models.CharField(max_length=20, blank=True, null=True, verbose_name="بر زمین") 
    gozar = models.CharField(max_length=40, blank=True, null=True, verbose_name="گذر") 
    sanad = models.CharField(max_length=50, choices=sanad_status, verbose_name="سند") 
    position = models.CharField(max_length=50, choices=position_status, verbose_name="موقعیت") 
    karbari = models.CharField(max_length=50, choices=karbari_status, verbose_name="کاربری") 
    dastrsi = models.CharField(max_length=50, choices=dastrsi_status, verbose_name="دسترسی") 
    topography = models.CharField(max_length=50, choices=topography_status, verbose_name="توپوگرافی") 
    javaz = models.CharField(max_length=50, choices=javaz_status, verbose_name="جواز") 
    ensheabat = models.CharField(max_length=100, verbose_name="انشعابات") 
    baft = models.CharField(max_length=50, choices=baft_status, verbose_name="بافت") 
    view = models.CharField(max_length=50, choices=view_status, verbose_name="چشم انداز") 
    malek_need = models.CharField(max_length=50, choices=malek_need_status, verbose_name="نیاز مالک") 
    features = models.CharField(max_length=50, choices=features_status, verbose_name="ویژگی ها") 
    edit = models.CharField(max_length=50, choices=edit_status, verbose_name="وضعیت اصلاحی") 
    price = models.CharField(max_length=100, null=True, blank=True, verbose_name="قیمت") 
    title = models.CharField(max_length=100, null=True, verbose_name="عنوان") 
    address = models.TextField(null=True, verbose_name="آدرس") 
    area_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="متراژ بنا") 
    type_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="نوع ساخت") 
    build_age = models.CharField(max_length=100, blank=True, null=True, verbose_name="سال ساخت") 
    floor_count = models.CharField(max_length=100, blank=True, null=True, verbose_name="تعداد طبقات") 
    floor = models.CharField(max_length=50, blank=True, null=True, verbose_name="طبقه") 
    vahed_count = models.CharField(max_length=50, blank=True, null=True, verbose_name="تعداد واحد") 
    asansor = models.CharField(max_length=50, blank=True, null=True, verbose_name="آسانسور") 
    vahed = models.CharField(max_length=100, blank=True, null=True, verbose_name="واحد") 
    nama_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="نمای ساختمان") 
    description = models.TextField(null=True, verbose_name="توضیحات")    
    image_1 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_2 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_3 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_4 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_5 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_6 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_7 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_8 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_9 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_10 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر")  
    modified = models.DateTimeField(auto_now=True, null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    kaf = models.CharField(max_length=50, choices=kaf_status, verbose_name="کف") 
    bam = models.CharField(max_length=50, choices=bam_status, verbose_name="بام")
    kichen = models.CharField(max_length=50, choices=kichen_status, verbose_name="آشپزخانه") 
    garmayesh = models.CharField(max_length=50, choices=garmayesh_status, verbose_name="گرمایش") 
    system_garmayesh = models.CharField(max_length=50, choices=system_garmayesh_status, verbose_name="سیستم گرمایش") 
    sarmayesh = models.CharField(max_length=50, choices=sarmayesh_status, verbose_name="سرمایش") 
    parking = models.CharField(max_length=50, choices=parking_status, verbose_name="پارکینگ")
    fitures = models.CharField(max_length=100, verbose_name="ویژگی ها") 
    zelzele = models.CharField(max_length=50, choices=zelzele_status, verbose_name="طراحی ضد زلزله") 
    mechanic_biulding = models.CharField(max_length=50, choices=mechanic_biulding_status, verbose_name="مکانیک ساختمان") 

    def __str__(self) :
        return self.superuser.mobile +" "+ self.address
    
    def jcreated(self) :
        return jalali_converter(self.created) 


class Villa(models.Model) :
    superuser = models.ForeignKey(User, on_delete=models.CASCADE)
    malek_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام مالک")  
    malek_mobile = models.CharField(max_length=12, blank=True, null=True, verbose_name="تلفن مالک") 
    necessary_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن ضروری") 
    post_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="کد پستی") 
    area = models.CharField(max_length=100, blank=True, null=True, verbose_name="مساحت") 
    bar_zamin = models.CharField(max_length=20, blank=True, null=True, verbose_name="بر زمین") 
    gozar = models.CharField(max_length=40, blank=True, null=True, verbose_name="گذر") 
    sanad = models.CharField(max_length=50, choices=sanad_status, verbose_name="سند") 
    position = models.CharField(max_length=50, choices=position_status, verbose_name="موقعیت") 
    karbari = models.CharField(max_length=50, choices=karbari_status, verbose_name="کاربری") 
    dastrsi = models.CharField(max_length=50, choices=dastrsi_status, verbose_name="دسترسی") 
    topography = models.CharField(max_length=50, choices=topography_status, verbose_name="توپوگرافی") 
    javaz = models.CharField(max_length=50, choices=javaz_status, verbose_name="جواز") 
    ensheabat = models.CharField(max_length=100, verbose_name="انشعابات") 
    baft = models.CharField(max_length=50, choices=baft_status, verbose_name="بافت") 
    view = models.CharField(max_length=50, choices=view_status, verbose_name="چشم انداز") 
    malek_need = models.CharField(max_length=50, choices=malek_need_status, verbose_name="نیاز مالک") 
    features = models.CharField(max_length=50, choices=features_status, verbose_name="ویژگی ها") 
    edit = models.CharField(max_length=50, choices=edit_status, verbose_name="وضعیت اصلاحی") 
    price = models.CharField(max_length=100, null=True, blank=True, verbose_name="قیمت") 
    title = models.CharField(max_length=100, null=True, verbose_name="عنوان") 
    address = models.TextField(null=True, verbose_name="آدرس")
    area_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="متراژ بنا") 
    type_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="نوع ساخت") 
    build_age = models.CharField(max_length=100, blank=True, null=True, verbose_name="سال ساخت") 
    floor_count = models.CharField(max_length=100, blank=True, null=True, verbose_name="تعداد طبقات") 
    nama_building = models.CharField(max_length=100, blank=True, null=True, verbose_name="نمای ساختمان") 
    description = models.TextField(null=True, verbose_name="توضیحات")  
    image_1 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_2 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_3 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_4 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_5 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_6 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_7 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_8 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_9 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_10 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    modified = models.DateTimeField(auto_now=True, null=True, blank=True) 
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True) 
    kaf = models.CharField(max_length=50, choices=kaf_status, verbose_name="کف") 
    bam = models.CharField(max_length=50, choices=bam_status, verbose_name="بام")
    kichen = models.CharField(max_length=50, choices=kichen_status, verbose_name="آشپزخانه") 
    garmayesh = models.CharField(max_length=50, choices=garmayesh_status, verbose_name="گرمایش") 
    system_garmayesh = models.CharField(max_length=50, choices=system_garmayesh_status, verbose_name="سیستم گرمایش") 
    sarmayesh = models.CharField(max_length=50, choices=sarmayesh_status, verbose_name="سرمایش") 
    parking = models.CharField(max_length=50, choices=parking_status, verbose_name="پارکینگ") 
    fitures = models.CharField(max_length=100, verbose_name="سایر ویژگی های خاص") 
    zelzele = models.CharField(max_length=50, choices=zelzele_status, verbose_name="طراحی ضد زلزله ") 
    javaz_villa = models.CharField(max_length=50, choices=javaz_villa_status, verbose_name="جواز ویلا") 
    mechanic_biulding = models.CharField(max_length=50, choices=mechanic_biulding_status, verbose_name="مکانیک ساختمان") 
    amniat = models.CharField(max_length=50, choices=system_amniat, verbose_name="سیستم امنیت") 


    def __str__(self) :
        return self.superuser.mobile +" "+ self.address

    def jcreated(self) :
        return jalali_converter(self.created) 


class Zamin(models.Model) :
    superuser = models.ForeignKey(User, on_delete=models.CASCADE)
    malek_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام مالک")  
    malek_mobile = models.CharField(max_length=12, blank=True, null=True, verbose_name="تلفن مالک") 
    necessary_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن ضروری") 
    address = models.TextField(null=True, verbose_name="آدرس")
    post_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="کد پستی") 
    area = models.CharField(max_length=50, blank=True, null=True, verbose_name="مساحت") 
    bar_zamin = models.CharField(max_length=20, blank=True, null=True, verbose_name="بر زمین") 
    gozar = models.CharField(max_length=40, blank=True, null=True, verbose_name="گذر") 
    sanad = models.CharField(max_length=50, choices=sanad_status, verbose_name="سند") 
    position = models.CharField(max_length=50, choices=position_status, verbose_name="موقعیت") 
    karbari = models.CharField(max_length=50, choices=karbari_status, verbose_name="کاربری") 
    dastrsi = models.CharField(max_length=50, choices=dastrsi_status, verbose_name="دسترسی") 
    topography = models.CharField(max_length=50, choices=topography_status, verbose_name="توپوگرافی") 
    baft = models.CharField(max_length=50, choices=baft_status, verbose_name="بافت") 
    javaz = models.CharField(max_length=50, choices=javaz_status, verbose_name="جواز") 
    ensheabat = models.CharField(max_length=100, verbose_name="انشعابات") 
    view = models.CharField(max_length=50, choices=view_status, verbose_name="چشم انداز") 
    malek_need = models.CharField(max_length=50, choices=malek_need_status, verbose_name="نیاز مالک") 
    features = models.CharField(max_length=50, choices=features_status, verbose_name="ویژگی ها") 
    edit = models.CharField(max_length=50, choices=edit_status, verbose_name="وضعیت اصلاحی") 
    price = models.CharField(max_length=100, null=True, blank=True, verbose_name="قیمت") 
    title = models.CharField(max_length=100, null=True, verbose_name="عنوان") 
    description = models.TextField(null=True, verbose_name="توضیحات")    
    image_1 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_2 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_3 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_4 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_5 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_6 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_7 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_8 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_9 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_10 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر")   
    modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="")
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="")

    def __str__(self):
        return self.superuser.mobile +" "+ self.address
    
    def jcreated(self):
        return jalali_converter(self.created)


class Maqaze(models.Model):
    superuser = models.ForeignKey(User, on_delete=models.CASCADE)
    malek_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام مالک")  
    malek_mobile = models.CharField(max_length=12, blank=True, null=True, verbose_name="تلفن مالک") 
    necessary_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن ضروری") 
    post_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="کد پستی") 
    area = models.CharField(max_length=50, blank=True, null=True, verbose_name="مساحت")
    bar_zamin = models.CharField(max_length=20, blank=True, null=True, verbose_name="بر زمین") 
    gozar = models.CharField(max_length=40, blank=True, null=True, verbose_name="گذر") 
    sanad = models.CharField(max_length=50, choices=sanad_status, verbose_name="سند") 
    position = models.CharField(max_length=50, choices=position_status, verbose_name="موقعیت") 
    karbari = models.CharField(max_length=50, choices=karbari_status, verbose_name="کاربری") 
    dastrsi = models.CharField(max_length=50, choices=dastrsi_status, verbose_name="دسترسی") 
    topography = models.CharField(max_length=50, choices=topography_status, verbose_name="توپوگرافی") 
    javaz = models.CharField(max_length=50, choices=javaz_status, verbose_name="جواز") 
    ensheabat = models.CharField(max_length=100, verbose_name="انشعابات")  
    baft = models.CharField(max_length=50, choices=baft_status, verbose_name="بافت") 
    view = models.CharField(max_length=50, choices=view_status, verbose_name="چشم انداز") 
    malek_need = models.CharField(max_length=50, choices=malek_need_status, verbose_name="نیاز مالک") 
    features = models.CharField(max_length=50, choices=features_status, verbose_name="ویژگی ها") 
    edit = models.CharField(max_length=50, choices=edit_status, verbose_name="وضعیت اصلاحی") 
    price = models.CharField(max_length=100, null=True, blank=True, verbose_name="قیمت") 
    title = models.CharField(max_length=100, null=True, verbose_name="عنوان") 
    address = models.TextField(null=True, verbose_name="آدرس")
    description = models.TextField(null=True, verbose_name="توضیحات")   
    image_1 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_2 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_3 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_4 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_5 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_6 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_7 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_8 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_9 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_10 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    sarqofli = models.CharField(max_length=100, blank=True, null=True, verbose_name="سرقفلی")
    malekiat = models.CharField(max_length=100, blank=True, null=True, verbose_name="مالکیت")
    karbari_khas = models.CharField(max_length=50, choices=karbari_khas_status, verbose_name="کاربری خاص")


    def __str__(self):
        return self.superuser.mobile +" "+ self.address
    
    def jcreated(self):
        return jalali_converter(self.created)


class Bagh(models.Model):
    superuser = models.ForeignKey(User, on_delete=models.CASCADE)
    malek_name = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام مالک")  
    malek_mobile = models.CharField(max_length=12, blank=True, null=True, verbose_name="تلفن مالک") 
    necessary_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن ضروری") 
    post_code = models.CharField(max_length=20, blank=True, null=True, verbose_name="کد پستی") 
    area = models.CharField(max_length=50, blank=True, null=True, verbose_name="مساحت")
    bar_zamin = models.CharField(max_length=20, blank=True, null=True, verbose_name="بر زمین") 
    gozar = models.CharField(max_length=40, blank=True, null=True, verbose_name="گذر") 
    sanad = models.CharField(max_length=50, choices=sanad_status, verbose_name="سند") 
    position = models.CharField(max_length=50, choices=position_status, verbose_name="موقعیت") 
    karbari = models.CharField(max_length=50, choices=karbari_status, verbose_name="کاربری") 
    dastrsi = models.CharField(max_length=50, choices=dastrsi_status, verbose_name="دسترسی") 
    topography = models.CharField(max_length=50, choices=topography_status, verbose_name="توپوگرافی") 
    javaz = models.CharField(max_length=50, choices=javaz_status, verbose_name="جواز") 
    ensheabat = models.CharField(max_length=100, verbose_name="انشعابات") 
    baft = models.CharField(max_length=50, choices=baft_status, verbose_name="بافت") 
    view = models.CharField(max_length=50, choices=view_status, verbose_name="چشم انداز") 
    malek_need = models.CharField(max_length=50, choices=malek_need_status, verbose_name="نیاز مالک") 
    features = models.CharField(max_length=50, choices=features_status, verbose_name="ویژگی ها") 
    edit = models.CharField(max_length=50, choices=edit_status, verbose_name="وضعیت اصلاحی") 
    price = models.CharField(max_length=100, null=True, blank=True, verbose_name="قیمت") 
    title = models.CharField(max_length=100, null=True, verbose_name="عنوان") 
    address = models.TextField(null=True, verbose_name="آدرس")
    description = models.TextField(null=True, verbose_name="توضیحات") 
    image_1 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_2 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_3 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_4 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_5 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_6 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_7 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_8 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_9 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر") 
    image_10 = models.ImageField(blank=True, null=True, upload_to="khane", verbose_name="تصویر")  
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    hagh_ab = models.CharField(max_length=50, choices=hagh_ab_status, verbose_name="حق آب")
    system_ab = models.CharField(max_length=50, choices=system_ab_status, verbose_name="سیستم آبیاری")
    derakht = models.CharField(max_length=50, choices=derakht_type, verbose_name="نوع درخت")


    def __str__(self):
        return self.superuser.mobile +" "+ self.address
    
    def jcreated(self):
        return jalali_converter(self.created)

    
class ArchiveUser(models.Model):
    title = models.CharField(max_length=100, null=True, verbose_name="عنوان") 
    description = models.TextField(null=True, verbose_name="توضیحات") 
    name_malek = models.CharField(max_length=100, blank=True, null=True, verbose_name="نام خریدار")
    mobile_malek = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن خریدار")
    necessary_mobile = models.CharField(max_length=20, blank=True, null=True, verbose_name="تلفن ضروری")
    needed_melk = models.CharField(max_length=50, choices=melk_status, verbose_name="نوع ملک")
    needed_area = models.CharField(max_length=50, blank=True, null=True, verbose_name="مساحت")
    position = models.CharField(max_length=100, blank=True, null=True, verbose_name="موقعیت")
    melk_karbari = models.CharField(max_length=50, blank=True, null=True, verbose_name="کاربری")
    bodge = models.CharField(max_length=50, blank=True, null=True, verbose_name="بودجه")
    olaviat = models.CharField(max_length=100, blank=True, null=True, verbose_name="اولویت")
    ejra_paymankari = models.BooleanField(default=True, verbose_name="اجرای پیمانکاری")
    khadamat = models.BooleanField(default=True, verbose_name="خدمات")
    tarahi_koli = models.BooleanField(default=True, verbose_name="طراحی کلی")
    other = models.CharField(max_length=100, blank=True, null=True, verbose_name="سایر موارد")
    name_moshaver = models.CharField(max_length=50, blank=True, null=True, verbose_name="نام مشاور")
    suggest_moshaver = models.CharField(max_length=100, blank=True, null=True, verbose_name="پیشنهاد مشاور")
    features_user = models.CharField(max_length=100, blank=True, null=True, verbose_name="خصوصیات شخصی")

    def __str__(self):
        return self.name_malek
