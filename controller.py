from PyQt5.QtWidgets import *
from FinalWordle import *
import random
import time

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)

def get_random_word():
    """
    This function pulls a random word from the .txt file
    of five-letter words.
    :return: returns the chosen random word
    """
    with open("dictionary.txt", "r") as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        correct_word = random.choice(words)
        return correct_word

def check_if_user_word_passes(user_word: str):
    """
    This function checks if the word that the user input is 5 characters
    and in the dictionary file.
    :param user_word: the word that the user input
    :return: returns different values depending on different cases, so that the
    label in the GUI can display the correct image.
    """
    if (len(user_word) != 5) or (user_word.isalpha() == False):
        print('Please input a word that is five letters long')
        user_word_passes = 1
    elif in_dictionary(user_word) == False:
        print('Please input a real word.')
        user_word_passes = 2
    else:
        user_word_passes = 3
    return user_word_passes


def in_dictionary(user_word: str):
    """
    This function determines if the input word is in the dictionary.txt file or not
    :param user_word: the word that the user wants to test
    :return: ouputs true if the word is in the file, outputs false otherwise
    """
    word_in_dict = False
    with open("dictionary.txt", 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if user_word in line:
                word_in_dict = True
                break
    return word_in_dict

# chose the random word that will be the answer
correct_word = get_random_word()

class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.submit())
        self.round = 1

    def submit(self):
        """
        Determines what happens when the submit button is selected. Determines if the word is in the dictionary or not
        and returns error messages to the user if not. If it is a suitable word,then it displays that word on the appropriate row.
        :return: returns nothing
        """
        self.Main_Label_2.setText("")

        # get the word from the text input
        user_word = self.textInput.text().strip().lower()
        user_list = list(user_word)
        correct_list = list(correct_word)

        # check if the word passes
        user_word_passes = (check_if_user_word_passes(user_word))
        if user_word_passes == 1:
            self.Main_Label_2.setText("Please input a word that is five letters long")
        elif user_word_passes == 2:
            self.Main_Label_2.setText("Please input a real word")
        elif user_word_passes == 3:
            if str(user_word) == str(correct_word):
                # winning conditions
                self.Main_Label_2.setText(f'You win! The correct word is {user_word.upper()}.')
                if self.round == 1:
                    self.R1C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R1C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R1C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R1C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R1C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R1C1.setText(user_word[0].upper())
                    self.R1C2.setText(user_word[1].upper())
                    self.R1C3.setText(user_word[2].upper())
                    self.R1C4.setText(user_word[3].upper())
                    self.R1C5.setText(user_word[4].upper())
                elif self.round == 2:
                    self.R2C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R2C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R2C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R2C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R2C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R2C1.setText(user_word[0].upper())
                    self.R2C2.setText(user_word[1].upper())
                    self.R2C3.setText(user_word[2].upper())
                    self.R2C4.setText(user_word[3].upper())
                    self.R2C5.setText(user_word[4].upper())
                elif self.round == 3:
                    self.R3C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R3C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R3C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R3C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R3C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R3C1.setText(user_word[0].upper())
                    self.R3C2.setText(user_word[1].upper())
                    self.R3C3.setText(user_word[2].upper())
                    self.R3C4.setText(user_word[3].upper())
                    self.R3C5.setText(user_word[4].upper())
                elif self.round == 4:
                    self.R4C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R4C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R4C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R4C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R4C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R4C1.setText(user_word[0].upper())
                    self.R4C2.setText(user_word[1].upper())
                    self.R4C3.setText(user_word[2].upper())
                    self.R4C4.setText(user_word[3].upper())
                    self.R4C5.setText(user_word[4].upper())
                elif self.round == 5:
                    self.R5C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R5C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R5C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R5C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R5C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R5C1.setText(user_word[0].upper())
                    self.R5C2.setText(user_word[1].upper())
                    self.R5C3.setText(user_word[2].upper())
                    self.R5C4.setText(user_word[3].upper())
                    self.R5C5.setText(user_word[4].upper())
                elif self.round == 6:
                    self.R6C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R6C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R6C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R6C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R6C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                    self.R6C1.setText(user_word[0].upper())
                    self.R6C2.setText(user_word[1].upper())
                    self.R6C3.setText(user_word[2].upper())
                    self.R6C4.setText(user_word[3].upper())
                    self.R6C5.setText(user_word[4].upper())

            else:
                # setting text to correct colors
                # Row 1
                if self.round == 1:
                    # Row 1 Column 1
                    if str(user_list[0]) == str(correct_list[0]):
                        user_list[0] = user_list[0].upper()
                        self.R1C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R1C1.setText(user_list[0])
                    elif str(user_list[0]) in correct_list:
                        user_list[0] = user_list[0].upper()
                        self.R1C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R1C1.setText(user_list[0])
                    else:
                        user_list[0] = user_list[0].upper()
                        self.R1C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R1C1.setText(user_list[0])
                    # Row 1 Column 2
                    if str(user_list[1]) == str(correct_list[1]):
                        user_list[1] = user_list[1].upper()
                        self.R1C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R1C2.setText(user_list[1])
                    elif str(user_list[1]) in correct_list:
                        user_list[1] = user_list[1].upper()
                        self.R1C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R1C2.setText(user_list[1])
                    else:
                        user_list[1] = user_list[1].upper()
                        self.R1C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R1C2.setText(user_list[1])
                    # Row 1 Column 3
                    if str(user_list[2]) == str(correct_list[2]):
                        user_list[2] = user_list[2].upper()
                        self.R1C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R1C3.setText(user_list[2])
                    elif str(user_list[2]) in correct_list:
                        user_list[2] = user_list[2].upper()
                        self.R1C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R1C3.setText(user_list[2])
                    else:
                        user_list[2] = user_list[2].upper()
                        self.R1C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R1C3.setText(user_list[2])
                    # Row 1 Column 4
                    if str(user_list[3]) == str(correct_list[3]):
                        user_list[3] = user_list[3].upper()
                        self.R1C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R1C4.setText(user_list[3])
                    elif str(user_list[3]) in correct_list:
                        user_list[3] = user_list[3].upper()
                        self.R1C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R1C4.setText(user_list[3])
                    else:
                        user_list[3] = user_list[3].upper()
                        self.R1C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R1C4.setText(user_list[3])
                    # Row 1 Column 5
                    if str(user_list[4]) == str(correct_list[4]):
                        user_list[4] = user_list[4].upper()
                        self.R1C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R1C5.setText(user_list[4])
                    elif str(user_list[4]) in correct_list:
                        user_list[4] = user_list[4].upper()
                        self.R1C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R1C5.setText(user_list[4])
                    else:
                        user_list[4] = user_list[4].upper()
                        self.R1C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R1C5.setText(user_list[4])

                elif self.round == 2:
                    # Row 2 Column 1
                    if str(user_list[0]) == str(correct_list[0]):
                        user_list[0] = user_list[0].upper()
                        self.R2C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R2C1.setText(user_list[0])
                    elif str(user_list[0]) in correct_list:
                        user_list[0] = user_list[0].upper()
                        self.R2C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R2C1.setText(user_list[0])
                    else:
                        user_list[0] = user_list[0].upper()
                        self.R2C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R2C1.setText(user_list[0])
                    # Row 2 Column 2
                    if str(user_list[1]) == str(correct_list[1]):
                        user_list[1] = user_list[1].upper()
                        self.R2C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R2C2.setText(user_list[1])
                    elif str(user_list[1]) in correct_list:
                        user_list[1] = user_list[1].upper()
                        self.R2C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R2C2.setText(user_list[1])
                    else:
                        user_list[1] = user_list[1].upper()
                        self.R2C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R2C2.setText(user_list[1])
                    # Row 2 Column 3
                    if str(user_list[2]) == str(correct_list[2]):
                        user_list[2] = user_list[2].upper()
                        self.R2C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R2C3.setText(user_list[2])
                    elif str(user_list[2]) in correct_list:
                        user_list[2] = user_list[2].upper()
                        self.R2C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R2C3.setText(user_list[2])
                    else:
                        user_list[2] = user_list[2].upper()
                        self.R2C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R2C3.setText(user_list[2])
                    # Row 2 Column 4
                    if str(user_list[3]) == str(correct_list[3]):
                        user_list[3] = user_list[3].upper()
                        self.R2C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R2C4.setText(user_list[3])
                    elif str(user_list[3]) in correct_list:
                        user_list[3] = user_list[3].upper()
                        self.R2C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R2C4.setText(user_list[3])
                    else:
                        user_list[3] = user_list[3].upper()
                        self.R2C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R2C4.setText(user_list[3])
                    # Row 2 Column 5
                    if str(user_list[4]) == str(correct_list[4]):
                        user_list[4] = user_list[4].upper()
                        self.R2C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R2C5.setText(user_list[4])
                    elif str(user_list[4]) in correct_list:
                        user_list[4] = user_list[4].upper()
                        self.R2C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R2C5.setText(user_list[4])
                    else:
                        user_list[4] = user_list[4].upper()
                        self.R2C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R2C5.setText(user_list[4])

                elif self.round == 3:
                    # Row 3 Column 1
                    if str(user_list[0]) == str(correct_list[0]):
                        user_list[0] = user_list[0].upper()
                        self.R3C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R3C1.setText(user_list[0])
                    elif str(user_list[0]) in correct_list:
                        user_list[0] = user_list[0].upper()
                        self.R3C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R3C1.setText(user_list[0])
                    else:
                        user_list[0] = user_list[0].upper()
                        self.R3C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R3C1.setText(user_list[0])
                    # Row 3 Column 2
                    if str(user_list[1]) == str(correct_list[1]):
                        user_list[1] = user_list[1].upper()
                        self.R3C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R3C2.setText(user_list[1])
                    elif str(user_list[1]) in correct_list:
                        user_list[1] = user_list[1].upper()
                        self.R3C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R3C2.setText(user_list[1])
                    else:
                        user_list[1] = user_list[1].upper()
                        self.R3C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R3C2.setText(user_list[1])
                    # Row 3 Column 3
                    if str(user_list[2]) == str(correct_list[2]):
                        user_list[2] = user_list[2].upper()
                        self.R3C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R3C3.setText(user_list[2])
                    elif str(user_list[2]) in correct_list:
                        user_list[2] = user_list[2].upper()
                        self.R3C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R3C3.setText(user_list[2])
                    else:
                        user_list[2] = user_list[2].upper()
                        self.R3C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R3C3.setText(user_list[2])
                    # Row 3 Column 4
                    if str(user_list[3]) == str(correct_list[3]):
                        user_list[3] = user_list[3].upper()
                        self.R3C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R3C4.setText(user_list[3])
                    elif str(user_list[3]) in correct_list:
                        user_list[3] = user_list[3].upper()
                        self.R3C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R3C4.setText(user_list[3])
                    else:
                        user_list[3] = user_list[3].upper()
                        self.R3C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R3C4.setText(user_list[3])
                    # Row 3 Column 5
                    if str(user_list[4]) == str(correct_list[4]):
                        user_list[4] = user_list[4].upper()
                        self.R3C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R3C5.setText(user_list[4])
                    elif str(user_list[4]) in correct_list:
                        user_list[4] = user_list[4].upper()
                        self.R3C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R3C5.setText(user_list[4])
                    else:
                        user_list[4] = user_list[4].upper()
                        self.R3C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R3C5.setText(user_list[4])

                elif self.round == 4:
                    # Row 4 Column 1
                    if str(user_list[0]) == str(correct_list[0]):
                        user_list[0] = user_list[0].upper()
                        self.R4C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R4C1.setText(user_list[0])
                    elif str(user_list[0]) in correct_list:
                        user_list[0] = user_list[0].upper()
                        self.R4C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R4C1.setText(user_list[0])
                    else:
                        user_list[0] = user_list[0].upper()
                        self.R4C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R4C1.setText(user_list[0])
                    # Row 4 Column 2
                    if str(user_list[1]) == str(correct_list[1]):
                        user_list[1] = user_list[1].upper()
                        self.R4C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R4C2.setText(user_list[1])
                    elif str(user_list[1]) in correct_list:
                        user_list[1] = user_list[1].upper()
                        self.R4C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R4C2.setText(user_list[1])
                    else:
                        user_list[1] = user_list[1].upper()
                        self.R4C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R4C2.setText(user_list[1])
                    # Row 4 Column 3
                    if str(user_list[2]) == str(correct_list[2]):
                        user_list[2] = user_list[2].upper()
                        self.R4C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R4C3.setText(user_list[2])
                    elif str(user_list[2]) in correct_list:
                        user_list[2] = user_list[2].upper()
                        self.R4C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R4C3.setText(user_list[2])
                    else:
                        user_list[2] = user_list[2].upper()
                        self.R4C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R4C3.setText(user_list[2])
                    # Row 4 Column 4
                    if str(user_list[3]) == str(correct_list[3]):
                        user_list[3] = user_list[3].upper()
                        self.R4C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R4C4.setText(user_list[3])
                    elif str(user_list[3]) in correct_list:
                        user_list[3] = user_list[3].upper()
                        self.R4C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R4C4.setText(user_list[3])
                    else:
                        user_list[3] = user_list[3].upper()
                        self.R4C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R4C4.setText(user_list[3])
                    # Row 4 Column 5
                    if str(user_list[4]) == str(correct_list[4]):
                        user_list[4] = user_list[4].upper()
                        self.R4C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R4C5.setText(user_list[4])
                    elif str(user_list[4]) in correct_list:
                        user_list[4] = user_list[4].upper()
                        self.R4C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R4C5.setText(user_list[4])
                    else:
                        user_list[4] = user_list[4].upper()
                        self.R4C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R4C5.setText(user_list[4])

                elif self.round == 5:
                    # Row 5 Column 1
                    if str(user_list[0]) == str(correct_list[0]):
                        user_list[0] = user_list[0].upper()
                        self.R5C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R5C1.setText(user_list[0])
                    elif str(user_list[0]) in correct_list:
                        user_list[0] = user_list[0].upper()
                        self.R5C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R5C1.setText(user_list[0])
                    else:
                        user_list[0] = user_list[0].upper()
                        self.R5C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R5C1.setText(user_list[0])
                    # Row 5 Column 2
                    if str(user_list[1]) == str(correct_list[1]):
                        user_list[1] = user_list[1].upper()
                        self.R5C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R5C2.setText(user_list[1])
                    elif str(user_list[1]) in correct_list:
                        user_list[1] = user_list[1].upper()
                        self.R5C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R5C2.setText(user_list[1])
                    else:
                        user_list[1] = user_list[1].upper()
                        self.R5C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R5C2.setText(user_list[1])
                    # Row 5 Column 3
                    if str(user_list[2]) == str(correct_list[2]):
                        user_list[2] = user_list[2].upper()
                        self.R5C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R5C3.setText(user_list[2])
                    elif str(user_list[2]) in correct_list:
                        user_list[2] = user_list[2].upper()
                        self.R5C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R5C3.setText(user_list[2])
                    else:
                        user_list[2] = user_list[2].upper()
                        self.R5C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R5C3.setText(user_list[2])
                    # Row 5 Column 4
                    if str(user_list[3]) == str(correct_list[3]):
                        user_list[3] = user_list[3].upper()
                        self.R5C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R5C4.setText(user_list[3])
                    elif str(user_list[3]) in correct_list:
                        user_list[3] = user_list[3].upper()
                        self.R5C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R5C4.setText(user_list[3])
                    else:
                        user_list[3] = user_list[3].upper()
                        self.R5C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R5C4.setText(user_list[3])
                    # Row 5 Column 5
                    if str(user_list[4]) == str(correct_list[4]):
                        user_list[4] = user_list[4].upper()
                        self.R5C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R5C5.setText(user_list[4])
                    elif str(user_list[4]) in correct_list:
                        user_list[4] = user_list[4].upper()
                        self.R5C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R5C5.setText(user_list[4])
                    else:
                        user_list[4] = user_list[4].upper()
                        self.R5C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R5C5.setText(user_list[4])

                elif self.round == 6:
                    # Row 6 Column 1
                    if str(user_list[0]) == str(correct_list[0]):
                        user_list[0] = user_list[0].upper()
                        self.R6C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R6C1.setText(user_list[0])
                    elif str(user_list[0]) in correct_list:
                        user_list[0] = user_list[0].upper()
                        self.R6C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R6C1.setText(user_list[0])
                    else:
                        user_list[0] = user_list[0].upper()
                        self.R6C1.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R6C1.setText(user_list[0])
                    # Row 6 Column 2
                    if str(user_list[1]) == str(correct_list[1]):
                        user_list[1] = user_list[1].upper()
                        self.R6C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R6C2.setText(user_list[1])
                    elif str(user_list[1]) in correct_list:
                        user_list[1] = user_list[1].upper()
                        self.R6C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R6C2.setText(user_list[1])
                    else:
                        user_list[1] = user_list[1].upper()
                        self.R6C2.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R6C2.setText(user_list[1])
                    # Row 6 Column 3
                    if str(user_list[2]) == str(correct_list[2]):
                        user_list[2] = user_list[2].upper()
                        self.R6C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R6C3.setText(user_list[2])
                    elif str(user_list[2]) in correct_list:
                        user_list[2] = user_list[2].upper()
                        self.R6C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R6C3.setText(user_list[2])
                    else:
                        user_list[2] = user_list[2].upper()
                        self.R6C3.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R6C3.setText(user_list[2])
                    # Row 6 Column 4
                    if str(user_list[3]) == str(correct_list[3]):
                        user_list[3] = user_list[3].upper()
                        self.R6C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R6C4.setText(user_list[3])
                    elif str(user_list[3]) in correct_list:
                        user_list[3] = user_list[3].upper()
                        self.R6C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R6C4.setText(user_list[3])
                    else:
                        user_list[3] = user_list[3].upper()
                        self.R6C4.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R6C4.setText(user_list[3])
                    # Row 6 Column 5
                    if str(user_list[4]) == str(correct_list[4]):
                        user_list[4] = user_list[4].upper()
                        self.R6C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(0, 170, 0); font: 22pt "MS Shell Dlg 2"')
                        self.R6C5.setText(user_list[4])
                    elif str(user_list[4]) in correct_list:
                        user_list[4] = user_list[4].upper()
                        self.R6C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 50); font: 22pt "MS Shell Dlg 2"')
                        self.R6C5.setText(user_list[4])
                    else:
                        user_list[4] = user_list[4].upper()
                        self.R6C5.setStyleSheet('background-color: rgb(97, 97, 97); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                        self.R6C5.setText(user_list[4])

                # losing conditions
                elif self.round > 6:
                    self.Main_Label_2.setStyleSheet('background-color: rgb(0, 0, 0); color: rgb(255, 255, 255); font: 22pt "MS Shell Dlg 2"')
                    self.Main_Label_2.setText("You have run out of turns :(")
                    time.sleep(5)
                    quit()

            self.round += 1