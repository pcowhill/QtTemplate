from PySide6.QtWidgets import QMainWindow, QTextEdit, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon

from config import settings


class FileEditor(QMainWindow):
  def __init__(self):
    super().__init__()

    self._setup_text_editor()

    self._set_basic_components()
    self._create_ui_elements()

  def _setup_text_editor(self):
    self.text_editor = QTextEdit()
    self.setCentralWidget(self.text_editor)

    with open(settings.FILE_EDITOR_STYLE_SHEET, "r") as in_file:
      style = in_file.read()
      self.setStyleSheet(style)

  def _set_basic_components(self):
    self.setGeometry(
      settings.FILE_EDITOR_WINDOW_X_POSITION,
      settings.FILE_EDITOR_WINDOW_Y_POSITION,
      settings.FILE_EDITOR_WINDOW_WIDTH,
      settings.FILE_EDITOR_WINDOW_HEIGHT)
    self.setWindowTitle(settings.FILE_EDITOR_WINDOW_TITLE)
    self.setWindowIcon(QIcon(settings.FILE_EDITOR_WINDOW_ICON))

  def _create_ui_elements(self):
    # Menu Bar
    menu_bar = self.menuBar()
    file_menu = menu_bar.addMenu("File")

    new_action = file_menu.addAction("New")
    new_action.triggered.connect(self.new_file)

    open_action = file_menu.addAction("Open")
    open_action.triggered.connect(self.open_file)

    save_action = file_menu.addAction("Save")
    save_action.triggered.connect(self.save_file)
  
  def new_file(self):
    self.text_editor.clear()
  
  def open_file(self):
    caption = "Open File"
    dir = ""
    filter = "Text Files (*.txt);;All Files (*)"
    file_name, _ = QFileDialog.getOpenFileName(self, caption, dir, filter)
    if file_name:
      with open(file_name, "r") as in_file:
        content = in_file.read()
        self.text_editor.setPlainText(content)
      QMessageBox.information(self, "File Opened", f"File opened successfully: {file_name}")

  def save_file(self):
    caption = "Save File"
    dir = ""
    filter = "Text Files (*.txt);;All Files (*)"
    file_name, _ = QFileDialog.getSaveFileName(self, caption, dir, filter)
    if file_name:
      with open(file_name, "w") as out_file:
        content = self.text_editor.toPlainText()
        out_file.write(content)
      QMessageBox.information(self, "File Saved", f"File saved successfully: {file_name}")
