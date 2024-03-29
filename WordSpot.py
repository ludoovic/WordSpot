
# todo créer un serveur flask qui affiche le dictionnaire retourné dans une page html utiliser le tuto da gerald

import PyPDF2
import textract
import os
import docxpy

def spot(filename, listWords):
    extirper = filename.split(".")[-1]

    if extirper == "docx":
        try:
            doc = docxpy.DOCReader(filename)
            doc.process()
            text = doc.data['document'].replace('\n', '')

            with open("CVs/data.txt", "w") as fichier:
                for line in text:
                    fichier.write(line)
            searchText(listWords)
        except:
            print(f"erreur de lecture du fichier {filename}")
######

    elif extirper == "pdf":
        try:
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

            num_pages = pdfReader.numPages
            count = 0
            text = ""

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
            searchText(listWords)
        except:
            print(f"erreur de lecture du fichier {filename}")
######        ######

    elif extirper == "html":
        with open(filename, "r") as rfichier:
            text = rfichier.read()
        with open("CVs/data.txt", "w") as fichier:
            for line in text:
                fichier.write(line)
        searchText(listWords)
    else:
        print("extention de fichier non gérée")


def searchText(listWords):


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
            print(f" |\t '{lower   }'  |\t {count    }   |\t {filename    }")
    except FileNotFoundError:
        print("Désole, ce fichier n'existe pas !")
    except Exception as e:
        print(e)
    else:
        print(file.read())
        file.close()
    finally:
        print("Recherche effectué !")

listWords = ["logiciel", "contact","diplome"]
listFilenames = os.listdir('CVs/')
for filename in listFilenames:
    filename = "CVs/" + filename
    print(filename)
    spot(filename, listWords)


