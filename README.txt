
This is a stand-alone PtQt/PySide application which can be launched from the command line.

The technical requirements are:
* Include a menu bar offering one or more options 
* Include a widget for the user to enter text with a 140-character limit 
* Include a control to modify the text style (eg. text font or colour)
* Have a view to indicate to the user how many characters have been typed
* Offers a status bar with some relevant information 
* Remember at least one aspect of the GUI's state between sessions (eg. geometry) and restore that aspect when the application is relaunched

This module was written and tested out with Python3.6 and PyQt5

What Is Done:
- A simple menu bar with a standard File and Edit menus
- A TextArea widget where a user writes some text which has a 140-character limit
    (when it comes to the limit - a relative message is shown on the StatusBar)
- A ToolBar that lets user modify a selected text
- A StatusBar extra information such as:
    . A project name
    . A user
    . An amount of character entered by a user
- A StatusBar that shows regular messages (Menu Actions hover, and 140-limit notification) as well as some extra info
- It remembers a geometry and a state of the MainWindow and also restores some previously entered data to the TextArea

Usage:
    $cd {A folder where yhave copied WetaApp project}
    $ python3.6 WetaApp

Requirements:
    PyQt5
Install: 
    sudo pip3.6 install pyqt5
