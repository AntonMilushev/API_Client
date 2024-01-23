import psycopg2
import requests
import logging

def fetch_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        return response.json()
    except requests.RequestException as e:
        logging.error(f"Failed to fetch joke: {e}")
        return None

def save_to_database(joke):
    db_params = {
        'host': 'db',
        'port': 5432,
        'database': 'jokes',
        'user': 'user',
        'password': 'password'
    }
    try:
        with psycopg2.connect(**db_params) as connection:
            with connection.cursor() as cursor:
                cursor.execute("CREATE TABLE IF NOT EXISTS jokes (id SERIAL PRIMARY KEY,type VARCHAR(255), setup TEXT, punchline TEXT)")
                cursor.execute("INSERT INTO jokes (type, setup, punchline) VALUES (%s,%s,%s)", (joke.get('type', ''), joke.get('setup', ''), joke.get('punchline', '')))
            connection.commit()
    except psycopg2.Error as e:
        logging.error(f"Failed to save joke to database: {e}")

if __name__ == "__main__":
    joke_data = fetch_joke()
    if joke_data:
        save_to_database(joke_data)
