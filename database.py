import pandas as pd
from sqlalchemy import create_engine, text

# ⚠️ Remplace par ton vrai mot de passe Supabase
DATABASE_URL = st.secrets["DATABASE_URL"]

engine = create_engine(DATABASE_URL)


# ─────────────────────────────────────────────
# Initialisation de la table
# ─────────────────────────────────────────────
def init_db():
    with engine.connect() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS catalogue (
                id TEXT PRIMARY KEY,
                data JSONB
            )
        """))
        conn.commit()


# ─────────────────────────────────────────────
# Charger les données
# ─────────────────────────────────────────────
def load_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT data FROM catalogue"))
        rows = result.fetchall()

    return [row[0] for row in rows]


# ─────────────────────────────────────────────
# Sauvegarder les données
# ─────────────────────────────────────────────
def save_db(data):
    with engine.connect() as conn:

        # Vide ancienne base
        conn.execute(text("DELETE FROM catalogue"))

        # Réinsère tout
        for item in data:
            conn.execute(
                text("""
                    INSERT INTO catalogue (id, data)
                    VALUES (:id, :data)
                """),
                {
                    "id": item["id"],
                    "data": item
                }
            )

        conn.commit()
