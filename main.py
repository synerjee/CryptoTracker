from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
        QHBoxLayout, QLabel, QPushButton, QStyleFactory, QVBoxLayout)
import sys

import urllib.request
import json
from cryptoList import CryptoList

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class CryptoTracker(QDialog):
    def __init__(self, parent=None):
        super(CryptoTracker, self).__init__(parent)

        list = CryptoList().getComboBoxList()

        att = QLabel()
        att.setText("<a href=\"https://www.coingecko.com/en\">Powered by CoinGecko.</a>")
        att.setTextInteractionFlags(Qt.TextBrowserInteraction)
        att.setOpenExternalLinks(True)

        cryptoComboBox = QComboBox()
        cryptoComboBox.addItems(list)
        listLabel = QLabel("&Cryptocurrency:")
        listLabel.setBuddy(cryptoComboBox)

        fig = Figure()
        self.chart = FigureCanvas(fig)
        self.chart.axes = fig.add_subplot(111)

        cryptoComboBox.activated[str].connect(self.displayChart)

        chartLabel = QLabel("The chart below indicates the fluctuation of the monetary value of the selected cryptocurrency, measured in US Dollar, for the past 30 days.")
        yLabel = QLabel("Numbers in Y-Axis (vertical axis) indicatethe price of the cryptocurrency in US Dollars.")

        layout = QVBoxLayout()
        layout.addWidget(att)
        layout.addWidget(listLabel)
        layout.addWidget(cryptoComboBox)
        layout.addStretch(1)
        layout.addWidget(chartLabel)
        layout.addWidget(yLabel)
        layout.addWidget(self.chart)
        self.setLayout(layout)

        self.setWindowTitle("Cryptocurrency Chart")
        self.resize(1000, 500)
        self.changeStyle('Fusion')

    def changeStyle(self, style):
        QApplication.setStyle(QStyleFactory.create(style))

    def displayChart(self, value):
        id = CryptoList().getCryptoDict()[value]

        if (id != None):
            self.chart.axes.cla()

            x = []
            history = []
            url = "https://api.coingecko.com/api/v3/coins/"+id+"/market_chart?vs_currency=usd&days=30"
            data = json.loads(urllib.request.urlopen(url).read())

            for i in range(len(data["prices"])):
                history.append(data["prices"][i][1])
                x.append(i)

            self.chart.axes.plot(x, history)
            self.chart.draw()

if __name__ == '__main__':
    appctxt = ApplicationContext()
    cryptoTracker = CryptoTracker()
    cryptoTracker.show()
    sys.exit(appctxt.app.exec_())
