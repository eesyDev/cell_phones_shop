# id | name | description  | price | image | color

from db import conn, cursor

def create_table_product():
    query = """CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(150) NOT NULL,
        description TEXT,
        price INT,
        photo VARCHAR,
        color VARCHAR,
        brand VARCHAR,
        callback VARCHAR
        );"""
    cursor.execute(query=query)
    conn.commit()

# create_table_product()

def insert_product(name: str, description: str, price: str, photo: str, color: str, brand: str, callback: str):
    query = f"""
    INSERT INTO products (
        name:, description, price, photo, color, brand, callback
        )
        VALUES (
            '{name}', '{description}', {price}, '{photo}', '{color}', '{brand}', '{callback}
        );"""
    cursor.execute(query=query)
    conn.commit()

