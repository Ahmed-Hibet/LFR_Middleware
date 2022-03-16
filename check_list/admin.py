from django.contrib import admin
from check_list.models import LicenseRequirement, FacilityType


admin.site.register(LicenseRequirement)
admin.site.register(FacilityType)