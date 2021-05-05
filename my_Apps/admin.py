from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "MeroCare"
admin.site.site_title = "MeroCare"
admin.site.index_title = "MeroCare"


admin.site.register(Doctor)
admin.site.register(Contact)
admin.site.register(Patient)
admin.site.register(Appointment)