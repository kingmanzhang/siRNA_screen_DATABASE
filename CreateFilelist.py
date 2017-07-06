import sqlite3
# set up connection
conn = sqlite3.connect(
    '/Users/Aaron/Dropbox/siRNA screening/database/genome_siRNA.db')

# create a cursor
cur = conn.cursor()

# create Table plate if it does not exist
cur.execute(
    'CREATE TABLE IF NOT EXISTS filelist(file_id INTEGER PRIMARY KEY, \
    category_id INTEGER, file_name TEXT);')

# readin data and insert into table
f = open(
    '/Users/Aaron/Dropbox/siRNA screening/siRNA library map/siRNA_maps.txt')
for line in f:
    line_split = line.split(',')
    if (line_split[2].rstrip() != 'file_name'):
        values = str(line_split[0]) + ', ' 
                    + str(line_split[1]) + ', ' + '\'' 
                    + line_split[2].rstrip() + '\''
        cur.execute('INSERT INTO filelist(file_id, category_id, file_name) \
                                 VALUES (' + values + ');')
# commit changes
conn.commit()

# close connection
cur.close()
conn.close()




