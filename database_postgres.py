import json
import streamlit as st
from sqlalchemy import create_engine, text

# ─────────────────────────────────────────────
# Connexion à la base de données
# ─────────────────────────────────────────────
DATABASE_URL = st.secrets["DATABASE_URL"]

# Compatibilité SQLAlchemy 1.4+ (postgres:// → postgresql://)
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(
    DATABASE_URL,
    connect_args={"sslmode": "require"},
)

# ─────────────────────────────────────────────
# Initialisation de la table
# ─────────────────────────────────────────────
def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS catalogue (
                id   TEXT PRIMARY KEY,
                data JSONB NOT NULL
            )
        """))

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
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM catalogue"))
        for item in data:
            conn.execute(
                text("""
                    INSERT INTO catalogue (id, data)
                    VALUES (:id, :data)
                """),
                {
                    "id":   item["id"],
                    "data": json.dumps(item, ensure_ascii=False),
                }
            )
