from django.contrib import admin

from accounts.models import UserDetail, Donation, DonationRequest

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Donation)
admin.site.register(DonationRequest)
