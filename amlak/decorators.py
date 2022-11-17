from django.http import HttpResponse
from django.shortcuts import redirect

def just_superuser(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('register')
    return wrapper_func


def just_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        else:
            return redirect('register')
    return wrapper_func
