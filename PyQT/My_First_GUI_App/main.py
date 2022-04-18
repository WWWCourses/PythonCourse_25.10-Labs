# 1. import needed QtWidgets classes
import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 2. the main app instance for our application.
app = QApplication(sys.argv)
# app.windowIcon()
print('1')

# 3. Create Qt widget, which will be our main window.
window = QWidget()
print('2')

# 4. show the window
window.show()
print('3')

# 5. Start the event loop
# exit_code = app.exec()
# print(exit_code)

sys.exit(app.exec())
