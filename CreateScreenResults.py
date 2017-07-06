import sqlite3
import pandas

# set up connection
conn = sqlite3.connect(
    '/Users/Aaron/Dropbox/siRNA screening/database/genome_siRNA.db')

# create a cursor
cur = conn.cursor()

# create Table plate if it does not exist
cur.execute(
    ('CREATE TABLE IF NOT EXISTS' 
    'screen_result(test_well_count INTEGER PRIMARY KEY, sup_Venus FLOAT,' 
    'sup_mcherry FLOAT, lys_Venus FLOAT, lys_mcherry FLOAT,' 
    'total_Venus_normalized FLOAT, total_mcherry_normalized FLOAT,'
    'lysate_mcherry_normalized FLOAT, percentSecretion_Venus FLOAT,'
    'percentInhibition_Venus FLOAT, Z_score FLOAT, Robust_Z_score FLOAT,' 
    'Robust_Z_score_sample_ctrl FLOAT, SSMD FLOAT, Robust_SSMD FLOAT,' 
    'geneSymbol VARCHAR, geneId VARCHAR, row CHAR(1), col INTEGER);'))

screen_result = pandas.read_excel(
    ('/Users/Aaron/Dropbox/SafireII/'
    'All plates of genome screen/'
    'Results of automated analysis sample until 5.27.2012 gene annotated.xlsx'))

for index, row in screen_result.iterrows():
    position = row['well']
    values = [
        row['test_well_count'], row['sup_venus'], row['sup_mcherry'], 
        row['lys_venus'], row['lys_mcherry'], row['total_venus_relative_ctrl'], 
        row['total_mcherry_relative_ctrl'], row['lys_mcherry_relative_ctrl'], 
        row['secretion_venus'], row['secretion_venus_percent_inhibition'], 
        row['Z_score'], row['Robust_Z_score'], row['Robust_Z_sample_control'], 
        row['SSMD'], row['SSMD_robust'], row['gene'], str(row['geneID']), 
        position[0], int(position[1:])]
#    values = str(values)[1:len(str(values))-1]
    cur.execute(
        ('INSERT INTO screen_result(test_well_count, sup_Venus, sup_mcherry,'
        ' lys_Venus, lys_mcherry, total_Venus_normalized,'
        ' total_mcherry_normalized, lysate_mcherry_normalized,'
        ' percentSecretion_Venus, percentInhibition_Venus, Z_score,'
        ' Robust_Z_score, Robust_Z_score_sample_ctrl, SSMD, Robust_SSMD,'
        ' geneSymbol, geneId, row, col)'
        ' VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'), 
        values)

# commit changes
conn.commit()

# close connections
cur.close()
conn.close()
