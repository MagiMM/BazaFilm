import sqlite3

def findMovie(search_string):
    """
    Wyszukuje filmy zawierające podany string w tytule lub danych aktorów
    """
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    
    # Wyszukiwanie filmów zawierających search_string w tytule lub aktorach
    query = '''
    SELECT * FROM movies 
    WHERE title LIKE ? OR actors LIKE ?
    '''
    search_pattern = f'%{search_string}%'
    cursor.execute(query, (search_pattern, search_pattern))
    
    results = cursor.fetchall()
    
    if results:
        print(f'\nZnaleziono {len(results)} film(ów) dla "{search_string}":')
        for row in results:
            # row[0]=ID, row[1]=title, row[2]=year, row[3]=actors
            print(f'  - {row[1]} ({row[2]}) - {row[3]}')
    else:
        print(f'\nBrak filmów zawierających "{search_string}"')
    
    db.close()
    return results

def addMovie(title, year, actors):
    """
    Dodaje nowy film do bazy danych
    """
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    
    query = 'INSERT INTO movies (title, year, actors) VALUES (?, ?, ?)'
    cursor.execute(query, (title, year, actors))
    
    db.commit()  # Zapisuje zmiany w bazie
    db.close()
    
    print(f'Dodano film: {title} ({year})')

# Oryginalny kod - wyświetlanie wszystkich filmów
db = sqlite3.connect('movies.db')
cursor = db.cursor()
cursor.execute('SELECT * FROM movies')
for row in cursor:
    print('{0} {1}'.format(row[1], row[2]))
db.close()

# Przykłady użycia funkcji findMovie
print('\n' + '='*50)
findMovie("Indi")
findMovie("Connery")
findMovie("Mat")