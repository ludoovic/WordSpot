from flask import Flask, render_template
import PyPDF2
import textract
import os
import docxpy


def spot(filename, listWords):
    extirper = filename.split(".")[-1]

    # si le fichier est un fichier docx alors
    if extirper == "docx":
        try:
            doc = docxpy.DOCReader(filename)
            doc.process()
            text = doc.data['document'].replace('\n', '')

            with open("CVs/data.txt", "w") as fichier:
                for line in text:
                    fichier.write(line)
            returnedSearch = searchText(listWords, filename)
            return returnedSearch
        except:
            print(f"erreur de lecture du fichier {filename}")
            return []

####################################################
    elif extirper == "pdf":
        try:
            pdfFileObj = open(filename, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            # discerning the number of pages will allow us to parse through all #the pages
            num_pages = pdfReader.numPages
            count = 0
            text = ""
            # The while loop will read each page
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
#####
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
    listWords = ["e-mail", "adresse", "email", "outils"]
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
    # return listOfListReturn[0][0]
    return render_template("result.html", list=listOfListReturn)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)