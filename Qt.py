from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout
import sys
from main import TrafficGenerator


class TrafficGeneratorWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.TrafGen = TrafficGenerator()
        self.secs = int
        self.start_button = None
        self.add_button = None
        self.url_input = None
        self.url_label = None
        self.seconds_input = None
        self.seconds_label = None
        self.url_label_to_del = None
        self.del_button = None
        self.url_del = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Traffic Generator")
        self.setGeometry(100, 100, 300, 300)

        self.seconds_label = QLabel("Seconds:")
        self.seconds_input = QLineEdit()
        self.seconds_input.setPlaceholderText("Enter seconds")

        self.url_label = QLabel("URL:")
        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("Enter URL")

        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.addWebsite)

        self.url_label_to_del = QLabel("URL:")
        self.url_del = QLineEdit()
        self.url_del.setPlaceholderText("Delete URL")

        self.del_button = QPushButton("Delete")
        self.del_button.clicked.connect(self.delWebsite)

        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.run)

        layout = QVBoxLayout()
        layout.addWidget(self.seconds_label)
        layout.addWidget(self.seconds_input)
        layout.addWidget(self.url_label)
        layout.addWidget(self.url_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.url_label_to_del)
        layout.addWidget(self.url_del)
        layout.addWidget(self.del_button)
        layout.addWidget(self.start_button)
        self.setLayout(layout)

    def addWebsite(self):
        url = self.url_input.text()
        self.TrafGen.links.add_link(url)

    def delWebsite(self):
        url = self.url_input.text()
        self.TrafGen.links.del_link(url)

    def run(self):
        self.TrafGen.driverConnect()
        self.secs = int(self.seconds_input.text()) if self.seconds_input.text() else 10
        self.TrafGen.startGen(self.secs)
        self.TrafGen.driverDisconnect()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TrafficGeneratorWindow()
    window.show()
    sys.exit(app.exec_())

# Можно добавить Show all links с опциональным выбором ссылок галочками, возможность загружать текстовик со ссылками,
# Поле для логов.
