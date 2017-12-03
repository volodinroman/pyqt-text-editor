from QtTextEditor import QtWidgets, QtGui, QtCore
from .statusBar import StatusBar


import os

PROJECT_ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')) #Projects path

class MyApp(QtWidgets.QMainWindow):
    '''
    Main TextEditor class
    '''

    def __init__(self):
        super(MyApp, self).__init__()

        self.fileBasename = "Untitled"
        self.filePath = None
        self._CHAR_MAX = 140
      
        self.settings = QtCore.QSettings("RomanVolodin", "QtTextEditor")

        self.setupUI()
        self.restoreSettings()


    def restoreSettings(self):
        '''
        Get window position and size
        Get state of window's widgets
        '''
        try:
            self.restoreGeometry(self.settings.value("geometry", ""))
        except:
            pass

        try:
            self.restoreState(self.settings.value("windowState", ""))
        except:
            pass

        html = self.settings.value("textEditor_content")
        self.text_edit.setHtml(html)

        self.filePath = self.settings.value("textEditor_FilePath")
        self.fileBasename = self.settings.value("textEditor_FileBasename")

        if not (self.fileBasename == None or self.fileBasename == "Untitled"):
            self.statusBar.setFileName(fileName = self.fileBasename)


    def closeEvent(self, event):
        '''
        ReDefined Close event
        Save settings on close
        '''
        self.settings.setValue("geometry", self.saveGeometry())
        self.settings.setValue("windowState", self.saveState())
        self.settings.setValue("textEditor_content", self.text_edit.toHtml())
        self.settings.setValue("textEditor_FilePath", self.filePath)
        self.settings.setValue("textEditor_FileBasename", self.fileBasename)
        

        QtWidgets.QMainWindow.closeEvent(self, event)


    def setupUI(self):
        '''
        Basic Setup
        '''
        #attributes
        self.setObjectName("QtTextEditor2017")
        self.setMinimumSize(400, 300)
        self.setGeometry(100, 100, 1200, 800)

        #Editor
        self.text_edit = QtWidgets.QTextEdit()
        self.text_edit.setStyleSheet("background-color: rgb(50,50,50); color: rgb(220, 220, 220)")
        self.text_edit.textChanged.connect(self.eventTextChanged)
        self.setCentralWidget(self.text_edit)
        
        #Menu
        self.menu = QtWidgets.QMenuBar()
        self.setMenuBar(self.menu)
        self.initMainMenu()
        
        #Toolbar
        self.toolbar = QtWidgets.QToolBar(self)
        self.toolbar.setMovable(True)
        self.toolbar.setStyleSheet("border-width: 0px;")
        self.toolbar.setObjectName("QtTextEditorToolbar")
        self.addToolBar(self.toolbar)
        self.initToolbar()

        #StatusBar
        self.statusBar = StatusBar(self)
        self.setStatusBar(self.statusBar)

    def initToolbar(self):
        '''
        Initialize ToolBar compoents
        '''

        #undo redo
        self.undo = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "undo.svg")),"Undo",self)
        self.undo.triggered.connect(self.appUndo)
        self.redo = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "redo.svg")),"Redo",self)
        self.redo.triggered.connect(self.appRedo)

        #bold italic underline
        self.bold = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "bold-text.svg")),"Make text bold",self)
        self.bold.triggered.connect(self.CSS_fontBold)
        self.italic = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "italics.svg")),"Make text italic",self)
        self.italic.triggered.connect(self.CSS_fontItalic)
        self.underline = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "undelined.svg")),"Make text underlined",self)
        self.underline.triggered.connect(self.CSS_fontUnderline)

        #Font Family
        self.combobox_fontfamily = QtWidgets.QFontComboBox()
        self.combobox_fontfamily.currentFontChanged.connect(self.CSS_fontFamily)

        #FontSize
        self.combobox_fontsize = QtWidgets.QSpinBox()
        self.combobox_fontsize.setSuffix(" pt")
        self.combobox_fontsize.valueChanged.connect(lambda size: self.CSS_fontSize(size))
        self.combobox_fontsize.setValue(14)

        #FontColor
        self.fontColor = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "letter-color.svg")),"Change font color",self)
        self.fontColor.triggered.connect(self.CSS_fontColor)

        #fontBackground
        self.fontBG = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "brush.svg")),"Change font background color",self)
        self.fontBG.triggered.connect(self.CSS_fontBackgroundColor)

        #Alignment
        self.alignLeft = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "041-left-alignment.svg")), "Text left alignment", self)
        self.alignLeft.triggered.connect(lambda: self.CSS_textAlign("Left"))

        self.alignRight = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "041-right-alignment.svg")), "Text right alignment", self)
        self.alignRight.triggered.connect(lambda: self.CSS_textAlign("Right"))

        self.alignCenter = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "041-center-alignment.svg")), "Text center alignment", self)
        self.alignCenter.triggered.connect(lambda: self.CSS_textAlign("Center"))

        self.alignJustify = QtWidgets.QAction(QtGui.QIcon(os.path.join(
            PROJECT_ROOT, "res", "icons", "041-justify-align.svg")), "Text justify alignment", self)
        self.alignJustify.triggered.connect(lambda: self.CSS_textAlign("Justify"))

        #Add components
        self.toolbar.addAction(self.undo)
        self.toolbar.addAction(self.redo)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.bold)
        self.toolbar.addAction(self.italic)
        self.toolbar.addAction(self.underline)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.combobox_fontfamily)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(self.combobox_fontsize)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.fontColor)
        self.toolbar.addAction(self.fontBG)
        self.toolbar.addSeparator()
        self.toolbar.addAction(self.alignLeft)
        self.toolbar.addAction(self.alignRight)
        self.toolbar.addAction(self.alignCenter)
        self.toolbar.addAction(self.alignJustify)

    def initMainMenu(self):

        #FILE menu
        self.menu_file = self.menu.addMenu("File")

        self.action_new = self.menu_file.addAction("New")
        self.action_new.setStatusTip("Create a new text document")
        self.action_new.setShortcut("Ctrl+N")
        self.action_new.triggered.connect(self.appNew)

        self.action_open = self.menu_file.addAction("Open")
        self.action_open.setStatusTip("Open an existing text document")
        self.action_open.setShortcut("Ctrl+O")
        self.action_open.triggered.connect(self.appOpen)

        self.action_save = self.menu_file.addAction("Save")
        self.action_save.setStatusTip("Save the current document")
        self.action_save.setShortcut("Ctrl+S")
        self.action_save.triggered.connect(self.appSave)

        self.action_saveAs = self.menu_file.addAction("Save As...")
        self.action_saveAs.setStatusTip("Save the current document in a custom folder")
        self.action_saveAs.setShortcut("Ctrl+Shift+S")
        self.action_saveAs.triggered.connect(self.appSaveAs)

        self.menu_file.addSeparator()

        self.submenu_export = self.menu_file.addMenu("Export")

        self.subaction_exportPlainText = self.submenu_export.addAction("Plain Text")
        self.subaction_exportPlainText.setStatusTip("Export the document as a plain txt file with no styles applied.")
        self.subaction_exportPlainText.triggered.connect(self.appExport)
        
        self.separator = self.menu_file.addSeparator()
        self.action_exit = self.menu_file.addAction("Exit")
        self.action_exit.setStatusTip("Exit the application")
        self.action_exit.triggered.connect(self.appExit)

        #EDIT menu
        self.menu_edit = self.menu.addMenu("Edit")
        
        self.action_undo = self.menu_edit.addAction("Undo")
        self.action_undo.setStatusTip("Undo action")
        self.action_undo.setShortcut("Ctrl+Z")
        self.action_undo.triggered.connect(self.appUndo)

        self.action_redo = self.menu_edit.addAction("Redo")
        self.action_redo.setStatusTip("Redo action")
        self.action_redo.setShortcut("Ctrl+Shift+Z")
        self.action_redo.triggered.connect(self.appRedo)

        self.menu_edit.addSeparator()
        
        self.action_copy = self.menu_edit.addAction("Copy")
        self.action_copy.setStatusTip("Copy action")
        self.action_copy.setShortcut("Ctrl+C")
        self.action_copy.triggered.connect(self.appCopy)

        self.action_cut = self.menu_edit.addAction("Cut")
        self.action_cut.setStatusTip("Cut action")
        self.action_cut.setShortcut("Ctrl+X")
        self.action_cut.triggered.connect(self.appCut)

        self.action_paste = self.menu_edit.addAction("Paste")
        self.action_paste.setStatusTip("Paste action")
        self.action_paste.setShortcut("Ctrl+V")
        self.action_paste.triggered.connect(self.appPaste)


    #Toolbar Styles
    def CSS_fontFamily(self, font):
        '''
        Set font family
        '''
        self.text_edit.setCurrentFont(font)
        
    def CSS_fontSize(self, fontSize):
        '''
        Set font size
        '''
        self.text_edit.setFontPointSize(fontSize)
        
    def CSS_fontColor(self):
        '''
        Set font color via standard color picker dialog
        '''
        colorDialog = QtWidgets.QColorDialog()
        color = colorDialog.getColor()
        self.text_edit.setTextColor(color)

    def CSS_fontBackgroundColor(self):
        '''
        Set font background color via standard color picker dialog
        '''
        colorDialog = QtWidgets.QColorDialog()
        backgroundColor = colorDialog.getColor()
        self.text_edit.setTextBackgroundColor(backgroundColor)

    def CSS_fontBold(self):
        '''
        Make font bald
        '''
        if self.text_edit.fontWeight() == QtGui.QFont.Bold:

            self.text_edit.setFontWeight(QtGui.QFont.Normal)
        else:
            self.text_edit.setFontWeight(QtGui.QFont.Bold)

    def CSS_fontItalic(self):
        '''
        Make font italic
        '''
        state = self.text_edit.fontItalic()
        self.text_edit.setFontItalic(not state)

    def CSS_fontUnderline(self):
        '''
        Make font underlined
        '''
        state = self.text_edit.fontUnderline()
        self.text_edit.setFontUnderline(not state)

    def CSS_textAlign(self, alignType = "Left"):
        '''
        Align text according alignType attribute
        '''
        if alignType == "Left":
            self.text_edit.setAlignment(QtCore.Qt.AlignLeft)
        elif alignType == "Right":
            self.text_edit.setAlignment(QtCore.Qt.AlignRight)
        elif alignType == "Center":
            self.text_edit.setAlignment(QtCore.Qt.AlignCenter)
        elif alignType == "Justify":
            self.text_edit.setAlignment(QtCore.Qt.AlignJustify)
        else:
            raise ValueError("Please check 'alignType' attribute. You have probably used an undefined type.")

    #MENU File
    def appSave(self):

        temp_filePath = self.filePath

        #if new document - open a FileDialog - save FilePath & FileName
        if not self.fileBasename or self.fileBasename == "Untitled":
            self.filePath = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
            if not self.filePath:
                self.filePath = temp_filePath
                return

            self.fileBasename = os.path.basename(self.filePath)


        #add extension 
        if not self.filePath.endswith(".qtxt"):
            self.filePath += ".qtxt"

        #write data
        with open(self.filePath, "wt") as file:
            file.write(self.text_edit.toHtml())

        #set statusbar filename
        self.statusBar.setFileName(fileName = self.fileBasename)
        print("The current document has been saved")

    def appSaveAs(self):

        #if new document - open a FileDialog - save FilePath & FileName
        temp_filePath = self.filePath
        temp_fileBasename = self.fileBasename

        self.filePath = QtWidgets.QFileDialog.getSaveFileName(self, 'Save File')[0]
        if not self.filePath:
            self.filePath = temp_filePath
            return

        self.fileBasename = os.path.basename(self.filePath)

        #add extension
        if not self.filePath.endswith(".qtxt"):
            self.filePath += ".qtxt"

        #write data
        with open(self.filePath, "wt") as file:
            file.write(self.text_edit.toHtml())

        #set statusbar filename
        self.statusBar.setFileName(fileName=self.fileBasename)
        print("The current document has been saved")

    def appOpen(self):
        self.filePath = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File',".","(*.qtxt)")[0]
        self.fileBasename = os.path.basename(self.filePath)
        
        if self.filePath:
            with open(self.filePath, "rt") as file:
                self.text_edit.setText(file.read())

        self.statusBar.setFileName(fileName=self.fileBasename)
        print("A document has been opened")

    def appNew(self):
        '''
        reInit text editor
        '''
        self.text_edit.clear()
        self.statusBar.setFileName(fileName = "Untitled")
        self.filePath = None
        self.fileBasename = "Untitled"

    def appExit(self):
        self.close()

    def appExport(self):

        exportPath = QtWidgets.QFileDialog.getSaveFileName(self, 'Export File')[0]
 
        #add extension
        if not exportPath.endswith(".txt"):
            exportPath += ".txt"

        #write data
        with open(exportPath, "wt") as file:
            file.write(self.text_edit.toPlainText())

        #set statusbar filename
        print("The current document has been exported")

    #MENU Edit
    def appUndo(self):
        '''
        Undo user action
        '''
        self.text_edit.undo()

    def appRedo(self):
        '''
        Redo user action
        '''
        self.text_edit.redo()

    def appCopy(self):
        '''
        Copy selected text
        '''
        self.text_edit.copy()

    def appCut(self):
        '''
        Cut selected text
        '''
        self.text_edit.cut()

    def appPaste(self):
        '''
        Paste text from clipboard
        '''
        self.text_edit.paste()



    def eventTextChanged(self):

        '''
        - Restricts the number of entered characters using self._CHAR_MAX attribute
        - Updates StatusBar information related to the amount of entered characters
        '''

        if len(self.text_edit.toPlainText()) > self._CHAR_MAX:
            cursor = self.text_edit.textCursor()
            cursor.setPosition(140, QtGui.QTextCursor.MoveAnchor)
            cursor.movePosition(QtGui.QTextCursor.End, QtGui.QTextCursor.KeepAnchor, 1)
            cursor.removeSelectedText()
            self.text_edit.setTextCursor(cursor)
            self.statusBar.showMessage("You have entered the maximum amount of characters (CHAR_MAX = {})".format(self._CHAR_MAX))

        if self.statusBar:
            self.statusBar.setCharCount(count=len(self.text_edit.toPlainText()))
            
