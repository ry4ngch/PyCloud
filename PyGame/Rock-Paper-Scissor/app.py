import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import randint

textFont = QFont("Times", 14)
buttonFont = QFont("Arial", 12)

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissor Game")
        self.setGeometry(300, 150, 550, 550)
        self.UI()

    def UI(self):
        ## DEFINE LOCAL STORES
        self.computerScore = 0
        self.playerScore = 0

        ### CREATE SCORES
        self.scoreComputerText = QLabel(f"Computer Score: {self.computerScore}", self)
        self.scoreComputerText.move(30, 20)
        self.scoreComputerText.setFont(textFont)

        self.scorePlayerText = QLabel(f"Player Score: {self.playerScore}", self)
        self.scorePlayerText.move(330, 20)
        self.scorePlayerText.setFont(textFont)

        ### IMAGES
        self.imageComputer = QLabel(self)
        self.computerChoice = QPixmap(os.path.join('images', 'paper.png')).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.imageComputer.setPixmap(self.computerChoice)
        self.imageComputer.move(50, 100)

        self.imagePlayer = QLabel(self)
        self.playerChoice = QPixmap(os.path.join('images', 'paper.png')).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.imagePlayer.setPixmap(self.playerChoice)
        self.imagePlayer.move(330, 100)

        self.imageGame = QLabel(self)
        self.gameVS = QPixmap(os.path.join('images', 'versus.png')).scaled(40, 40, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.imageGame.setPixmap(self.gameVS)
        self.imageGame.move(230, 130)

        ### ADD BUTTONS
        btnStart = QPushButton("Start", self)
        btnStop = QPushButton("Stop", self)

        btnStart.setFont(buttonFont)
        btnStop.setFont(buttonFont)

        btnStart.move(180, 250)
        btnStop.move(280, 250)


        ### ADD TIMER
        self.timer = QTimer(self)
        self.timer.setInterval(100)


        # CONNECT WIDGETS
        self.timer.timeout.connect(self.playGame)
        btnStart.clicked.connect(self.timer.start)
        btnStop.clicked.connect(self.stop)


        self.show()

    def stop(self):
        self.timer.stop()

        if (self.computerScore < 4) or (self.playerScore < 4):
            if self.rndComp == self.rndPlayer:
                QMessageBox.information(self, "Information", "Draw")
            elif self.rndComp == 1 and self.rndPlayer == 3: # rock vs scissor
                QMessageBox.information(self, "Information", "Computer Wins")
                self.computerScore += 1
                self.scoreComputerText.setText(f"Computer Score: {self.computerScore}")
            elif self.rndComp == 3 and self.rndPlayer == 2: # scissor vs paper
                QMessageBox.information(self, "Information", "Computer Wins")
                self.computerScore += 1
                self.scoreComputerText.setText(f"Computer Score: {self.computerScore}")
            elif self.rndComp == 2 and self.rndPlayer == 1:
                QMessageBox.information(self, "Information", "Computer Wins")
                self.computerScore += 1
                self.scoreComputerText.setText(f"Computer Score: {self.computerScore}")
            else:
                QMessageBox.information(self, "Information", "Player Wins")
                self.playerScore += 1
                self.scorePlayerText.setText(f"Player Score: {self.playerScore}")

        if self.playerScore == 5 or self.computerScore == 5:
            reply = QMessageBox.question(self, "Message", f"Game Over: {'Computer Win' if self.computerScore > self.playerScore else 'Player Win'} \n Restart Game?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.computerScore = 0
                self.playerScore = 0
                self.scoreComputerText.setText(f"Computer Score: {self.computerScore}")
                self.scorePlayerText.setText(f"Player Score: {self.playerScore}")




    def playGame(self):
        self.rndComp = randint(1, 3)

        if self.rndComp == 1:
            self.computerChoice = QPixmap(os.path.join('images', 'rock.png')).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.imageComputer.setPixmap(self.computerChoice)

        elif self.rndComp == 2:
            self.computerChoice = QPixmap(os.path.join('images', 'paper.png')).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.imageComputer.setPixmap(self.computerChoice)

        else:
            self.computerChoice = QPixmap(os.path.join('images', 'scissor.png')).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.imageComputer.setPixmap(self.computerChoice)



        self.rndPlayer = randint(1, 3)

        if self.rndPlayer == 1:
            self.playerChoice = QPixmap(os.path.join('images', 'rock.png')).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.imagePlayer.setPixmap(self.playerChoice)

        elif self.rndPlayer == 2:
            self.playerChoice = QPixmap(os.path.join('images', 'paper.png')).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.imagePlayer.setPixmap(self.playerChoice)

        else:
            self.playerChoice = QPixmap(os.path.join('images', 'scissor.png')).scaled(100, 100, Qt.KeepAspectRatio, Qt.FastTransformation)
            self.imagePlayer.setPixmap(self.playerChoice)



def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()