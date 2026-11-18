from django.db import models
from django.urls import reverse
from django.core.exceptions import ValidationError

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

    class TypeAcces(models.TextChoices):
        GRATUIT = "GRATUIT", "Gratuite"
        PAYANT = "PAYANT", "Payante"

    type_acces = models.CharField(
        "Accès",
        max_length=10,
        choices=TypeAcces.choices,
        default=TypeAcces.GRATUIT,
    )
    prix = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        null=True,
        blank=True,
        help_text="Prix en FCFA (obligatoire si la formation est payante).",
    )

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
    @property
    def est_gratuite(self):
        return self.type_acces == self.TypeAcces.GRATUIT

    def clean(self):
        super().clean()
        if self.type_acces == self.TypeAcces.PAYANT and not self.prix:
            raise ValidationError({"prix": "Indiquez un prix pour une formation payante."})
        if self.type_acces == self.TypeAcces.GRATUIT:
            self.prix = None
