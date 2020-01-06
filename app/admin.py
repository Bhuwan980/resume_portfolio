from django.contrib import admin
from .models import Contact
# Register your models here
class Contactadmin(admin.ModelAdmin):
	list_display = ('FirstName', 'LastName', 'email')
	search_fields = ('FirstName','LastName','email')
	list_per_page = 10


admin.site.register(Contact,Contactadmin)
