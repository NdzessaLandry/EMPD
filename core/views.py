from django.shortcuts import render

from formations.models import Formation
from publications.models import Publication


def accueil(request):
    """
    Page d'accueil : dernières publications, aperçu des formations disponibles
    gratuitement, et message invitant aux contributions libres.
    """
    context = {
        "publications": Publication.objects.filter(publiee=True)[:5],
        "formations": Formation.objects.filter(active=True)[:6],
    }
    return render(request, "core/accueil.html", context)


def a_propos(request):
    return render(request, "core/a_propos.html")
