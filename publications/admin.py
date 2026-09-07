from django.contrib import admin

from .models import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    """
    L'admin Django permet nativement d'ajouter ET de supprimer des publications
    (boutons 'Ajouter Publication' et case à cocher + action 'Supprimer' dans la liste).
    """
    list_display = ("titre", "auteur_nom", "date_creation", "publiee")
    list_filter = ("publiee", "date_creation")
    search_fields = ("titre", "contenu")
