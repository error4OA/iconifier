from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5 import uic
import emoji
import clipboard
import json
import random
import sys
import traceback
import webbrowser
import requests

lookalikes = requests.get("https://gist.githubusercontent.com/StevenACoffman/a5f6f682d94e38ed804182dc2693ed4b/raw/fa2ed09ab6f9b515ab430692b588540748412f5f/some_homoglyphs.json").json()
leet_dict = {
    'A': '4', 'a': '4', 'B': '8', 'b': '8', 'E': '3', 'e': '3', 'G': '6', 'g': '6', 'I': '1', 'i': '1',
    'O': '0', 'o': '0', 'S': '5', 's': '5', 'T': '7', 't': '7', 'Z': '2', 'z': '2',
    'C': '(', 'c': '(', 'D': '|)', 'd': '|)', 'F': '|=', 'f': '|=', 'H': '#', 'h': '#', 'K': '|<', 'k': '|<',
    'L': '1', 'l': '1', 'M': '|\\/|', 'm': '|\\/|', 'N': '|\\|', 'n': '|\\|', 'P': '|*', 'p': '|*', 'Q': '(,)',
    'q': '(,)', 'R': '|2', 'r': '|2', 'U': '|_|', 'u': '|_|', 'V': '\\/', 'v': '\\/', 'W': '\\/\\/', 'w': '\\/\\/',
    'X': '><', 'x': '><', 'Y': '`/', 'y': '`/'
}

def exception_hook(exctype, value, tb):
    tb_str = ''.join(traceback.format_tb(tb))

    errorbox = QMessageBox()
    errorbox.setWindowTitle("Error")
    errorbox.setText("An error ocurred! Click \"See details\" to view what happened. If this wasnt supposed to happen, join our discord.")
    errorbox.setWindowIcon(QIcon("assets/icon.png"))
    errorbox.setTextFormat(Qt.RichText)
    errorbox.setDetailedText("{}".format(tb_str))
    errorbox.setIcon(QMessageBox.Critical)
    errorbox.exec_()

    sys.__excepthook__(exctype, value, tb)

