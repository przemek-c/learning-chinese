import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS cards (id INTEGER PRIMARY KEY, name TEXT, picture BLOB, sound BLOB)')

with open('image.jpg', 'rb') as file: # b is important -> binary
    image_data = file.read()
    cursor.execute("INSERT INTO cards (name, picture) VALUES (?,?)", ('car',image_data,))

# Retrieve binary data
cursor.execute("SELECT picture FROM cards WHERE id = 1")
data = cursor.fetchone()[0]

with open('stored_image.jpg', 'wb') as file:
    file.write(data)

# Commit changes and close the database connection
conn.commit()
conn.close()