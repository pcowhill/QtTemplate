from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QGraphicsDropShadowEffect, QFileDialog, QMessageBox
from PySide6.QtGui import QIcon, QPainter, QPen, QPixmap, QColor
from PySide6.QtCore import Qt

from config import settings

class PaintCanvas(QWidget):
  def __init__(self):
    super().__init__()
    self.setFixedSize(
      settings.IMAGE_DRAW_CANVAS_WIDTH,
      settings.IMAGE_DRAW_CANVAS_HEIGHT)  # Set the size of the image to paint
    self.pixmap = QPixmap(self.size())
    self.pixmap.fill(Qt.white)
    self.last_point = None  # Stores the last point the mouse was for drawing lines.

  def mousePressEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
      painter = QPainter(self.pixmap)
      pen = QPen(Qt.black, 2)
      painter.setPen(pen)
      painter.drawLine(event.pos(), event.pos())
      painter.end()
      self.last_point = event.pos()
      self.update()

  def mouseMoveEvent(self, event):
    if event.buttons() == Qt.MouseButton.LeftButton and self.last_point is not None:
        painter = QPainter(self.pixmap)
        pen = QPen(Qt.black, 2)
        painter.setPen(pen)
        painter.drawLine(self.last_point, event.pos())
        painter.end()
        self.last_point = event.pos()
        self.update()

  def mouseReleaseEvent(self, event):
    if event.button() == Qt.MouseButton.LeftButton:
      self.last_point = None

  def paintEvent(self, _):
    painter = QPainter(self)
    painter.drawPixmap(0, 0, self.pixmap)

  def clear_canvas(self):
    self.pixmap.fill(Qt.white)
    self.update()


class ImageDraw(QMainWindow):
  def __init__(self):
    super().__init__()

    self._setup_canvas()

    self._set_basic_components()
    self._create_ui_elements()

  def _setup_canvas(self):
    self.paint_canvas = PaintCanvas()
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(15)
    shadow.setColor(QColor(0, 0, 0, 160))
    shadow.setOffset(5, 5)
    self.paint_canvas.setGraphicsEffect(shadow)
    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
    layout.addWidget(self.paint_canvas)
    container = QWidget()
    container.setLayout(layout)
    self.setCentralWidget(container)

  def _set_basic_components(self):
    self.setGeometry(
      settings.IMAGE_DRAW_WINDOW_X_POSITION,
      settings.IMAGE_DRAW_WINDOW_Y_POSITION,
      settings.IMAGE_DRAW_WINDOW_WIDTH,
      settings.IMAGE_DRAW_WINDOW_HEIGHT)
    self.setWindowTitle(settings.IMAGE_DRAW_WINDOW_TITLE)
    self.setWindowIcon(QIcon(settings.IMAGE_DRAW_WINDOW_ICON))

  def _create_ui_elements(self):
    menu_bar = self.menuBar()
    file_menu = menu_bar.addMenu("File")

    new_action = file_menu.addAction("New")
    new_action.triggered.connect(self.paint_canvas.clear_canvas)

    save_action = file_menu.addAction("Save")
    save_action.triggered.connect(self.save_file)

  def save_file(self):
    caption = "Save File"
    dir = ""
    filter = "Image Files (*.png);;All Files (*)"
    file_name, _ = QFileDialog.getSaveFileName(self, caption, dir, filter)
    if file_name:
      success = self.paint_canvas.pixmap.save(file_name, "PNG")
      if success:
        QMessageBox.information(self, "File Saved", f"File saved successfully: {file_name}")
      else:
        QMessageBox.information(self, "File Not Saved", f"Failed to save PNG file: {file_name}")