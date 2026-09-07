from django.db import models
from django.urls import reverse


class Publication(models.Model):
    """
    Actualité / publication de l'association, ajoutée uniquement par
    l'administrateur depuis /admin/. Pas de compte utilisateur associé.
    """

    titre = models.CharField(max_length=200)
    auteur_nom = models.CharField(
        max_length=150, default="Administration", help_text="Nom affiché comme auteur de la publication."
    )
    contenu = models.TextField()
    image = models.ImageField(upload_to="publications/", blank=True, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    publiee = models.BooleanField(default=True)

    class Meta:
        ordering = ["-date_creation"]

    def get_absolute_url(self):
        return reverse("publications:publication_detail", args=[self.pk])

    def __str__(self):
        return self.titre
