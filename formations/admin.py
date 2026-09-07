from django.contrib import admin

from .models import Categorie, Formation


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom", "slug")
    prepopulated_fields = {"slug": ("nom",)}


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    """Ajout et suppression de formations gérés nativement par l'admin Django."""
    list_display = ("titre", "type_formation", "categorie", "active", "date_publication")
    list_filter = ("type_formation", "active", "categorie")
    search_fields = ("titre", "description")
