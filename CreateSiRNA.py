import sqlite3
import pandas 


# define a function to add all records into a table
record_id = 1

def getMaxLen(dataframe):

    poolNumMax = 0
    duplexNumMax = 0
    geneSymbolMax = 0
    geneIDMax = 0
    geneAccessionMax = 0
    GINumMax = 0
    seedSeqMax = 0

    nrow = dataframe.shape[0];
    for row in range(nrow):
        if (not(pandas.isnull(dataframe.iloc[row, 0]))):
            orderNum = str(dataframe.iloc[row, 0])
            plate = int(dataframe.iloc[row, 1].split(' ')[1])
            rowID = dataframe.iloc[row, 2][:1]
            colID = dataframe.iloc[row, 2][1:]
            poolNum = dataframe.iloc[row, 3]
            duplexNum = dataframe.iloc[row, 4]
            geneSymbol = dataframe.iloc[row, 5]
            geneId = str(dataframe.iloc[row, 6])
            geneAccession = dataframe.iloc[row, 7]
            GINum =str(dataframe.iloc[row, 8])
            seedSeq = dataframe.iloc[row, 9]

            poolNumMax = max(poolNumMax, len(poolNum))
            duplexNumMax = max(duplexNumMax, len(duplexNum))
            geneSymbolMax = max(geneSymbolMax, len(geneSymbol))
            geneIDMax = max(geneIDMax, len(geneId))
            geneAccessionMax = max(geneAccessionMax, len(geneAccession))
            GINumMax = max(GINumMax, len(GINum))
            seedSeqMax = max(seedSeqMax, len(seedSeq))
        
    print('poolNumMax:', poolNumMax, 'duplexNumMax:', duplexNumMax, 'geneSymbolMax:', geneSymbolMax, 'geneIDMax:', geneIDMax, 'geneAccessionMax:', geneAccessionMax, 'GINumMax:', GINumMax, 'seedSeqMax:', seedSeqMax)


def insert_siRNAs(dataframe, cur, file_id):
    global record_id 
    nrow = dataframe.shape[0];
    for row in range(nrow):
        if (not(pandas.isnull(dataframe.iloc[row, 0]))):
            orderNum = str(dataframe.iloc[row, 0])
            plate = int(dataframe.iloc[row, 1].split(' ')[1])
            rowID = dataframe.iloc[row, 2][:1]
            colID = dataframe.iloc[row, 2][1:]
            poolNum = dataframe.iloc[row, 3]
            duplexNum = dataframe.iloc[row, 4]
            geneSymbol = dataframe.iloc[row, 5]
            geneId = str(dataframe.iloc[row, 6])
            geneAccession = dataframe.iloc[row, 7]
            GINum =str(dataframe.iloc[row, 8])
            seedSeq = dataframe.iloc[row, 9]

            values = [record_id, file_id, orderNum, plate, rowID, colID, poolNum, duplexNum, geneSymbol, geneId, geneAccession, GINum, seedSeq] 
            values = str(values)[1:(len(str(values))-1)]
            cur.execute('INSERT INTO siRNA(record_id, file_id, orderNum, plate, row, col, poolNum, duplexNum, geneSymbol, geneId, geneAccession, GINum, seedSeq) VALUES (' + values + ');')
            record_id += 1


# set up connection
conn = sqlite3.connect('/Users/Aaron/Documents/Software-Carpentry/genome_siRNA')

# create a cursor
cur = conn.cursor()

# create Table plate if it does not exist
cur.execute('CREATE TABLE IF NOT EXISTS siRNA(record_id INTEGER, file_id INTEGER, orderNum VARCHAR, plate INTEGER, row INTEGER, col INTEGER, poolNum CHAR(11), duplexNum CHAR(11), geneSymbol VARCHAR, geneId VARCHAR, geneAccession VARCHAR, GINum VARCHAR, seedSeq VARCHAR);')

folder = '/Users/Aaron/Dropbox/siRNA screening/siRNA library map/'
kinase = pandas.read_excel(folder + 'G-003505 Human Protein Kinase Lot 08105.xls', skiprows = 2)
GPCR = pandas.read_excel(folder + 'G-003605 Human GPCR Lot 080115.xls', skiprows = 2)
Phosphatase = pandas.read_excel(folder + 'G-003705 Human Phosphatase Lot 08116.xls', skiprows = 2)
IonChannel = pandas.read_excel(folder + 'G-003805 Human Ion Channel Lot 08117.xls', skiprows = 2)
DrugTargets1 = pandas.read_excel(folder + 'G-004655 Human Drug Targets Lot 08122.xls',sheetname = 0, skiprows = 2)
DrugTargets2 = pandas.read_excel(folder + 'G-004655 Human Drug Targets Lot 08122.xls', sheetname = 1,skiprows = 2)
Genome1 = pandas.read_excel(folder + 'G-005005 Human Genome Lot 08126.xls', sheetname = 0, skiprows = 2)
Genome2 = pandas.read_excel(folder + 'G-005005 Human Genome Lot 08126.xls', sheetname = 1, skiprows = 2)
Genome3 = pandas.read_excel(folder + 'G-005005 Human Genome Lot 08126.xls', sheetname = 2, skiprows = 2)
Protease = pandas.read_excel(folder + 'G-005105 Human Protease Lot 08118.xls', skiprows = 2)
Ubiquination1 = pandas.read_excel(folder + 'G-005615 Human Ubiquitin Conjugation Subset 1 Lot 08119.xls', skiprows = 2)
Ubiquination2 = pandas.read_excel(folder + 'G-005625 Human Ubiquitin Conjugation Subset 2 Lot 08120.xls', skiprows = 2)
Ubiquination3 = pandas.read_excel(folder + 'G-005635 Human Ubiquitin Conjugation Subset 3 Lot 08121.xls', skiprows = 2)

# all dataframes and their file_id
datafiles = [[kinase, 1], [GPCR, 2], [Phosphatase, 3], [IonChannel, 4], [DrugTargets1, 5], [DrugTargets2, 5], [Genome1, 6], [Genome2, 6], [Genome3, 6], [Protease, 7], [Ubiquination1, 8], [Ubiquination2, 9], [Ubiquination3, 10]]

# get max values
#for datafiles in datafiles:
#    getMaxLen(datafiles[0])

# insert values
for i in range(len(datafiles)):
    insert_siRNAs(datafiles[i][0], cur, datafiles[i][1])

# commit changes
conn.commit()

# close connections
cur.close()
conn.close()

