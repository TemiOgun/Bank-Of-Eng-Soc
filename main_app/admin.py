from django.contrib import admin
from .models import account, message, event, alert, transaction



# Register your models here.

admin.site.register(transaction)
admin.site.register(message)
admin.site.register(event)
admin.site.register(account)
admin.site.register(alert)