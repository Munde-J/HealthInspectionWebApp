from django.utils import timezone
from django.db import models


class Business_type(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
   
class Inspection(models.Model):
    business = models.ForeignKey(Business_type, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    observations = models.TextField()

class Compliance(models.Model):
    business = models.ForeignKey(Business_type, on_delete=models.CASCADE)
    sanitation = models.BooleanField()
    water_quality = models.BooleanField()
    food_safety = models.BooleanField()
    disease_prevention = models.BooleanField()

class InspectionChecklist(models.Model):
    business = models.ForeignKey(Business_type, on_delete=models.CASCADE)
    cleanliness = models.BooleanField()
    protective_equipment = models.BooleanField()
    handwashing_equipment = models.BooleanField()

class Violation(models.Model):
    business = models.ForeignKey(Business_type, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    observations = models.TextField()
    violation_details = models.TextField()
    corrective_action = models.TextField()

class FollowUp(models.Model):
    violation = models.ForeignKey(Violation, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    followUp_details = models.TextField()
    followUp_status = models.TextField()
