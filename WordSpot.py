# from tika import parser

import sys
from PySide2.QtWidgets import (QApplication, QWidget, QMainWindow, QDialog,)
from ui_RadarWords import Ui_MainWindow

class RadarWords(QMainWindow):
    def __init__(self):
        super(RadarWords, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        global filename
        self.mesData = {}
        self.mesdata = self.lireJSON(filename)

# trouver un moyen (tika) pour rechercher un mot dans tous les fichiers selectionné (pdf,xls,txt, doc)
def spot(filename, indexwords):
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
            print(lower, " : ", count)
    except FileNotFoundError:
        print("Désole, ce fichier n'existe pas !")
    except Exception as e:
        print(e)

    else:
        print(file.read())
        file.close()
    finally:
        print("Recherche effectué !")

spot("divers.txt", ["fichier"])


# file = 'path/to/file'
# # Parse date from file
# file_data = parser.from_title(file)
# # get files text content
# text = file_data['content']
# print(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = RadarWords()
    window.show()

    sys.exit(app.exec_())