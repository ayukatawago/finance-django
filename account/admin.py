from django.contrib import admin
from account.models import Account, Fund, Journal

admin.site.register(Account)
admin.site.register(Fund)
admin.site.register(Journal)