github_v = requests.get("https://raw.githubusercontent.com/error4OA/iconifier/main/do-not-mess/info.json").json()
curr_v = "2.5"
class iconifierWindow(QMainWindow):
    def __init__(self):
        super(iconifierWindow, self).__init__()
        uic.loadUi("assets/SOURCE_NEW.ui", self)
        iconifierWindow.setFixedSize(self, 351, 321)
        iconifierWindow.setWindowIcon(self, QIcon("assets/icon.png"))
        self.show()

        if github_v["CURR_V"] != curr_v:
            update_warn = QMessageBox()
            update_warn.setWindowTitle("Update available")
            update_warn.setText("Hey! A new version was released ({})\nDo you wish to update?".format(github_v["CURR_V"]))
            update_warn.setWindowIcon(QIcon("assets/icon.png"))
            update_warn.setIcon(QMessageBox.Warning)
            update_warn.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
            result = update_warn.exec_()
            if result == QMessageBox.Yes:
                webbrowser.open_new_tab("https://github.com/error4OA/iconifier/releases")

        self.generate.clicked.connect(self.iconify)
        self.randomStyle.stateChanged.connect(self.usesRandomStyling)
        self.randomStyle_2.stateChanged.connect(self.usesRandomTextStyling)
        self.randomIcon.stateChanged.connect(self.usesRandomIcon)
        self.copy.clicked.connect(self.copyResult)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.clear.clicked.connect(self.clearResult)
        self.save.clicked.connect(self.saveF)
        self.load.clicked.connect(self.loadF)        

    def saveF(self):
        Fdialog = QFileDialog()
        Fsave, _ = Fdialog.getSaveFileName(self, "Save settings", "./presets", "JSON file (*.json)")

        if Fsave:
            with open(Fsave, "w") as f:
                parsed_data = {
                    "icon": self.emoji.text(),
                    "text": self.text.text(),
                    "style": self.styling.currentText(),
                    "textStyle": self.textStyling.currentText(),
                    "useRandomIcon": self.randomIcon.isChecked(),
                    "useRandomT_Style": self.randomStyle_2.isChecked(),
                    "useRandomStyle": self.randomStyle.isChecked()
                }
                json.dump(parsed_data, f, indent=1)

    def loadF(self):
        Fdialog = QFileDialog()
        Fload, _ = Fdialog.getOpenFileName(self, "Load settings", "./presets", "JSON file (*.json)")

        if Fload:
            with open(Fload, "r") as f:
                data = json.load(f)
                self.text.setText(data["text"])
                self.emoji.setText(data["icon"])
                self.styling.setCurrentText(data["style"])
                self.textStyling.setCurrentText(data["textStyle"])
                self.randomIcon.setChecked(data["useRandomIcon"])
                self.randomStyle.setChecked(data["useRandomStyle"])
                self.randomStyle_2.setChecked(data["useRandomT_Style"])

        self.settingsLabel.setText(f"Text: {self.text.text()}\nIcon: {self.emoji.text()}\nUse random icon? {self.randomIcon.isChecked()}\nUse random styling? {self.randomStyle.isChecked()}\nUse random text styling? {self.randomStyle_2.isChecked()}\nStyling: {self.styling.currentText()}\nText styling: {self.textStyling.currentText()}")

    def tab_changed(self, index):
        if index == 1:
            self.settingsLabel.setText(f"Text: {self.text.text()}\nIcon: {self.emoji.text()}\nUse random icon? {self.randomIcon.isChecked()}\nUse random styling? {self.randomStyle.isChecked()}\nUse random text styling? {self.randomStyle_2.isChecked()}\nStyling: {self.styling.currentText()}\nText styling: {self.textStyling.currentText()}")

    def iconify(self):
        emojized = emoji.emojize(f":{self.emoji.text()}:", variant="emoji_type")
        possibleStyles = ["「」", "〘〙", "  "]
        possibleIcons = list(emoji.EMOJI_DATA.keys())
        selectedStyle = random.choice(possibleStyles)
        selectedIcon = random.choice(possibleIcons)
        selected = self.styling.currentText()
        if self.randomStyle_2.isChecked():
            selectedTextStyle = random.choice(["Normal", "L33t", "Lookalike"])
        else:
            selectedTextStyle = self.textStyling.currentText()
        currentText = ""
        if selectedTextStyle == "Normal":
            currentText = self.text.text()
        elif selectedTextStyle == "Lookalike":
            for letter in self.text.text():
                try:
                    currentText = currentText + random.choice(lookalikes.get(letter.lower()))
                except:
                    currentText = currentText + letter
        elif selectedTextStyle == "L33t":
            for char in self.text.text():
                if char in leet_dict:
                    currentText += leet_dict[char]
                else:
                    currentText += char
        if not self.randomStyle.isChecked():
            if selected == "(none)":
                if not self.randomIcon.isChecked():
                    self.result.setText(f"{emojized} {currentText}")
                else:
                    self.result.setText(f"{selectedIcon} {currentText}")
            else:
                if not self.randomIcon.isChecked():
                    self.result.setText(f"{selected[0]}{emojized}{selected[1]} {currentText}")
                else:
                    self.result.setText(f"{selected[0]}{selectedIcon}{selected[1]} {currentText}")
        else:
            if not self.randomIcon.isChecked():
                self.result.setText(f"{selectedStyle[0]}{emojized}{selectedStyle[1]} {currentText}")
            else:
                self.result.setText(f"{selectedStyle[0]}{selectedIcon}{selectedStyle[1]} {currentText}")

    def usesRandomStyling(self, checked):
        self.styling.setEnabled(not checked)

    def usesRandomTextStyling(self, checked):
        self.textStyling.setEnabled(not checked)

    def usesRandomIcon(self, checked):
        self.emoji.setEnabled(not checked)

    def copyResult(self):
        clipboard.copy(self.result.text())
        message_box = QMessageBox()
        message_box.setIcon(QMessageBox.Information)
        message_box.setWindowTitle("Success")
        message_box.setWindowIcon(QIcon("assets/icon.png"))
        message_box.setText("Copied to clipboard! Made by Cheesehead.")
        message_box.setStandardButtons(QMessageBox.Ok)
        message_box.exec_()

    def clearResult(self):
        self.result.clear()

sys.excepthook = exception_hook

app = QApplication([])
window = iconifierWindow()
app.exec_()