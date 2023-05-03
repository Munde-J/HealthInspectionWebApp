from django.shortcuts import render

# Create your views here.
from bdb import effective
# from locale import currency
from urllib.request import Request
from django.shortcuts import render
# import wallet
from healthapp .models import models
from django.shortcuts import redirect
from .forms import FollowUpRegistrationForm, InspectionChecklistRegistrationForm
from .models import Inspection, InspectionChecklist, Violation, Compliance, FollowUp
# from . import forms
from .forms import InspectionRegistrationForm
from .forms import ViolationRegistrationForm
from .forms import ComplianceRegistrationForm
from .forms import Business_typeRegistrationForm
from .forms import FollowUpRegistrationForm



def register_business_type(request):
    if request.method == "POST":
        form = Business_typeRegistrationForm(request.POST)
        if form.is_valid():
         form.save()
    else:
        form = Business_typeRegistrationForm()
    return render(request,"healthapp/register_business_type.html",
        {"form":form})

def register_violation(request):
    if request.method == "POST":
        form = ViolationRegistrationForm(request.POST)
        if form.is_valid():
         form.save()
    else:
        form = ViolationRegistrationForm()
    return render(request,"healthapp/register_violation.html",
        {"form":form})

def register_compliance(request):
    # form = ComplianceRegistrationForm()
    if request.method == "POST":
        form = ComplianceRegistrationForm(request.POST)
        if form.is_valid():
          form.save()
    else:
        form = ComplianceRegistrationForm()
    return render(request,"healthapp/register_compliance.html",
        {"form":form})

def register_inspection(request):
    if request.method == "POST":
        form = InspectionRegistrationForm(request.POST)
        if form.is_valid():
         form.save()
    else:
        form = InspectionRegistrationForm()
    return render(request,"healthapp/register_inspection.html",
        {"form":form})

def register_inspectionChecklist(request):
    form = InspectionChecklistRegistrationForm()
    if request.method == "POST":
        form = InspectionChecklistRegistrationForm(request.POST)
        if form.is_valid():
         form.save()
    else:
        form = InspectionChecklistRegistrationForm()
    return render(request,"healthapp/register_inspectionChecklist.html",
        {"form":form})

def register_followUp(request):
    if request.method == "POST":
        form = FollowUpRegistrationForm(request.POST)
        if form.is_valid():
         form.save()
    else:
        form = FollowUpRegistrationForm()
    return render(request,"healthapp/register_followUp.html",
        {"form":form})


