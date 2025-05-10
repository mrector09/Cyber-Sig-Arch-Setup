
# LexarWin - Advanced Windows Control (PyQt5 GUI)

from PyQt5 import QtWidgets, QtGui, QtCore
import sys, psutil, os

class LexarWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("LexarWin - Advanced Windows Control (PyQt5)")
        self.setGeometry(100, 100, 1200, 700)
        self.setStyleSheet("background-color: #1e1e2e; color: #ffffff;")

        # Sidebar Navigation (Left)
        self.sidebar = QtWidgets.QFrame(self)
        self.sidebar.setGeometry(0, 0, 200, 700)
        self.sidebar.setStyleSheet("background-color: #2e2e3e;")

        self.system_button = self.create_sidebar_button("System Control", 0, self.show_system_control)
        self.file_button = self.create_sidebar_button("File Management", 50, self.show_file_management)
        self.network_button = self.create_sidebar_button("Network Management", 100, self.show_network_management)
        self.security_button = self.create_sidebar_button("Security Center", 150, self.show_security_center)
        self.lexarai_button = self.create_sidebar_button("LexarAI", 200, self.show_lexarai)

        # Main Panel
        self.main_panel = QtWidgets.QStackedWidget(self)
        self.main_panel.setGeometry(200, 0, 1000, 700)
        self.main_panel.setStyleSheet("background-color: #1e1e2e;")

        # Creating Main Pages
        self.system_page = self.create_system_page()
        self.file_page = self.create_file_page()
        self.network_page = self.create_network_page()
        self.security_page = self.create_security_page()
        self.lexarai_page = self.create_lexarai_page()

        # Adding Pages to Main Panel
        self.main_panel.addWidget(self.system_page)
        self.main_panel.addWidget(self.file_page)
        self.main_panel.addWidget(self.network_page)
        self.main_panel.addWidget(self.security_page)
        self.main_panel.addWidget(self.lexarai_page)

        self.show_system_control()  # Default view

    def create_sidebar_button(self, text, y_position, function):
        button = QtWidgets.QPushButton(text, self.sidebar)
        button.setGeometry(0, y_position, 200, 40)
        button.setStyleSheet("background-color: #3e3e4e; color: #ffffff; font-size: 14px;")
        button.clicked.connect(function)
        return button

    def create_system_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)

        title = QtWidgets.QLabel("System Control")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        cpu_label = QtWidgets.QLabel("CPU Usage: " + str(psutil.cpu_percent()) + "%")
        layout.addWidget(cpu_label)

        ram_label = QtWidgets.QLabel("RAM Usage: " + str(psutil.virtual_memory().percent) + "%")
        layout.addWidget(ram_label)

        shutdown_button = QtWidgets.QPushButton("Shutdown System")
        shutdown_button.clicked.connect(lambda: os.system("shutdown /s /f /t 0"))
        layout.addWidget(shutdown_button)

        restart_button = QtWidgets.QPushButton("Restart System")
        restart_button.clicked.connect(lambda: os.system("shutdown /r /f /t 0"))
        layout.addWidget(restart_button)

        return page

    def create_file_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        layout.addWidget(QtWidgets.QLabel("File Management"))
        return page

    def create_network_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        layout.addWidget(QtWidgets.QLabel("Network Management"))
        return page

    def create_security_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        layout.addWidget(QtWidgets.QLabel("Security Center"))
        return page

    def create_lexarai_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        title = QtWidgets.QLabel("LexarAI - Command Center")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        self.ai_input = QtWidgets.QLineEdit()
        self.ai_input.setPlaceholderText("Ask LexarAI...")
        layout.addWidget(self.ai_input)

        self.ai_button = QtWidgets.QPushButton("Run Command")
        self.ai_button.clicked.connect(self.run_ai_command)
        layout.addWidget(self.ai_button)

        self.ai_output = QtWidgets.QTextEdit()
        self.ai_output.setReadOnly(True)
        layout.addWidget(self.ai_output)

        return page

    def run_ai_command(self):
        command = self.ai_input.text()
        self.ai_output.append("You: " + command)
        self.ai_output.append("LexarAI: Command executed (simulated).")

    def show_system_control(self):
        self.main_panel.setCurrentWidget(self.system_page)

    def show_file_management(self):
        self.main_panel.setCurrentWidget(self.file_page)

    def show_network_management(self):
        self.main_panel.setCurrentWidget(self.network_page)

    def show_security_center(self):
        self.main_panel.setCurrentWidget(self.security_page)

    def show_lexarai(self):
        self.main_panel.setCurrentWidget(self.lexarai_page)

# Running the Advanced LexarWin GUI
def run_lexarwin():
    app = QtWidgets.QApplication(sys.argv)
    window = LexarWin()
    sys.exit(app.exec_())

run_lexarwin()
