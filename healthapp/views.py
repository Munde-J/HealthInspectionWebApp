from django.shortcuts import render

# Create your views here.
from bdb import effective
# from locale import currency
from urllib.request import Request
from django.shortcuts import render
# import wallet
from healthapp .models import healthapp
from django import redirect
from .forms import FollowUpRegistrationForm, InspectionChecklistRegistrationForm
from .models import Inspect, InspectionChecklist, Violation, Compliance, Business_type, FollowUp
# from . import forms
from .forms import InspectRegistrationForm
from .forms import ViolationRegistrationForm
from .forms import ComplianceRegistrationForm
from .forms import Business_typeRegistrationForm
from .forms import FollowUpRegistrationForm



def register_business_type(request):
    form = Business_typeRegistrationForm()
    if request.method == "POST":
        form = Business_typeRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = Business_typeRegistrationForm()
        return render(request,"business_type/register_business_type.html",
        {"form":form})

def list_business_types(request):
    business_type = business_type.objects.all()
    return business_type(request, "business_type/business_type_list.html",
    {"business_type": business_type})       
    # return render(request,"wallet/register_wallet.html",
    # {"form":form})

def business_type_profile(request,id):
    business_type = business_type.objects.get(id = id)
    return render(request,"business_type/business_type_profile.html",{"business_type":business_type})

def edit_business_type(request,id):
    business_type = business_type.objects.get(id=id)
    if request.method == "POST":
        form = Business_typeRegistrationForm(request.POST,instance=business_type)
    if form.is_valid():
            form.save()
            return redirect("business_type_profile",id=business_type.id)
    else:
        form = Business_typeRegistrationForm(instance=business_type)
        return render(request,"business_type/business_type.html",{"form":form})



def register_violation(request):
    form = ViolationRegistrationForm()
    if request.method == "POST":
        form = ViolationRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = ViolationRegistrationForm()
        return render(request,"violation/register_violation.html",
        {"form":form})

def list_violation(request):
    violation = violation.objects.all()
    return violation(request, "violation/violation_list.html",
    {"violation": violation})       
    # return render(request,"wallet/register_wallet.html",
    # {"form":form})

def violation_profile(request,id):
    violation = violation.objects.get(id = id)
    return render(request,"violation/violation_profile.html",{"violation":violation})

def edit_violation(request,id):
    violation = violation.objects.get(id=id)
    if request.method == "POST":
        form = ViolationRegistrationForm(request.POST,instance=violation)
    if form.is_valid():
            form.save()
            return redirect("violation_profile",id=violation.id)
    else:
        form = ViolationRegistrationForm(instance=violation)
        return render(request,"violation/violation.html",{"form":form})



def register_compliance(request):
    form = ComplianceRegistrationForm()
    if request.method == "POST":
        form = ComplianceRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = ComplianceRegistrationForm()
        return render(request,"compliance/register_compliance.html",
        {"form":form})

def list_compliance(request):
    compliance = compliance.objects.all()
    return compliance(request, "compliance/compliance_list.html",
    {"compliance": compliance})       
    # return render(request,"wallet/register_wallet.html",
    # {"form":form})

def compliance_profile(request,id):
    compliance = compliance.objects.get(id = id)
    return render(request,"compliance/compliance_profile.html",{"compliance":compliance})

def edit_compliance(request,id):
    compliance = compliance.objects.get(id=id)
    if request.method == "POST":
        form = ComplianceRegistrationForm(request.POST,instance=compliance)
    if form.is_valid():
            form.save()
            return redirect("compliance_profile",id=compliance.id)
    else:
        form = ComplianceRegistrationForm(instance=compliance)
        return render(request,"compliance/compliance.html",{"form":form})



def register_inspect(request):
    form = InspectRegistrationForm()
    if request.method == "POST":
        form = InspectRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = InspectRegistrationForm()
        return render(request,"inspect/register_inspect.html",
        {"form":form})

def list_inspect(request):
    inspect = inspect.objects.all()
    return inspect(request, "inspect/inspect_list.html",
    {"inspect": inspect})       
    # return render(request,"wallet/register_wallet.html",
    # {"form":form})

def inspect_profile(request,id):
    inspect = inspect.objects.get(id = id)
    return render(request,"inspect/inspect_profile.html",{"inspect":inspect})

def edit_inspect(request,id):
    inspect = inspect.objects.get(id=id)
    if request.method == "POST":
        form = InspectRegistrationForm(request.POST,instance=inspect)
    if form.is_valid():
            form.save()
            return redirect("inspect_profile",id=inspect.id)
    else:
        form = InspectRegistrationForm(instance=inspect)
        return render(request,"inspect/inspect.html",{"form":form})


def register_inspectionChecklist(request):
    form = InspectionChecklistRegistrationForm()
    if request.method == "POST":
        form = InspectionChecklistRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = InspectionChecklistRegistrationForm()
        return render(request,"inspect/register_inspect.html",
        {"form":form})

def list_inspectionChecklist(request):
    inspectionChecklist = InspectionChecklist.objects.all()
    return inspectionChecklist(request, "inspectionChecklist/inspectionChecklist_list.html",
    {"inspectionChecklist": inspectionChecklist})       
    # return render(request,"wallet/register_wallet.html",
    # {"form":form})

def inspectionChecklist_profile(request,id):
    inspectionChecklist = inspectionChecklist.objects.get(id = id)
    return render(request,"inspectionChecklist/inspectionChecklist_profile.html",{"inspectionChecklist":inspectionChecklist})

def edit_inspectionChecklist(request,id):
    inspectionChecklist = inspectionChecklist.objects.get(id=id)
    if request.method == "POST":
        form = InspectionChecklistRegistrationForm(request.POST,instance=inspectionChecklist)
    if form.is_valid():
            form.save()
            return redirect("inspectionChecklist_profile",id=inspectionChecklist.id)
    else:
        form = InspectionChecklistRegistrationForm(instance=inspectionChecklist)
        return render(request,"inspectionChecklist/inspectionChecklist.html",{"form":form})



def register_followUp(request):
    form = FollowUpRegistrationForm()
    if request.method == "POST":
        form = FollowUpRegistrationForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        form = FollowUpRegistrationForm()
        return render(request,"followUp/register_followUp.html",
        {"form":form})

def list_followUp(request):
    followUp = followUp.objects.all()
    return followUp(request, "followUp/followUp_list.html",
    {"followUp": followUp})       
    # return render(request,"wallet/register_wallet.html",
    # {"form":form})

def followUp_profile(request,id):
    followUp = followUp.objects.get(id = id)
    return render(request,"followUp/followUp_profile.html",{"followUp":followUp})

def edit_followUp(request,id):
    followUp = followUp.objects.get(id=id)
    if request.method == "POST":
        form = FollowUpRegistrationForm(request.POST,instance=followUp)
    if form.is_valid():
            form.save()
            return redirect("followUp_profile",id=followUp.id)
    else:
        form = FollowUpRegistrationForm(instance=followUp)
        return render(request,"followUp/followUp.html",{"form":form})



