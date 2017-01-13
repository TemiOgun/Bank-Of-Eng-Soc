from django.contrib import admin
from .models import account, message, event, alert



# Register your models here.

admin.site.register(account)
admin.site.register(message)
admin.site.register(event)
admin.site.register(alert)