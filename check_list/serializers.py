from check_list.models import LicenseRequirement, FacilityType
from rest_framework import serializers


class LicenseRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseRequirement
        fields = ['id','requirement_name', 'required_value', 'facility_type']


class FacilityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacilityType
        fields = ['id','facility_type_name']