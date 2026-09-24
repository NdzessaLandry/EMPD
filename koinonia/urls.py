"""
URLconf racine du projet koinonia (EMPD).
Adapte les préfixes 'publications/' et 'formations/' si tes apps
utilisent déjà d'autres chemins.
"""

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # Route nécessaire pour le formulaire de changement de langue
    # (celui utilisé dans base.html, action="{% url 'set_language' %}")
    path("i18n/", include("django.conf.urls.i18n")),

    path("", include("core.urls", namespace="core")),
    path("publications/", include("publications.urls", namespace="publications")),
    path("formations/", include("formations.urls", namespace="formations")),
]

# Sert les fichiers médias (images de formations/publications) en développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
