from QtTextEditor import QtWidgets, QtGui, QtCore
import getpass


class StatusBarSeparator(QtWidgets.QWidget):
    def __init__(self, width = 20):
        super(StatusBarSeparator, self).__init__()

        self.setFixedWidth(width)


class StatusBar(QtWidgets.QStatusBar):
    '''
    Custom Status bar that hold some extra information for users such as:
        Project Name
        User Name
        Amount of entered characters

    It also shows regular StatusBar messeges.
    '''

    def __init__(self, parent = None):
        super().__init__()

        self.charCount = 0
        self.user = "None"
        self.currentFile = "Untitled"

        self.setupUI()


    def setupUI(self):

        self.setStyleSheet("background-color: rgb(230,230,230); color: rgb(30,30,30);")

        #File Name
        self.info_file = QtWidgets.QLabel("Prj: {file}".format(file = self.currentFile))
        self.addPermanentWidget(self.info_file, 0)

        #separator
        separator = StatusBarSeparator(10)
        self.addPermanentWidget(separator, 0)

        #User Info
        self.getUser()
        self.info_user = QtWidgets.QLabel("Usr: {user}".format(user = self.user))
        self.addPermanentWidget(self.info_user, 0)

        #separator
        separator = StatusBarSeparator(10)
        self.addPermanentWidget(separator, 0)

        #Char Count Info
        self.info_charCount = QtWidgets.QLabel("Chr: {charCount}".format(charCount=self.charCount))
        self.info_charCount.setFixedWidth(80)
        self.addPermanentWidget(self.info_charCount, 0)

        #separator
        separator = StatusBarSeparator(10)
        self.addPermanentWidget(separator, 0)

        self.showMessage("Hello, {user}".format(user=self.user))


    def updateStatusBar(self):
        self.info_charCount.setText("Chr: {charCount}".format(charCount=self.charCount))
        self.info_user.setText("Usr: {user}".format(user=self.user))
        self.info_file.setText("Prj: {file}".format(file = self.currentFile))


    def setCharCount(self, count = 0):
        self.charCount = count
        self.updateStatusBar()

    def showMessage(self, str = None):
        if not str:
            raise ValueError("Pass string attribute to the showMessage method of a StatusBar instance")
            return

        super().showMessage(str, 2000)

    def setUser(self, name = None):
        if name:
            self.user = name
        self.updateStatusBar()

    def setFileName(self, fileName = None):
        if not fileName:
            return
        self.currentFile = fileName
        self.updateStatusBar()

    def getUser(self):
        self.user = str(getpass.getuser())
            





