# atm.py

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox
)


class ATM(QWidget):
    def __init__(self):
        super().__init__()
        self.balance = 0.0
        self.pin_code = "1234"  # PINCODE
        self.entered_pin = ""
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('ATM Simulator')
        self.setStyleSheet("background-color: #f0f8ff;")

        # Create widgets
        self.pin_input = QLineEdit(self)
        self.pin_input.setPlaceholderText('Enter PIN')
        self.pin_input.setEchoMode(QLineEdit.Password)
        self.pin_input.setStyleSheet("padding: 10px; border: 1px solid #008cba; border-radius: 5px;")

        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText('Enter amount')
        self.amount_input.setStyleSheet("padding: 10px; border: 1px solid #008cba; border-radius: 5px;")

        self.login_button = QPushButton('Login', self)
        self.deposit_button = QPushButton('Deposit', self)
        self.withdraw_button = QPushButton('Withdraw', self)
        self.check_balance_button = QPushButton('Check Balance', self)
        self.exit_button = QPushButton('Exit', self)

        # Style buttons
        button_style = """
        QPushButton {
            background-color: #008cba; 
            color: white; 
            padding: 10px; 
            border: none; 
            border-radius: 5px;
            font-size: 16px;
        }
        QPushButton:hover {
            background-color: #005f8b;
        }
        """
        self.login_button.setStyleSheet(button_style)
        self.deposit_button.setStyleSheet(button_style)
        self.withdraw_button.setStyleSheet(button_style)
        self.check_balance_button.setStyleSheet(button_style)
        self.exit_button.setStyleSheet(button_style)

        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.pin_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.amount_input)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.deposit_button)
        button_layout.addWidget(self.withdraw_button)
        button_layout.addWidget(self.check_balance_button)
        button_layout.addWidget(self.exit_button)

        layout.addLayout(button_layout)

        self.setLayout(layout)


        self.login_button.clicked.connect(self.check_pin)
        self.deposit_button.clicked.connect(self.deposit)
        self.withdraw_button.clicked.connect(self.withdraw)
        self.check_balance_button.clicked.connect(self.check_balance)
        self.exit_button.clicked.connect(self.exit_app)


        self.set_buttons_enabled(False)

        self.show()

    def check_pin(self):
        self.entered_pin = self.pin_input.text()
        if self.entered_pin == self.pin_code:
            QMessageBox.information(self, 'Success', 'PIN accepted. You can now access the ATM functions.')
            self.set_buttons_enabled(True)
            self.pin_input.setEnabled(False)
            self.login_button.setEnabled(False)
        else:
            QMessageBox.warning(self, 'Error', 'Incorrect PIN. Please try again.')

    def set_buttons_enabled(self, enabled):
        self.deposit_button.setEnabled(enabled)
        self.withdraw_button.setEnabled(enabled)
        self.check_balance_button.setEnabled(enabled)

    def deposit(self):
        amount = self.get_amount_from_input()
        if amount is not None:
            self.balance += amount
            QMessageBox.information(self, 'Success', f'You have deposited ${amount:.2f}.')

    def withdraw(self):
        amount = self.get_amount_from_input()
        if amount is not None:
            if amount > self.balance:
                QMessageBox.warning(self, 'Error', 'Insufficient funds.')
            else:
                self.balance -= amount
                QMessageBox.information(self, 'Success', f'You have withdrawn ${amount:.2f}.')

    def check_balance(self):
        QMessageBox.information(self, 'Current Balance', f'Your current balance is ${self.balance:.2f}.')

    def get_amount_from_input(self):
        try:
            amount = float(self.amount_input.text())
            if amount <= 0:
                QMessageBox.warning(self, 'Error', 'Amount must be greater than zero.')
                return None
            return amount
        except ValueError:
            QMessageBox.warning(self, 'Error', 'Invalid input. Please enter a number.')
            return None

    def exit_app(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    atm_simulator = ATM()
    sys.exit(app.exec_())
