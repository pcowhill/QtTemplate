from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon

from config import settings
from src.views.FileEditor import FileEditor
from src.views.Rotate3D import Rotate3D
from src.views.TicTacToe import TicTacToe
from src.views.ImageDraw import ImageDraw


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
    rotate_3d_button = QPushButton("Rotate 3D")
    tictactoe_button = QPushButton("Tic Tac Toe")
    image_draw_button = QPushButton("Image Draw")

    # Connect the buttons to functions which launch the programs
    file_editor_button.clicked.connect(self.launch_file_editor)
    rotate_3d_button.clicked.connect(self.launch_rotate_3d)
    tictactoe_button.clicked.connect(self.launch_tictactoe)
    image_draw_button.clicked.connect(self.launch_image_draw)

    # Add the buttons to the layout
    layout.addWidget(file_editor_button)
    layout.addWidget(rotate_3d_button)
    layout.addWidget(tictactoe_button)
    layout.addWidget(image_draw_button)

  def launch_file_editor(self):
    self.file_editor_window = FileEditor()
    self.file_editor_window.show()

  def launch_rotate_3d(self):
    self.rotate_3d_window = Rotate3D()
    self.rotate_3d_window.show()

  def launch_tictactoe(self):
    self.tictactoe_window = TicTacToe()
    self.tictactoe_window.show()

  def launch_image_draw(self):
    self.image_draw_window = ImageDraw()
    self.image_draw_window.show()