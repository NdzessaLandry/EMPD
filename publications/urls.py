from django.urls import path

from . import views

app_name = "publications"

urlpatterns = [
    path("", views.PublicationListView.as_view(), name="liste"),
    path("<int:pk>/", views.PublicationDetailView.as_view(), name="publication_detail"),
]
