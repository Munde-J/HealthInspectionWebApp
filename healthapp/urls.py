from django .urls import path
from healthapp.models import Business_type
from .views import register_business_type
from .views import register_violation
from . import views
from .views import register_compliance
from .views import register_inspect
from .views import register_inspectionChecklist
from .views import register_followUp

from .views import edit_compliance
from .views import edit_business_type
from .views import edit_followUp
from .views import edit_violation
from .views import edit_inspect
from .views import edit_inspectionChecklist

from .views import compliance_profile
from .views import violation_profile
from .views import inspectionChecklist_profile
from .views import inspect_profile
from .views import business_type_profile
from .views import followUp_profile

urlpatterns = [
    path("business_type/", register_business_type, name = "registration"),
    path("business_type/", views.list_business_types, name="business_type_list"),
    path("business_type/edit/<int:id/",edit_business_type, name="edit_business_type"),
    path("business_type/<int:id>",business_type_profile,name="business_type_profile"), 

    path("followUp_type/", register_followUp, name = "registration"),
    path("followUp_type/", views.list_followUp, name="followUp_list"),
    path("followUp/edit/<int:id/",edit_followUp, name="edit_followUp"),
    path("followUp/<int:id>",followUp_profile,name="followUp_profile"),

    path("inspect_type/", register_inspect, name = "registration"),
    path("inspect/", views.list_inspect, name="inspect_list"),
    path("inspect/edit/<int:id/",edit_inspect, name="edit_inspect"),
    path("inspect_type/<int:id>",inspect_profile,name="inspect_profile"),

    path("inspectionChecklist/", register_inspectionChecklist, name = "registration"),
    path("inspectionChecklist/", views.list_inspectionChecklist, name="inspectionChecklist_list"),
    path("inspectionChecklist/edit/<int:id/",edit_inspectionChecklist, name="edit_inspectionChecklist"),
    path("inspectionChecklist/<int:id>",inspectionChecklist_profile,name="inspectionChecklist_profile"),

    path("violation_type/", register_violation, name = "registration"),
    path("violation_type/", views.list_violation, name="violation_list"),
    path("violation_type/edit/<int:id/",edit_violation, name="edit_violation"),
    path("violation_type/<int:id>",violation_profile,name="violation_profile"),

    path("compliance_type/", register_compliance, name = "registration"),
    path("compliance_type/", views.list_compliance, name="compliance_list"),
    path("compliance_type/edit/<int:id/",edit_compliance, name="edit_compliance"),
    path("compliance_type/<int:id>",compliance_profile,name="compliance_profile"),

]