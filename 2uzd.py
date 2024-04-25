import csv

def lasit_otras_kolonnas(fails):
    otras_kolonnas_dati = []
    with open(fails, 'r') as csvfile:
        csv_lasitajs = csv.reader(csvfile)
        for rinda in csv_lasitajs:
            if len(rinda) >= 4:  



