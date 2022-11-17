from django.shortcuts import render, redirect
from .models import(
    Apartment, Villa, Zamin,
    Bagh, Mostaghelat, Maqaze,
    Khane, ArchiveUser
)
from .forms import(
    ApartmentAddForm, VillaAddForm, ZaminAddForm,
    ApartmentUpdateForm, VillaUpdateForm, ZaminUpdateForm, 
    MostaghelatAddForm, MostaghelatUpdateForm, MaqazeAddForm, MaqazeUpdateForm,
    BaghAddForm, BaghUpdateForm, ArchiveUserAddForm, ArchiveUserUpdateForm, 
    KhaneAddForm, KhaneUpdateForm
)
from django.contrib.auth.decorators import login_required
from amlak.decorators import just_admin, just_superuser



def all_views_navbar_utils(request):
    login = False
    if request.user.is_authenticated:
        login = True
    same_context = {
        "login" : login
    }
    return same_context

def delete_dict(values):
    for x in range(1, 11):
        if 'image_'+str(x) in values:
            del values['image_'+str(x)]
    del values['created']
    del values['modified']
    del values['superuser_id']
    del values['id']
    return values

def home(request):
    context = {}
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/landing.html', context)


@login_required(login_url='register')
def dashboard(request):
    context = {}
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/dashboard.html', context)


