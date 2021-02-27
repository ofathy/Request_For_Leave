from django.contrib import admin

# Register your models here.
from .models import Leave_Requests
from .form import Leave_request_form
admin.site.register(Leave_Requests)
