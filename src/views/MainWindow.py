from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon

from config import settings


class MainWindow(QMainWindow):
  def __init__(self, controller):
    super().__init__()

    self.controller = controller

    self.set_basic_components()
    self.create_ui_elements()

  def set_basic_components(self):
    self.setGeometry(
      settings.WINDOW_X_POSITION,
      settings.WINDOW_Y_POSITION,
      settings.WINDOW_WIDTH,
      settings.WINDOW_HEIGHT)
    self.setWindowTitle(settings.WINDOW_TITLE)
    self.setWindowIcon(QIcon(str(settings.WINDOW_ICON)))

  def create_ui_elements(self):
    pass