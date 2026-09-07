from django.db import models
from django.urls import reverse


class Categorie(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Catégories"

    def __str__(self):
        return self.nom


class Formation(models.Model):
    """
    Formation gratuite (vidéo, audio ou PDF), librement téléchargeable.
    Ajoutée et supprimée uniquement depuis l'administration Django.
    """

    class TypeFormation(models.TextChoices):
        VIDEO = "VIDEO", "Vidéo"
        AUDIO = "AUDIO", "Audio"
        PDF = "PDF", "PDF"

    titre = models.CharField(max_length=200)
    description = models.TextField()
    categorie = models.ForeignKey(
        Categorie, on_delete=models.SET_NULL, null=True, blank=True, related_name="formations"
    )
    type_formation = models.CharField(max_length=10, choices=TypeFormation.choices)
    miniature = models.ImageField(upload_to="formations/miniatures/", blank=True, null=True)

    # Contenu : fichier hébergé directement, ou lien externe (ex: vidéo YouTube/Vimeo)
    fichier = models.FileField(upload_to="formations/fichiers/", blank=True, null=True)
    lien_externe = models.URLField(blank=True, help_text="Lien externe si le contenu n'est pas hébergé ici")

    active = models.BooleanField(default=True)
    date_publication = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date_publication"]

    def get_absolute_url(self):
        return reverse("formations:formation_detail", args=[self.pk])

    def __str__(self):
        return f"{self.titre} ({self.get_type_formation_display()})"
