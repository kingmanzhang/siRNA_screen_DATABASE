import sqlite3
# set up connection
conn = sqlite3.connect('/Users/Aaron/Documents/Software-Carpentry/genome_siRNA')

# create a cursor
cur = conn.cursor()

# create Table gene_category if it does not exist
cur.execute('CREATE TABLE IF NOT EXISTS gene_category(category_id INTEGER PRIMARY KEY, category_name VARCHAR);')
cur.executescript('''
    INSERT INTO gene_category(category_id, category_name) VALUES(1, 'kinase');
    INSERT INTO gene_category(category_id, category_name) VALUES(2, 'GPCR');
    INSERT INTO gene_category(category_id, category_name) VALUES(3, 'Phosphatase');
    INSERT INTO gene_category(category_id, category_name) VALUES(4, 'IonChannel');
    INSERT INTO gene_category(category_id, category_name) VALUES(5, 'DrugTarget');
    INSERT INTO gene_category(category_id, category_name) VALUES(6, 'Genome_unknown');
    INSERT INTO gene_category(category_id, category_name) VALUES(7, 'Protease');
    INSERT INTO gene_category(category_id, category_name) VALUES(8, 'Ubiquination');
    ''')

# commit changes
conn.commit()

# close connections
cur.close()
conn.close()
