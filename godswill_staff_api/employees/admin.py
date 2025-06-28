from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Godswill Staff Management Admin"
admin.site.register(Manager)
admin.site.register(Intern)
