
import os
import json
import pandas as pd
from sqlalchemy import create_engine, text

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL)


def init_db():
    with engine.begin() as conn:
        conn.execute(text("""
            CREATE TABLE IF NOT EXISTS catalogue (
                id SERIAL PRIMARY KEY,
                data JSONB
            )
        """))


def load_db():
    with engine.begin() as conn:
        result = conn.execute(text("SELECT data FROM catalogue"))

        rows = result.fetchall()

        if not rows:
            return []

        return [row[0] for row in rows]


def save_db(data):
    with engine.begin() as conn:
        conn.execute(text("DELETE FROM catalogue"))

        for row in data:
            conn.execute(
                text("INSERT INTO catalogue (data) VALUES (:data)"),
                {"data": json.dumps(row)},
            )
