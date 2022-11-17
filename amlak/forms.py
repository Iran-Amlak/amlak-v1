from django import forms
from user_auth.models import User
from .models import(
    Apartment, Villa, Zamin, 
    Maqaze, Mostaghelat, Bagh,
    Khane, ArchiveUser
)


class ApartmentAddForm(forms.ModelForm):

    class Meta:
        model = Apartment
        exclude = ['superuser']


class ApartmentUpdateForm(forms.ModelForm):

    class Meta:
        model = Apartment
        exclude = ['superuser']


class VillaAddForm(forms.ModelForm):

    class Meta:
        model = Villa
        exclude = ['superuser']


class VillaUpdateForm(forms.ModelForm):

    class Meta:
        model = Villa
        exclude = ['superuser']


class ZaminAddForm(forms.ModelForm):

    class Meta:
        model = Zamin
        exclude = ['superuser']


class ZaminUpdateForm(forms.ModelForm):

    class Meta:
        model = Zamin
        exclude = ['superuser']


class MaqazeAddForm(forms.ModelForm):

    class Meta:
        model = Maqaze
        exclude = ['superuser']


class MaqazeUpdateForm(forms.ModelForm):

    class Meta:
        model = Zamin
        exclude = ['superuser']


class BaghAddForm(forms.ModelForm):

    class Meta:
        model = Bagh
        exclude = ['superuser']


class BaghUpdateForm(forms.ModelForm):

    class Meta:
        model = Bagh
        exclude = ['superuser']


class KhaneAddForm(forms.ModelForm):

    class Meta:
        model = Khane
        exclude = ['superuser']


class KhaneUpdateForm(forms.ModelForm):

    class Meta:
        model = Khane
        exclude = ['superuser']


class MostaghelatAddForm(forms.ModelForm):

    class Meta:
        model = Mostaghelat
        exclude = ['superuser']


class MostaghelatUpdateForm(forms.ModelForm):

    class Meta:
        model = Mostaghelat
        exclude = ['superuser']


class ArchiveUserAddForm(forms.ModelForm):

    class Meta:
        model = ArchiveUser
        fields = '__all__'


class ArchiveUserUpdateForm(forms.ModelForm):

    class Meta:
        model = ArchiveUser
        exclude = '__all__'

