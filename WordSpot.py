# todo gérer les autres format
# todo ne pas faire de print mais spot doit retourner un dictionnaire
# todo créer un serveur flask qui affiche le dictionnaire retourné dans une page html
import csv
import numpy as np
import pandas as pd
import PyPDF2 as p2

def spot(filename, indexwords):
    # si le fichier est un fichier txt alors
    try:
        file = open(filename, "r")
        read = file.readlines()
        for word in indexwords:
            lower = word.lower()
            count = 0
            for sentance in read:
                line = sentance.split()
                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip("'#{[|`,^")
                    if lower == line2:
                        count += 1
            print(f"Le mot '{lower}' a été trouvé {count} fois dans le fichier {filename}")
    except FileNotFoundError:
        print("Désole, ce fichier n'existe pas !")
    except Exception as e:
        print(e)
    else:
        print(file.read())
        file.close()
    finally:
        print("Recherche effectué !")

    # sinon si le fichier est un fichier csv alors (DictReader de pandas)
    if filename == (str).csv:
        with open('filename.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
        return spot()

    # sinon si le fichier est un fichier doc alors
    elif filename == (str).doc:
        excel_files = ['filename.xlsx']
        for each_excel_file in excel_files:
            df = pd.read_excel(each_excel_file)
            return spot()

    # sinon si le fichier est un fichier pdf alors (import PyPDF2 as p2 pour p2.PdfFileReader)
    else:
        PDFfileObj = open("2018_CV Charte Ludovic GACHET.pdf", 'rb')
        pdfreader = p2.PdfFileReader(PDFfileObj)
        x = pdfreader.getPage(0)
        x.extractText(spot(filename, listWords))

listWords = ["partir", "fichier"]
listFilenames = ["divers.txt", "divers2.txt"]
for filename in listFilenames:
    spot(filename, listWords)