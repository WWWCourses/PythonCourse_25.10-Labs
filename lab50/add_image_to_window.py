import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QMainWindow):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')

		pixmap = qtg.QPixmap('./images/book-6957870_640.jpg')
		img_label = qtw.QLabel()
		img_label.setPixmap(pixmap)
		img_label.resize(pixmap.width(),pixmap.height())
		self.setCentralWidget(img_label)


		self.show();



if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
