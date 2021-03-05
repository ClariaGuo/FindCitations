import pdfplumber
import os
import time
import csv

path = input('Input absolute path to folder: ')
files = os.listdir(path)

with open('relation.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    header = ['Paper Name', 'Cited By']
    writer.writerow(header)

for i in range(len(files)):
    file = path + files[i]
    count = time.time()
    try:
        with pdfplumber.open(file) as pdf:

            p = round(len(pdf.pages)*0.9)
            for l in range(p, len(pdf.pages)):
                j = pdf.pages[l]
                text = j.extract_text()
                print('Scanning: [' + files[i] + '] page ' + str(l))

                for k in files:
                    if k == files[i]:
                        continue

                    if k in text:
                        with open('relation.csv', 'a', newline='') as csvfile:
                            print('An citation has been found!')
                            writer = csv.writer(csvfile, dialect='excel')
                            writer.writerow([k,files[i]])
                        # with open('relation.txt', 'a') as rel:
                        #     print('An citation has been found!')
                        #     rel.write('\'' + k + '\'' + ' has been cited by ' + '\'' + files[i] + '\'')

        print('Finished reading: [' + files[i] + '] in ' + str(round(time.time() - count, 2)) + ' seconds. ')
        pdf.close()
    except:
        print('Failed to scan ' + files[i])
        continue
