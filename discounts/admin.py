from django.contrib import admin
from .models import Discount, SpecialOffer


class DiscountAdmin(admin.ModelAdmin):
    search_fields = ('title', 'description')


admin.site.register(Discount, DiscountAdmin)
admin.site.register(SpecialOffer)






