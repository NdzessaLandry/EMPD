# Koinonia — Site vitrine

Site simple : Accueil, About us, Publications, Formations (vidéo/audio/PDF
gratuites et téléchargeables). Aucune création de compte, aucun paiement.
Seul un administrateur (superutilisateur Django) gère le contenu via /admin/.

## Installation

```bash
python3 -m venv venv
source venv/bin/activate        # Windows : venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Accès :
- Site : http://127.0.0.1:8000/
- Administration : http://127.0.0.1:8000/admin/

## Gestion du contenu (administrateur)

Depuis `/admin/` :
- **Publications** : ajouter/supprimer/modifier des actualités (titre, auteur affiché, contenu, image).
- **Formations** : ajouter/supprimer des formations vidéo, audio ou PDF —
  téléverser un fichier directement, ou renseigner un lien externe (ex: vidéo YouTube).
  Décocher "Active" pour masquer une formation sans la supprimer.

## Structure

```
koinonia/
├── core/           # Accueil, About us
├── publications/   # Liste + détail des publications
├── formations/     # Catalogue + téléchargement libre
├── templates/       # base.html + templates par app
└── static/css/style.css   # charte graphique noir/blanc
```

## Prochaines étapes possibles

- Ajouter un vrai formulaire de contact / lien de contribution (Mobile Money, virement) sur la page About us.
- Passer en production : DEBUG=False, HTTPS, base PostgreSQL si le volume de contenu grandit.
