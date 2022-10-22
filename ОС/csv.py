#===========================================================
#Запись в cvs файл
#-----------------------------------------------------------
import csv


def write_csv(data):
    with open(CSV_FILE_NAME, 'a') as f:
        writer = csv.writer(f)
        for item in data.keys():
            writer.writerow([item, data[item]])
#===========================================================