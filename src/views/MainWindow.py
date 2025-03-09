from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon

from config import settings
from src.views.FileEditor import FileEditor


class MainWindow(QMainWindow):
  def __init__(self, controller):
    super().__init__()

    self.controller = controller

    self._set_basic_components()
    self._create_ui_elements()

  def _set_basic_components(self):
    self.setGeometry(
      settings.MAIN_WINDOW_X_POSITION,
      settings.MAIN_WINDOW_Y_POSITION,
      settings.MAIN_WINDOW_WIDTH,
      settings.MAIN_WINDOW_HEIGHT)
    self.setWindowTitle(settings.MAIN_WINDOW_TITLE)
    self.setWindowIcon(QIcon(settings.MAIN_WINDOW_ICON))

  def _create_ui_elements(self):
    # Establish the central widget and layout
    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)
    self.setCentralWidget(central_widget)

    # Create a push button for each launchable program
    file_editor_button = QPushButton("File Editor")

    # Connect the buttons to functions which launch the programs
    file_editor_button.clicked.connect(self.launch_file_editor)

    # Add the buttons to the layout
    layout.addWidget(file_editor_button)

  def launch_file_editor(self):
    self.file_editor_window = FileEditor()
    self.file_editor_window.show()
