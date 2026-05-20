import sqlite3
import pandas as pd
from pathlib import Path

DB_NAME = "catalogue.db"


def get_connection():
    return sqlite3.connect(DB_NAME, check_same_thread=False)


def init_db():
    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS equipements (
        id TEXT PRIMARY KEY,
        categorie TEXT,
        designation TEXT,
        unite TEXT,
        note TEXT,
        SOGELUX REAL,
        DEYE REAL,
        HONLE REAL,
        ECS REAL,
        AUTRES REAL
    )
    """)

    conn.commit()
    conn.close()


def load_db():
    conn = get_connection()

    try:
        df = pd.read_sql("SELECT * FROM equipements", conn)

        if df.empty:
            json_file = Path("equipements_db.json")

            if json_file.exists():
                import json

                with open(json_file, "r", encoding="utf-8") as f:
                    data = json.load(f)

                save_db(data)
                return data

        return df.to_dict("records")

    except Exception:
        return []

    finally:
        conn.close()


def save_db(data):
    conn = get_connection()

    try:
        df = pd.DataFrame(data)

        df.to_sql(
            "equipements",
            conn,
            if_exists="replace",
            index=False
        )

        conn.commit()

    finally:
        conn.close()