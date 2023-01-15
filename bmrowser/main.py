import sys
from qtpy import QtCore, QtWidgets, QtWebEngineWidgets


class Browser(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Browser")
        self.setGeometry(50, 50, 800, 600)

        # Create a QWebEngineView widget
        self.view = QtWebEngineWidgets.QWebEngineView(self)
        self.setCentralWidget(self.view)

        # Create a URL bar
        self.urlbar = QtWidgets.QLineEdit(self)
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        # Create a toolbar
        self.navigation_bar = QtWidgets.QToolBar("Navigation")
        self.addToolBar(self.navigation_bar)

        # Add buttons to the toolbar
        self.back_button = QtWidgets.QAction("Back", self)
        self.back_button.triggered.connect(self.view.back)
        self.navigation_bar.addAction(self.back_button)

        self.forward_button = QtWidgets.QAction("Forward", self)
        self.forward_button.triggered.connect(self.view.forward)
        self.navigation_bar.addAction(self.forward_button)

        self.refresh_button = QtWidgets.QAction("Refresh", self)
        self.refresh_button.triggered.connect(self.view.reload)
        self.navigation_bar.addAction(self.refresh_button)

        # Add the URL bar to the toolbar
        self.navigation_bar.addWidget(self.urlbar)

        # Connect the QWebEngineView's signal for loading a page to a slot
        self.view.loadFinished.connect(self.update_urlbar)

    def navigate_to_url(self):
        q = QtCore.QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.view.load(q)

    def update_urlbar(self, success):
        if success:
            self.urlbar.setText(self.view.url().toString())


app = QtWidgets.QApplication(sys.argv)
browser = Browser()
browser.show()
sys.exit(app.exec_())