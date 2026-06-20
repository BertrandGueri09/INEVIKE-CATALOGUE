import json
import streamlit as st
from supabase import create_client, Client

# ─────────────────────────────────────────────
# Connexion Supabase
# ─────────────────────────────────────────────
SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

supabase: Client = create_client(
    SUPABASE_URL,
    SUPABASE_KEY
)

# ─────────────────────────────────────────────
# Initialisation
# ─────────────────────────────────────────────
def init_db():
    pass

# ─────────────────────────────────────────────
# Catalogue
# ─────────────────────────────────────────────
def load_db():
    try:
        response = (
            supabase
            .table("catalogue")
            .select("*")
            .execute()
        )

        if response.data:
            return [row["data"] for row in response.data]

        return []

    except Exception as e:
        st.error(f"Erreur lors du chargement : {e}")
        return []


def save_db(data):
    try:

        if not data:
            return

        rows = [
            {
                "id": item["id"],
                "data": item
            }
            for item in data
        ]

        (
            supabase
            .table("catalogue")
            .upsert(rows)
            .execute()
        )

    except Exception as e:
        st.error(f"Erreur lors de la sauvegarde : {e}")


# ─────────────────────────────────────────────
# Paramètres catalogue
# ─────────────────────────────────────────────
def load_settings_db():
    try:

        response = (
            supabase
            .table("app_settings")
            .select("*")
            .eq("key", "catalogue_settings")
            .execute()
        )

        if response.data:
            return response.data[0]["value"]

        return None

    except Exception as e:
        st.error(f"Erreur chargement paramètres : {e}")
        return None


def save_settings_db(settings):
    try:

        (
            supabase
            .table("app_settings")
            .upsert(
                {
                    "key": "catalogue_settings",
                    "value": settings
                }
            )
            .execute()
        )

    except Exception as e:
        st.error(f"Erreur sauvegarde paramètres : {e}")
