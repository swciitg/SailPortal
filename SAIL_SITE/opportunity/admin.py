from django.contrib import admin
from .models import Opportunity, Role, Branch,Program,Year
# Register your models here.
admin.site.register(Role)
admin.site.register(Program)
admin.site.register(Branch)
admin.site.register(Year)
admin.site.register(Opportunity)