import sqlite3
# set up connection
conn = sqlite3.connect(
    '/Users/Aaron/Dropbox/siRNA screening/database/genome_siRNA.db')

# create a cursor
cur = conn.cursor()

# create Table plate if it does not exist
cur.execute(
    'CREATE TABLE IF NOT EXISTS plate \
    (position INTEGER PRIMARY KEY, row CHAR(1), col CHAR(2))')

# insert all values of a plate
count = 1
rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
cols = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
for row in rows:
    for col in cols:
        values = (str(count) + ', ' + '\'' + 
                 str(row) + '\'' + ' ,' + '\'' + str(col) + '\'')
        cur.execute('INSERT INTO plate (position, row, col) VALUES (' 
                 + values + ');') 
        count += 1
conn.commit()
# close cursor and connection
cur.close() 
conn.close()
