import random
import os
import json
from dotenv import load_dotenv
import psycopg2
from flask import Flask, jsonify

load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

app = Flask(__name__)

def insert_random_countries():
    try:
        with open("countries.json", "r", encoding="utf-8") as file:
            all_countries = json.load(file)

        random_countries = random.sample(all_countries, min(10, len(all_countries)))

        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        cursor = conn.cursor()

        for country in random_countries:
            name = country.get('name', 'Unknown')
            capital = country.get('capital', 'Unknown')
            flag = country.get('flag', '')
            subregion = country.get('subregion', 'Unknown')
            population = country.get('population', 0)

            cursor.execute("SELECT 1 FROM countries WHERE name = %s", (name,))
            exists = cursor.fetchone()

            if not exists:
                cursor.execute("""
                    INSERT INTO countries (name, capital, flag, subregion, population)
                    VALUES (%s, %s, %s, %s, %s)
                """, (name, capital, flag, subregion, population))

        conn.commit()
        cursor.close()
        conn.close()
        return True, "Insertion sans doublons réussie"

    except Exception as e:
        print("❌ ERREUR :", e)
        return False, str(e)

@app.route('/insert-countries', methods=['GET'])
def insert_countries_route():
    success, message = insert_random_countries()
    if success:
        return jsonify({"message": message})
    else:
        return jsonify({"error": message}), 500

if __name__ == '__main__':
    app.run(debug=True)
