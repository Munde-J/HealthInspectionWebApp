from django .urls import path
# from healthapp.models import Business_type
from .views import register_business_type
from .views import register_violation
from . import views
from .views import register_compliance
from .views import register_inspection
from .views import register_inspectionChecklist
from .views import register_followUp

from .views import edit_compliance
from .views import edit_business_type
from .views import edit_followUp
from .views import edit_violation
from .views import edit_inspection
from .views import edit_inspectionChecklist

from .views import compliance_profile
from .views import violation_profile
from .views import inspectionChecklist_profile
from .views import inspection_profile
from .views import business_type_profile
from .views import followUp_profile

app_name = "healthapp"

urlpatterns = [
    path("business_type/", views.register_business_type, name = "registration"),
    path("business_type/", views.list_business_types, name="business_type_list"),
    path("business_type/edit/<int:id/",edit_business_type, name="edit_business_type"),
    path("business_type/<int:id>",business_type_profile,name="business_type_profile"), 

    path("followUp_type/", register_followUp, name = "registration"),
    path("followUp_type/", views.list_followUp, name="followUp_list"),
    path("followUp/edit/<int:id/",edit_followUp, name="edit_followUp"),
    path("followUp/<int:id>",followUp_profile,name="followUp_profile"),

    path("inspection_type/", register_inspection, name = "registration"),
    path("inspection/", views.list_inspection, name="inspection_list"),
    path("inspection/edit/<int:id/",edit_inspection, name="edit_inspection"),
    path("inspection_type/<int:id>",inspection_profile,name="inspection_profile"),

    path("inspectionChecklist/", register_inspectionChecklist, name = "registration"),
    path("inspectionChecklist/", views.list_inspectionChecklist, name="inspectionChecklist_list"),
    path("inspectionChecklist/edit/<int:id/",edit_inspectionChecklist, name="edit_inspectionChecklist"),
    path("inspectionChecklist/<int:id>",inspectionChecklist_profile,name="inspectionChecklist_profile"),

    path("violation_type/", register_violation, name = "registration"),
    path("violation_type/", views.list_violation, name="violation_list"),
    path("violation/",edit_violation, name="violation"),
    path("violation_type/<int:id>",violation_profile,name="violation_profile"),

    path("compliance_type/", register_compliance, name = "registration"),
    path("compliance_type/", views.list_compliance, name="compliance_list"),
    path("compliance_type/edit/<int:id/",edit_compliance, name="edit_compliance"),
    path("compliance_type/<int:id>",compliance_profile,name="compliance_profile"),

]