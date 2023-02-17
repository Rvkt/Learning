import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title 
        self.setWindowTitle('PyQt 01')

        # Set vertical Layout
        self.setLayout(qtw.QVBoxLayout())
        
        # Set horizontal Layout
        # self.setLayout(qtw.QHBoxLayout())

        # Create a label
        my_label = qtw.QLabel('Your name?')
            # set the font
        my_label.setFont(qtg.QFont('Roboto Condensed', 20))
        self.layout().addWidget(my_label)

        # create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName('name_field')
        my_entry.setText('')
        self.layout().addWidget(my_entry)

        # create a button
        my_button = qtw.QPushButton('Press Me!', clicked=lambda: press_it())
        self.layout().addWidget(my_button)



        # show thw app
        self.show()

        def press_it():
            my_label.setText(f'Hello {my_entry.text()}!')
            my_entry.setText('')


app = qtw.QApplication([])
mw = MainWindow()

# Run the App
app.exec_()