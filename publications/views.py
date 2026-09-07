from django.views.generic import DetailView, ListView

from .models import Publication


class PublicationListView(ListView):
    """Liste publique de toutes les publications, les plus récentes en premier."""

    model = Publication
    template_name = "publications/liste.html"
    context_object_name = "publications"
    paginate_by = 10

    def get_queryset(self):
        return Publication.objects.filter(publiee=True)


class PublicationDetailView(DetailView):
    """Détail d'une publication : auteur, date, titre, contenu."""

    model = Publication
    template_name = "publications/publication_detail.html"
    context_object_name = "publication"

    def get_queryset(self):
        return Publication.objects.filter(publiee=True)
