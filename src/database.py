# ======================================================
# Imports
# ======================================================

import os
import sqlite3

from datetime import datetime


# ======================================================
# Database Configuration
# ======================================================

DATABASE_DIR = "database"

DATABASE_PATH = os.path.join(
    DATABASE_DIR,
    "palmistry.db"
)

# ======================================================
# Database Manager
# ======================================================

class DatabaseManager:

    def __init__(self):

        os.makedirs(
            DATABASE_DIR,
            exist_ok=True
        )

        self.connection = sqlite3.connect(
            DATABASE_PATH,
            check_same_thread=False
        )

        self.create_table()

# ======================================================
# Create Table
# ======================================================

    def create_table(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS palm_sessions (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                session_id TEXT,

                user_name TEXT,

                created_at TEXT,

                image_quality TEXT,

                question TEXT,

                answer TEXT,

                pdf_generated TEXT

            )
            """
        )

        self.connection.commit()

# ======================================================
# Save Session
# ======================================================

    def save_session(

        self,

        session_id,

        user_name,

        image_quality,

        question,

        answer,

        pdf_generated="No"

    ):

        cursor = self.connection.cursor()

        cursor.execute(

            """
            INSERT INTO palm_sessions(

                session_id,

                user_name,

                created_at,

                image_quality,

                question,

                answer,

                pdf_generated

            )

            VALUES (?,?,?,?,?,?,?)

            """,

            (

                session_id,

                user_name,

                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                image_quality,

                question,

                answer,

                pdf_generated

            )

        )

        self.connection.commit()

# ======================================================
# Save Session
# ======================================================

    def save_session(

        self,

        session_id,

        user_name,

        image_quality,

        question,

        answer,

        pdf_generated="No"

    ):

        cursor = self.connection.cursor()

        cursor.execute(

            """
            INSERT INTO palm_sessions(

                session_id,

                user_name,

                created_at,

                image_quality,

                question,

                answer,

                pdf_generated

            )

            VALUES (?,?,?,?,?,?,?)

            """,

            (

                session_id,

                user_name,

                datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                ),

                image_quality,

                question,

                answer,

                pdf_generated

            )

        )

        self.connection.commit()

# ======================================================
# Update PDF Status
# ======================================================

    def update_pdf_status(

        self,

        session_id

    ):

        cursor = self.connection.cursor()

        cursor.execute(

            """
            UPDATE palm_sessions

            SET pdf_generated='Yes'

            WHERE session_id=?

            """,

            (
                session_id,
            )

        )

        self.connection.commit()

# ======================================================
# Database Statistics
# ======================================================

    def get_total_users(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(DISTINCT user_name)

            FROM palm_sessions

            WHERE user_name IS NOT NULL

            AND user_name != ''
            """
        )

        result = cursor.fetchone()

        return result[0] or 0


    def get_total_sessions(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM palm_sessions
            """
        )

        result = cursor.fetchone()

        return result[0] or 0


    def get_total_questions(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM palm_sessions

            WHERE question IS NOT NULL

            AND question != ''
            """
        )

        result = cursor.fetchone()

        return result[0] or 0


    def get_total_reports(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM palm_sessions

            WHERE pdf_generated='Yes'
            """
        )

        result = cursor.fetchone()

        return result[0] or 0


    def get_today_sessions(self):

        cursor = self.connection.cursor()

        today = datetime.now().strftime(
            "%Y-%m-%d"
        )

        cursor.execute(
            """
            SELECT COUNT(*)

            FROM palm_sessions

            WHERE created_at LIKE ?
            """,

            (
                f"{today}%",
            )

        )

        result = cursor.fetchone()

        return result[0] or 0

