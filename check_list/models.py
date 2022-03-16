from django.db import models


class LicenseRequirement(models.Model):
    requirement_name = models.CharField(max_length=100)
    required_value = models.IntegerField()
    facility_type = models.ForeignKey('FacilityType', on_delete=models.CASCADE)


class FacilityType(models.Model):
    facility_type_name = models.CharField(max_length=100)
