from django.utils import timezone
from django.db import models


class Business_type(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
   
class Inspect(models.Model):
    business = models.ForeignKey(Business_type, on_delete=models.CASCADE)
    # inspector_name = models.ForeignKey(inspector_name, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    observations = models.TextField()

class Compliance(models.Model):
    business = models.ForeignKey(Business_type, on_delete=models.CASCADE)
    sanitation = models.BooleanField()
    # sanitation_rating = models.DecimalField(max_digits=3, decimal_places=1)
    water_quality = models.BooleanField()
    # water_quality_rating = models.DecimalField(max_digits=3, decimal_places=1)
    food_safety = models.BooleanField()
    # food_safety_rating = models.DecimalField(max_digits=3, decimal_places=1)
    disease_prevention = models.BooleanField()
    # disease_prevention_rating = models.DecimalField(max_digits=3, decimal_places=1)

class InspectionChecklist(models.Model):
    business = models.ForeignKey(Business_type, on_delete=models.CASCADE)
    cleanliness = models.BooleanField()
    protective_equipment = models.BooleanField()
    handwashing_equipment = models.BooleanField()

class Violation(models.Model):
    business = models.ForeignKey(Business_type, on_delete=models.CASCADE)
    # inspector = models.ForeignKey(Inspector, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    observations = models.TextField()
    violation_details = models.TextField()
    corrective_action = models.TextField()

class FollowUp(models.Model):
    violation = models.ForeignKey(Violation, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    followUp_details = models.TextField()
    followUp_status = models.TextField()
