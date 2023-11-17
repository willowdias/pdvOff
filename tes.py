import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget

class FaderWidget(QWidget):
    def __init__(self, widget1, widget2, parent=None):
        super(FaderWidget, self).__init__(parent)
        
        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.addWidget(widget1)
        self.stackedWidget.addWidget(widget2)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.fade)
        
      
        layout = QVBoxLayout(self)
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

    def fade(self):
        current_index = self.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget.count()

        self.stackedWidget.setCurrentIndex(next_index)
        self.timer.stop()
        # Tempo para manter o widget visível antes de alternar para o próximo
        
    def muda(self):
        self.timer.start(1000) 

def main():
    app = QApplication(sys.argv)
    
    widget1 = QLabel("Widget 1")
    widget2 = QLabel("Widget 2")

    fader = FaderWidget(widget1, widget2)
    button = QPushButton("Fade")
    button.clicked.connect(fader.muda)
    
    main_widget = QWidget()
    layout = QVBoxLayout(main_widget)
    layout.addWidget(fader)
    layout.addWidget(button)
    main_widget.setLayout(layout)
    
    main_widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
