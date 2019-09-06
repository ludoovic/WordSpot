# TODO : faire fonctionner pour doc
# TODO : corriger le problème de charmap
# TODO : permettre à l'utilisateur d'entrer les mots clés recherché via un formulaire web

from flask import Flask, render_template
import PyPDF2
import textract
import os
import docxpy


def spot(filename, listWords):
    """ The fonction spot return a number of occur of searched words ;
    listWords in this fonction, transit the request to the fonction def searchText"""

    extirper = filename.split(".")[-1]
    #   extirper est une variable qui sépare le nom du fichier avec le . & ne garde que l'extension.
    #   boucle if pour extraire des données d'un fichier docx

    if extirper == "docx":
        try:
            doc = docxpy.DOCReader(filename)
            doc.process()
    # l'import de docxpy utilise DCOreader pour extraire les données en txt
            text = doc.data['document'].replace('\n', '')
    # les données sont placé dans le dossier CVs/data.txt | puis ouvert (ci-dessous)
            with open("CVs/data.txt", "w") as fichier:
                for line in text:
                    fichier.write(line)
            returnedSearch = searchText(listWords, filename)
            return returnedSearch
        except:
            print(f"erreur de lecture du fichier {filename}")
            return []

    # boucle elif pour extraire des données d'un fichier PDF
    elif extirper == "pdf":
        try:
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # discerner le nombre de pages permet de 'parse' toutes les pages
            num_pages = pdfReader.numPages
            count = 0
            text = ""
    # la boucle while va lire chaque page
            while count < num_pages:
                pageObj = pdfReader.getPage(count)
                count += 1
                text += pageObj.extractText()
            if text != "":
                text = text
            else:
                text = textract.process(fileurl, method='tesseract', language='eng')

            with open("CVs/data.txt", "w") as fichier:
                for line in text:
                    fichier.write(line)
            returnedSearch = searchText(listWords, filename)
            return returnedSearch

        except:
            print(f"erreur de lecture du fichier {filename}")
            return []

    # boucle if pour extraire des données d'un fichier HTML
    elif extirper == "html":
        with open(filename, "r") as rfichier:
            text = rfichier.read()
        with open("CVs/data.txt", "w") as fichier:
            for line in text:
                fichier.write(line)
        returnedSearch = searchText(listWords, filename)
        return returnedSearch
    else:
        print("extention de fichier non gérée")
        return []


def searchText(listWords, filename):
    """ This fonction allow to extract all the words in CVs/data.txt """
    listDico = []

    try:
        file = open("CVs/data.txt", "r")
        read = file.readlines()
        for word in listWords:
            lower = word.lower()
            count = 0
            for sentance in read:
                line = sentance.split()
                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip("'#{[|`,^")
                    if lower == line2:
                        count += 1
            listDico.append({"nom": filename, "mot": lower, "occur": count})

    except FileNotFoundError:
        print("Désole, ce fichier n'existe pas !")
    except Exception as e:
        print(e)
    else:
        print(file.read())
        file.close()
    finally:
        return listDico

def foncPrincipale():
    """ This fonction allow to select the words searched in files in folder CVs"""
    listWords = ["python", "logistique", "voiture", "outils"]
    listFilenames = os.listdir('CVs/')
    listReturn = []
    for filename in listFilenames:
        filename = "CVs/" + filename
        listReturn.append(spot(filename, listWords))
    return listReturn

app = Flask(__name__)

@app.route('/SpotWord/')
def index():
    listOfListReturn = foncPrincipale()
    print(listOfListReturn)

    return render_template("result.html", list=listOfListReturn)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)