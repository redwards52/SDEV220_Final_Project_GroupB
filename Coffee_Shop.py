import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QLabel, QWidget, QMessageBox, QStackedWidget
from PyQt5.QtCore import Qt

class CoffeeShopApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Coffee Shop")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Create a QLabel for the welcome message
        welcome_label = QLabel("Welcome to the Coffee Shop")
        welcome_label.setAlignment(Qt.AlignCenter)  # Center the label
        welcome_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        
        # Add label to layout
        layout.addWidget(welcome_label)

        # Buttons
        shop_button = QPushButton("Shop")
        shop_button.setStyleSheet("background-color: rgb(139, 69, 19); color: white; border: 1px solid black;")
        shop_button.clicked.connect(self.show_shop)
        layout.addWidget(shop_button)

        inventory_button = QPushButton("Inventory")
        inventory_button.setStyleSheet("background-color: rgb(139, 69, 19); color: white; border: 1px solid black;")
        inventory_button.clicked.connect(self.show_inventory)
        layout.addWidget(inventory_button)

        order_button = QPushButton("Order")
        order_button.setStyleSheet("background-color: rgb(139, 69, 19); color: white; border: 1px solid black;")
        order_button.clicked.connect(self.show_order)
        layout.addWidget(order_button)

        payment_button = QPushButton("Payment")
        payment_button.setStyleSheet("background-color: rgb(139, 69, 19); color: white; border: 1px solid black;")
        payment_button.clicked.connect(self.show_payment)
        layout.addWidget(payment_button)

        # Set layout in a central widget
        container = QWidget()
        container.setLayout(layout)

        # Set background color to tan for the main window
        container.setStyleSheet("background-color: #D2B48C;")  # Set tan color

        # Stacked widget for different pages
        self.stacked_widget = QStackedWidget()
        self.stacked_widget.addWidget(container)

        # Set stacked widget as the central widget
        self.setCentralWidget(self.stacked_widget)

    def show_shop(self):
        self.stacked_widget.setCurrentIndex(1)  # Show the shop window
        self.shop_window = ShopWindow(self.stacked_widget)
        self.stacked_widget.addWidget(self.shop_window)

    def show_inventory(self):
        QMessageBox.information(self, "Inventory", "This will show inventory details.")

    def show_order(self):
        QMessageBox.information(self, "Order", "This will show order details.")

    def show_payment(self):
        QMessageBox.information(self, "Payment", "This will show payment options.")


class ShopWindow(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.setWindowTitle("Shop")
        self.setGeometry(150, 150, 300, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Title Label - Centered
        title_label = QLabel("Shop Menu")
        title_label.setAlignment(Qt.AlignCenter)  # Center the label
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; text-align: center;")
        layout.addWidget(title_label)

        # Drink Buttons
        drink_buttons = {
            "Water $1.00": self.show_water_options,
            "Coffee $3.50": self.show_coffee_options,
            "Soda $2.00": self.show_soda_options,
        }

        for drink, handler in drink_buttons.items():
            button = QPushButton(drink)
            button.setStyleSheet("background-color: rgb(139, 69, 19); color: white; border: 1px solid black;")
            button.clicked.connect(handler)
            layout.addWidget(button)

        # Back Button
        back_button = QPushButton("Back")
        back_button.setStyleSheet("background-color: rgb(139, 69, 19); color: white; border: 1px solid black;")
        back_button.clicked.connect(self.back_to_main)
        layout.addWidget(back_button)

        # Set layout
        self.setLayout(layout)

        # Set background color to tan for the shop menu
        self.setStyleSheet("background-color: #D2B48C;")  # Set tan color for full window

    def back_to_main(self):
        # Go back to the main page
        self.stacked_widget.setCurrentIndex(0)

    def show_water_options(self):
        QMessageBox.information(self, "Water Options", "1. Iced Water\n2. Warm Water")

    def show_coffee_options(self):
        QMessageBox.information(self, "Coffee Options", "1. Iced Coffee\n2. Hot Coffee")

    def show_soda_options(self):
        QMessageBox.information(self, "Soda Options", "1. List of all available sodas")


class OrderWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Order Details")
        self.setGeometry(150, 150, 300, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Order Details")
        title_label.setStyleSheet("font-size: 16px; font-weight: bold; text-align: center;")
        layout.addWidget(title_label)

        # Placeholder for order details
        order_details = QLabel("No orders placed yet.")
        layout.addWidget(order_details)

        # Set layout
        self.setLayout(layout)


# Run the Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = CoffeeShopApp()
    main_window.show()
    sys.exit(app.exec_())
