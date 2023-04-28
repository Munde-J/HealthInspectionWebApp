from rest_framework import viewsets
from rest_framework import serializers
from.serializers import Business_typeSerializer



class Business_typeViewSet(viewsets.ModelViewSet):
    queryset = Business_type.objects.all()
    serializer_class = Business_typeSerializer
class InspectViewSet(viewsets.ModelViewSet):
    queryset =Inspect.objects.all()
    serializer_class = InspectSerializer
class InspectionChecklistViewSet(viewsets.ModelViewSet):
    queryset=InspectionChecklist.objects.all()
    serializer_class= InspectionChecklistSerilaizers
class ViolationViewSet(viewsets.ModelViewSet):
    queryset=Violation.objects.all()
    serializer_class=ViolationSerializer
class ComplianceViewSet(viewsets.ModelViewSet):
    queryset=Compliance.objects.all()
    serializer_class=ComplianceSerializer
class FollowUpViewSet(viewsets.ModelViewSet):
    queryset=FollowUp.objects.all()
    serializer_class=FollowUpSerializer
