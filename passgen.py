import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QCheckBox, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtGui import QIcon


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Candy Password Generator')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(400, 300)

        # Create widgets
        self.length_label = QLabel('Password length:')
        self.length_spinbox = QSpinBox()
        self.length_spinbox.setMinimum(4)
        self.length_spinbox.setMaximum(50)
        self.uppercase_checkbox = QCheckBox('Uppercase letters')
        self.lowercase_checkbox = QCheckBox('Lowercase letters')
        self.numbers_checkbox = QCheckBox('Numbers')
        self.special_checkbox = QCheckBox('Special characters')
        self.generate_button = QPushButton('Generate')
        self.save_button = QPushButton('Save')
        self.password_label = QLabel()

        # Connect signals to slots
        self.generate_button.clicked.connect(self.generate_password)
        self.save_button.clicked.connect(self.save_passwords)

        # Create layouts
        options_layout = QVBoxLayout()
        options_layout.addWidget(self.length_label)
        options_layout.addWidget(self.length_spinbox)
        options_layout.addWidget(self.uppercase_checkbox)
        options_layout.addWidget(self.lowercase_checkbox)
        options_layout.addWidget(self.numbers_checkbox)
        options_layout.addWidget(self.special_checkbox)
        options_layout.addStretch()

        buttons_layout = QHBoxLayout()
        buttons_layout.addWidget(self.generate_button)
        buttons_layout.addWidget(self.save_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(options_layout)
        main_layout.addLayout(buttons_layout)
        main_layout.addWidget(self.password_label)

        # Set the main layout
        self.setLayout(main_layout)

    def generate_password(self):
        length = self.length_spinbox.value()

        # Create a list of all characters to include in the password
        characters = []
        if self.uppercase_checkbox.isChecked():
            characters += string.ascii_uppercase
        if self.lowercase_checkbox.isChecked():
            characters += string.ascii_lowercase
        if self.numbers_checkbox.isChecked():
            characters += string.digits
        if self.special_checkbox.isChecked():
            characters += string.punctuation

        # Generate a password
        password = ''.join(random.choice(characters) for i in range(length))

        # Display the password
        self.password_label.setText(f'Password: {password}')

    def save_passwords(self):
        # Get the generated password
        password = self.password_label.text().split(': ')[1]

        # Open a file dialog to choose a file to save the passwords to
        filename, _ = QFileDialog.getSaveFileName(self, 'Save Passwords', '', 'Text Files (*.txt)')
        if filename:
            # Write the password to the file
            with open(filename, 'a') as f:
                f.write(password + '\n')


def main():
    # Create the application object
    app = QApplication(sys.argv)

    # Create the PasswordGenerator widget
    password_generator = PasswordGenerator()

    # Show the widget
    password_generator.show()

    # Run the event loop
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
