# todo gérer les autres format
# todo ne pas faire de print mais spot doit retourner un dictionnaire
# todo créer un serveur flask qui affiche le dictionnaire retourné dans une page html
# todo (API rest)
import csv
import numpy as np
import pandas as pd
import PyPDF2 as p2
from flask import Flask
import os

app = Flask(__name__)
app.secret_key = 'sdfghjkl'


@app.route('/keyword/')
def WordSpot():
    return "bon j'avance doucemment mais il faut trouver comment extraire des mots dans un PDF !"

def spot(filename, indexwords):
    # si le fichier est un fichier txt alors
    try:
        print(filename)
        extirper = filename.split(".")[-1]
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
    if extirper == "csv":
        with open('filename.csv', 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
        return spot()

    # sinon si le fichier est un fichier doc alors
    elif extirper == "docx":
        excel_files = ['mots cles.docx']
        for each_excel_file in excel_files:
            df = pd.read_excel(each_excel_file)
            return spot()

    # sinon si le fichier est un fichier pdf alors (import PyPDF2 as p2 pour p2.PdfFileReader)
    elif extirper == "pdf":
        with open(filename, 'rb') as PDFfileObj:
            pdfreader = p2.PdfFileReader(PDFfileObj)
            x = pdfreader.getPage(0)
            x.extractText()
    else:
        print("extention pas gerer")


listWords = ["python", "fichier"]
listFilenames = ["divers.txt", "cv mbakhane.pdf"]
for filename in listFilenames:
    spot(filename, listWords)


if __name__ == '__main__':
    app.run(debug=True)