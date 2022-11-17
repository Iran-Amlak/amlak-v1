from django.contrib import admin
from .models import (
    Apartment, Villa, Zamin, 
    Mostaghelat, Maqaze, Khane, Bagh, ArchiveUser
)

admin.site.register(Apartment)
admin.site.register(Villa)
admin.site.register(Zamin)
admin.site.register(Mostaghelat)
admin.site.register(Maqaze)
admin.site.register(Bagh)
admin.site.register(Khane)
admin.site.register(ArchiveUser)
