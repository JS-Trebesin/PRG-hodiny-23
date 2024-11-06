import sqlite3

# vytvoření spojení s databází?
connection = sqlite3.connect("hokus.db")

# vytvoření kurzoru, který nám umoňuje navigaci po databázi a vkládání příkazů
cursor = connection.cursor()

input_color = input("Add house color: ")

#zápis do databáze
cursor.execute(
    "INSERT INTO houses (color) VALUES (?)", (input_color,)
)

#potvrzení vložení dat do databáze
connection.commit()


cursor.execute("SELECT * FROM houses")
rows = cursor.fetchall()

for row in rows:
    print(row)

# uzavření spojení s databází
connection.close()