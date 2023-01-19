from django.contrib import admin
from .models import abnormal_condition,ticket
# Register your models here.
admin.site.register(abnormal_condition)

admin.site.register(ticket)
