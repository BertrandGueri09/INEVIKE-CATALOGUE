# INEVOKE SARL — Outil de Devis Solaire v2.1

## Déploiement Streamlit Community Cloud

1. Pousser ce dossier sur GitHub (public ou privé)
2. Aller sur https://share.streamlit.io → New app
3. Sélectionner le repo → fichier principal : `app.py`
4. Cliquer Deploy

## Corrections v2.1 (fix erreur Streamlit Cloud)
- Remplacement de st.stop() par st.rerun() après chaque action
- Suppression de xlsxwriter des dépendances
- Ajout du fichier .streamlit/config.toml
