import sys

from tika import parser
from PySide2.QtCore import  Qt
from PySide2.QtWidgets import QLabel, QApplication, QFileDialog, QLineEdit, QWidget, QSizePolicy,QMainWindow

from ui_RadarWords import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

        # self.ui.tableView # déplacer les fichiers dans la tableView(self.putCV)
        #
        # self.ui.lineEdit.clicked.connect(self.Search)
        #
        # self.ui.Search.clicked.connect(self.tableView)
        #
        #clear avec le pushbutton Search (valueChange.connect)
        #
        # self.updateTableView()

# trouver un moyen (tika) pour rechercher un mot dans tous les fichiers selectionné (pdf,xls,txt, doc)
#
# def updateTable(self):
#     self.ui.tableView.setColumnCount(2)

# Dans la table view les cv se place dans l'ordre croissant (suivant count)


def spot(filesname, indexwords):
    try:
        file = open(filesname, "r")
        read = file.readlines()
# déplacer les fichiers dans la tableView (filesname)
# Dans la line edit taper le mot rechercher (indexwords) dans tous les fichiers placé ds la tableView
#

        for word in indexwords:
            lower = word.lower()
            count = 0
# faire un lower ds tous les fichiers
            for sentance in read:
                line = sentance.split()
# "simplifier" les mots des fichiers
                for each in line:
                    line2 = each.lower()
                    line2 = line2.strip("'#{[|`,^")
                    if lower == line2:
                        count += 1
            print(lower, " : ", count)
# quand on click sur Search .../
# remplacer les fichiers de la tableview par les bon CV, 1 fois les "indewords" trouver ( "nom.CV" | indexwords : 3(
    # "count")
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

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())