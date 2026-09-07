from django.urls import path

from . import views

app_name = "formations"

urlpatterns = [
    path("", views.FormationListView.as_view(), name="liste"),
    path("<int:pk>/", views.FormationDetailView.as_view(), name="formation_detail"),
    path("<int:pk>/telecharger/", views.telecharger_formation, name="telecharger"),
]
