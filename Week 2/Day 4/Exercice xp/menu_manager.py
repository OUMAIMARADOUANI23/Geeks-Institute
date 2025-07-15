import psycopg2
from dotenv import load_dotenv
import os
from menu_item import MenuItem

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
            host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("SELECT item_name, item_price FROM Menu_Items WHERE item_name = %s;", (name,))
        result = cur.fetchone()
        cur.close()
        conn.close()

        if result:
            return MenuItem(result)
        return None

    @classmethod
    def all_items(cls):
        conn = psycopg2.connect(
            dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD,
            host=DB_HOST, port=DB_PORT
        )
        cur = conn.cursor()
        cur.execute("SELECT item_name, item_price FROM Menu_Items;")
        results = cur.fetchall()
        cur.close()
        conn.close()

        return [MenuItem(name, price) for name, price in results]
