from django.contrib import admin

from .models import Categorie, Formation


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nom", "slug")
    prepopulated_fields = {"slug": ("nom",)}


@admin.register(Formation)
class FormationAdmin(admin.ModelAdmin):
    list_display = ("titre", "type_formation", "type_acces", "prix", "categorie", "active")
    list_filter = ("type_formation", "type_acces", "active", "categorie")
    search_fields = ("titre", "description")

    class Media:
        js = ("formations/admin_prix.js",)