from check_list.models import LicenseRequirement, FacilityType
from check_list.serializers import LicenseRequirementSerializer, FacilityTypeSerializer
from rest_framework import generics


class FacilityTypeList(generics.ListCreateAPIView):
    queryset = FacilityType.objects.all()
    serializer_class = FacilityTypeSerializer


class FacilityTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FacilityType.objects.all()
    serializer_class = FacilityTypeSerializer


class LicenseRequirementList(generics.ListCreateAPIView):
    queryset = LicenseRequirement.objects.all()
    serializer_class = LicenseRequirementSerializer


class LicenseRequirementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LicenseRequirement.objects.all()
    serializer_class = LicenseRequirementSerializer