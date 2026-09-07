from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView

from .models import Formation


class FormationListView(ListView):
    """Catalogue public des formations gratuites, filtrable par type."""

    model = Formation
    template_name = "formations/liste.html"
    context_object_name = "formations"
    paginate_by = 12

    def get_queryset(self):
        qs = Formation.objects.filter(active=True).select_related("categorie")
        type_filtre = self.request.GET.get("type")
        if type_filtre in Formation.TypeFormation.values:
            qs = qs.filter(type_formation=type_filtre)
        return qs


class FormationDetailView(DetailView):
    model = Formation
    template_name = "formations/detail.html"
    context_object_name = "formation"

    def get_queryset(self):
        return Formation.objects.filter(active=True)


def telecharger_formation(request, pk):
    """Téléchargement libre, sans compte ni paiement."""
    formation = get_object_or_404(Formation, pk=pk, active=True)
    if formation.lien_externe:
        return redirect(formation.lien_externe)
    if formation.fichier:
        telecharger = formation.type_formation == Formation.TypeFormation.PDF
        return FileResponse(formation.fichier.open("rb"), as_attachment=telecharger)
    raise Http404("Aucun contenu disponible pour cette formation.")
