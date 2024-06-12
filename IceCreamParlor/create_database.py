import sqlite3

# creating ice cream parlor database
conn = sqlite3.connect('parlor_management.db')
cur = conn.cursor()

# creating tables 
cur.execute('''
    CREATE TABLE IF NOT EXISTS flavors (
        flavor_id INTEGER PRIMARY KEY,
        flavor_name TEXT NOT NULL,
        Cost INTEGER NOT NULL
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS Ingredient (
        Ingridient_id INTEGER PRIMARY KEY,
        Ingridient_name TEXT NOT NULL,
        Quantity INTEGER 
        Price INTEGER
    )
    ''')
    
cur.execute('''
    CREATE TABLE IF NOT EXISTS Customer (
        Customer_id INTEGER PRIMARY KEY,
        Customer_name TEXT NOT NULL
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS  Allergens (
        Allergen_name TEXT ,
        Customer_id INTEGER ,
        FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
    )
    ''')

cur.execute('''
    CREATE TABLE IF NOT EXISTS  Suggestions (
        flavour_suggestion TEXT ,
        Customer_id INTEGER ,
        FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
    )
    ''')
    
cur.execute('''
    CREATE TABLE IF NOT EXISTS  Cart (
        Customer_id INTEGER ,
        favourite_item TEXT,
        FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id)
    )
    ''')
    

#inserting values into the table
cur.execute('''
            INSERT INTO Customer VALUES (1,'a')
''')
cur.execute('''
            INSERT INTO Customer VALUES (2,'b')
''')
cur.execute('''
            INSERT INTO flavors VALUES (1,'mango',50)
''')
cur.execute('''
            INSERT INTO flavors VALUES (2,'strawberry',35)
''')
conn.commit()
cur.close()
conn.close()
    






