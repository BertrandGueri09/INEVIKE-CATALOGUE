# INEVOKE — Outil de Devis Solaire v2.0

## Lancement en 3 commandes

```bash
pip install -r requirements.txt
streamlit run app.py
# → http://localhost:8501
```

## Pages disponibles

| Page | Fonctionnalités |
|------|-----------------|
| 📦 Catalogue | Visualiser, filtrer, importer Excel, télécharger PDF/Excel |
| ➕ Ajouter | Ajout unitaire + ajout en masse (tableau interactif) + nouvelles catégories |
| ✏️ Modifier | Édition libre de toutes les cellules + fiche individuelle + suppression |
| 📄 Créer un devis | Sélection équipements, lignes libres, remise, TVA, PDF professionnel |

## Nouveautés v2.0
- Ajout de nouvelles catégories personnalisées
- Ajout en masse via tableau interactif (copier-coller depuis Excel)
- Édition libre de toutes les colonnes (désignation, catégorie, unité, tous les prix)
- Fiche individuelle détaillée pour modification précise
- Téléchargement catalogue en Excel ET PDF
- Lignes hors catalogue dans le devis (saisie libre de prix)
- Import Excel avec fusion intelligente (pas de doublons)