@just_superuser
@login_required(login_url='register')
def apartment_detail(request, pk):
    apartment_detail = Apartment.objects.filter(pk=pk)
    values = list(apartment_detail.values())[0]
    values = delete_dict(values)
    context = {
        'apartment_detail': apartment_detail.first(),
        'values':values.values(),
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/apartment_detail.html', context)


@just_superuser
@login_required(login_url='register')
def villa_detail(request, pk):
    villa_detail = Villa.objects.filter(pk=pk)
    values = list(villa_detail.values())[0]
    values = delete_dict(values)
    context = {
        'apartment_detail': villa_detail.first(),
        'values':values.values(),
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/villa-detail.html', context)


@just_superuser
@login_required(login_url='register')
def zamin_detail(request, pk):
    zamin_detail = Zamin.objects.filter(pk=pk)
    values = list(zamin_detail.values())[0]
    values = delete_dict(values)
    context = {
        'apartment_detail': zamin_detail.first(),
        'values':values.values(),
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/zamin-detail.html', context)


@just_superuser
@login_required(login_url='register')
def khane_detail(request, pk):
    khane_detail = Khane.objects.filter(pk=pk)
    values = list(khane_detail.values())[0]
    values = delete_dict(values)
    context = {
        'apartment_detail': khane_detail.first(),
        'values':values.values(),
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/khane_detail.html', context)


@just_superuser
@login_required(login_url='register')
def maqaze_detail(request, pk):
    maqaze_detail = Maqaze.objects.filter(pk=pk)
    values = list(maqaze_detail.values())[0]
    values = delete_dict(values)
    context = {
        'apartment_detail': maqaze_detail.first(),
        'values':values.values(),
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/maqaze_detail.html', context)


@just_superuser
@login_required(login_url='register')
def mostaghelat_detail(request, pk):
    mostaghelat_detail = Mostaghelat.objects.filter(pk=pk)
    values = list(mostaghelat_detail.values())[0]
    values = delete_dict(values)
    context = {
        'apartment_detail': mostaghelat_detail.first(),
        'values':values.values(),
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/mostaqelat_detail.html', context)


@just_superuser
@login_required(login_url='register')
def bagh_detail(request, pk):
    bagh_detail = Bagh.objects.filter(pk=pk)
    values = list(bagh_detail.values())[0]
    values = delete_dict(values)
    context = {
        'apartment_detail': bagh_detail.first(),
        'values':values.values(),
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/bagh_detail.html', context)


@just_superuser
@login_required(login_url='register')
def archive_detail(request, pk):
    archive_detail = ArchiveUser.objects.filter(pk=pk)
    values = list(archive_detail.values())[0]
    del values['id']
    context = {
        'apartment_detail': archive_detail.first(),
        'values':values.values(),
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/archive_detail.html', context)

@just_admin
@login_required(login_url='register')
def apartment_all(request):
    apartment_all = Apartment.objects.all()
    searched_list = []
    if request.method == 'POST':
        if 'action' in request.POST:
            search = request.POST['action']
            ap = apartment_all.values()
            for melk in ap:
                for value in melk:
                    if search in str(melk[value]):
                        ap_melk = Apartment.objects.filter(pk=melk['id']).first()
                        searched_list.append(ap_melk)
                        break
    if len(searched_list) == 0:
        searched_list = apartment_all
    context = {
        "apartment_all": searched_list,
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/apartment_all.html', context)


@just_admin
@login_required(login_url='register')
def villa_all(request):
    villa_all = Villa.objects.all()
    searched_list = []
    if request.method == 'POST':
        if 'action' in request.POST:
            search = request.POST['action']
            ap = villa_all.values()
            for melk in ap:
                for value in melk:
                    if search in str(melk[value]):
                        ap_melk = Villa.objects.filter(pk=melk['id']).first()
                        searched_list.append(ap_melk)
                        break
    if len(searched_list) == 0:
        searched_list = villa_all
    context = {
        "apartment_all": searched_list,
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/villa_all.html', context)


@just_admin
@login_required(login_url='register')
def zamin_all(request):
    zamin_all = Zamin.objects.all()
    searched_list = []
    if request.method == 'POST':
        if 'action' in request.POST:
            search = request.POST['action']
            ap = zamin_all.values()
            for melk in ap:
                for value in melk:
                    if search in str(melk[value]):
                        ap_melk = Zamin.objects.filter(pk=melk['id']).first()
                        searched_list.append(ap_melk)
                        break
    if len(searched_list) == 0:
        searched_list = zamin_all
    context = {
        "apartment_all": searched_list,
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/zamin_all.html', context)


@just_admin
@login_required(login_url='register')
def khane_all(request):
    khane_all = Khane.objects.all()
    searched_list = []
    if request.method == 'POST':
        if 'action' in request.POST:
            search = request.POST['action']
            ap = khane_all.values()
            for melk in ap:
                for value in melk:
                    if search in str(melk[value]):
                        ap_melk = Khane.objects.filter(pk=melk['id']).first()
                        searched_list.append(ap_melk)
                        break
    if len(searched_list) == 0:
        searched_list = khane_all
    context = {
        "apartment_all": searched_list,
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/khane_all.html', context)


@just_admin
@login_required(login_url='register')
def bagh_all(request):
    bagh_all = Bagh.objects.all()
    searched_list = []
    if request.method == 'POST':
        if 'action' in request.POST:
            search = request.POST['action']
            ap = bagh_all.values()
            for melk in ap:
                for value in melk:
                    if search in str(melk[value]):
                        ap_melk = Bagh.objects.filter(pk=melk['id']).first()
                        searched_list.append(ap_melk)
                        break
    if len(searched_list) == 0:
        searched_list = bagh_all
    context = {
        "apartment_all": searched_list,
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/bagh_all.html', context)


@just_admin
@login_required(login_url='register')
def mostaghelat_all(request):
    mostaghelat_all = Mostaghelat.objects.all()
    searched_list = []
    if request.method == 'POST':
        if 'action' in request.POST:
            search = request.POST['action']
            ap = mostaghelat_all.values()
            for melk in ap:
                for value in melk:
                    if search in str(melk[value]):
                        ap_melk = Mostaghelat.objects.filter(pk=melk['id']).first()
                        searched_list.append(ap_melk)
                        break
    if len(searched_list) == 0:
        searched_list = mostaghelat_all
    context = {
        "apartment_all": searched_list,
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/mostaqelat_all.html', context)


@just_admin
@login_required(login_url='register')
def maqaze_all(request):
    maqaze_all = Maqaze.objects.all()
    searched_list = []
    if request.method == 'POST':
        if 'action' in request.POST:
            search = request.POST['action']
            ap = maqaze_all.values()
            for melk in ap:
                for value in melk:
                    if search in str(melk[value]):
                        ap_melk = Maqaze.objects.filter(pk=melk['id']).first()
                        searched_list.append(ap_melk)
                        break
    if len(searched_list) == 0:
        searched_list = maqaze_all
    context = {
        "apartment_all": searched_list,
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/maqaze_all.html', context)


@just_admin
@login_required(login_url='register')
def archive_all(request):
    archive_all = ArchiveUser.objects.all()
    searched_list = []
    if request.method == 'POST':
        if 'action' in request.POST:
            search = request.POST['action']
            ap = archive_all.values()
            for melk in ap:
                for value in melk:
                    if search in str(melk[value]):
                        ap_melk = ArchiveUser.objects.filter(pk=melk['id']).first()
                        searched_list.append(ap_melk)
                        break
    print(searched_list)
    if len(searched_list) == 0:
        searched_list = archive_all
    context = {
        "apartment_all": searched_list,
    }
    context_sample = all_views_navbar_utils(request)
    context.update(context_sample)
    return render(request, 'dashboard/archive_all.html', context)


@just_superuser
@login_required(login_url='register')
def add_apartment(request):
    context_sample = all_views_navbar_utils(request)
    if request.method == 'POST':
        form = ApartmentAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = ApartmentAddForm()
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/apartment_add.html', context)


@just_superuser
@login_required(login_url='register')
def add_villa(request):
    context_sample = all_views_navbar_utils(request)
    if request.method == 'POST':
        form = VillaAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = VillaAddForm()
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/villa_add.html', context)


@just_superuser
@login_required(login_url='register')
def add_zamin(request):
    context_sample = all_views_navbar_utils(request)
    if request.method == 'POST':
        form = ZaminAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = ZaminAddForm()
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/villa_add.html', context)


@just_superuser
@login_required(login_url='register')
def add_mostaqelat(request):
    context_sample = all_views_navbar_utils(request)
    if request.method == 'POST':
        form = MostaghelatAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = MostaghelatAddForm()
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/mostaqelat_add.html', context)


@just_superuser
@login_required(login_url='register')
def add_bagh(request):
    context_sample = all_views_navbar_utils(request)
    if request.method == 'POST':
        form = BaghAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = BaghAddForm()
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/bagh_add.html', context)


@just_superuser
@login_required(login_url='register')
def add_khane(request):
    context_sample = all_views_navbar_utils(request)
    if request.method == 'POST':
        form = KhaneAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = KhaneAddForm()
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/khane_add.html', context)


@just_superuser
@login_required(login_url='register')
def add_maqaze(request):
    context_sample = all_views_navbar_utils(request)
    if request.method == 'POST':
        form = MaqazeAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = MaqazeAddForm()
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/maqaze_add.html', context)


@just_superuser
@login_required(login_url='register')
def add_archive(request):
    context_sample = all_views_navbar_utils(request)
    if request.method == 'POST':
        form = ArchiveUserAddForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = ArchiveUserAddForm()
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/archive_add.html', context)


@just_superuser
@login_required(login_url='register')
def update_apartment(request, pk):
    context_sample = all_views_navbar_utils(request)
    instance = Apartment.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = ApartmentUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = ApartmentUpdateForm(instance=instance)
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/apartment_update.html', context)


@just_superuser
@login_required(login_url='register')
def update_villa(request, pk):
    context_sample = all_views_navbar_utils(request)
    instance = Villa.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = VillaUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = VillaUpdateForm(instance=instance)
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/villa_update.html', context)


@just_superuser
@login_required(login_url='register')
def update_zamin(request, pk):
    context_sample = all_views_navbar_utils(request)
    instance = Zamin.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = ZaminUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = ZaminUpdateForm(instance=instance)
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/zamin_update.html', context)


@just_superuser
@login_required(login_url='register')
def update_mostaghelat(request, pk):
    context_sample = all_views_navbar_utils(request)
    instance = Mostaghelat.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = MostaghelatUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = MostaghelatUpdateForm(instance=instance)
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/mostaqelat_update.html', context)


@just_superuser
@login_required(login_url='register')
def update_khane(request, pk):
    context_sample = all_views_navbar_utils(request)
    instance = Khane.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = KhaneUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = KhaneUpdateForm(instance=instance)
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/khane_update.html', context)


@just_superuser
@login_required(login_url='register')
def update_maqaze(request, pk):
    context_sample = all_views_navbar_utils(request)
    instance = Maqaze.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = MaqazeUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = MaqazeUpdateForm(instance=instance)
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/maqaze_update.html', context)


@just_superuser
@login_required(login_url='register')
def update_bagh(request, pk):
    context_sample = all_views_navbar_utils(request)
    instance = Bagh.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = BaghUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = BaghUpdateForm(instance=instance)
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/bagh_update.html', context)


@just_superuser
@login_required(login_url='register')
def update_archive(request, pk):
    context_sample = all_views_navbar_utils(request)
    instance = ArchiveUser.objects.filter(pk=pk).first()
    if request.method == 'POST':
        form = ArchiveUserUpdateForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.superuser = request.user
            obj.save()
            return redirect('dashboard')
    else:
        form = ArchiveUserUpdateForm(instance=instance)
    context = {
        'form':form,
    }
    context.update(context_sample)
    return render(request, 'dashboard/archive_update.html', context)

