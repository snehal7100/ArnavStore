from django.contrib import admin
from ArnavStore.Taxes.models import Taxs

class TaxsAdmin(admin.ModelAdmin):
    list_display = ('id','sr_no', 'taxname', 'taxpercentage')  


admin.site.register(Taxs,TaxsAdmin)
