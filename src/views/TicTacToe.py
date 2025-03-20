from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QIcon, QPainter, QPen, QFont
from PySide6.QtCore import Qt, QRect
from config import settings

class TicTacToe(QWidget):
  def __init__(self):
    super().__init__()
    self._setup_tictactoe()
    self._set_basic_components()
  
  def _setup_tictactoe(self):
    self.current_player = 'X'
    self.board = [[None for _ in range(3)] for _ in range(3)]

  def _set_basic_components(self):
    self.setGeometry(
      settings.TICTACTOE_WINDOW_X_POSITION,
      settings.TICTACTOE_WINDOW_Y_POSITION,
      settings.TICTACTOE_WINDOW_WIDTH,
      settings.TICTACTOE_WINDOW_HEIGHT)
    self.setWindowTitle(settings.TICTACTOE_WINDOW_TITLE)
    self.setWindowIcon(QIcon(settings.TICTACTOE_WINDOW_ICON))

  def mousePressEvent(self, event):
    cell_width = self.width() / 3
    cell_height = self.height() / 3
    col_selected = int(event.x() / cell_width)
    row_selected = int(event.y() / cell_height)
    if self.board[row_selected][col_selected] is None:
      self.board[row_selected][col_selected] = self.current_player
      if self.has_won():
        QMessageBox.information(self, "Winnder!", f"{self.current_player} has won!")
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
      elif self.has_drawn():
        QMessageBox.information(self, "Draw!", "It is a draw!!")
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
      else:
        self.current_player = 'X' if self.current_player == 'O' else 'O'
    self.update()

  def has_won(self):
    if (
      self.is_3inarow(self.board[0]) or
      self.is_3inarow(self.board[1]) or
      self.is_3inarow(self.board[2]) or
      self.is_3inarow([self.board[i][0] for i in range(3)]) or
      self.is_3inarow([self.board[i][1] for i in range(3)]) or
      self.is_3inarow([self.board[i][2] for i in range(3)]) or
      self.is_3inarow([self.board[i][i] for i in range(3)]) or
      self.is_3inarow([self.board[i][-i-1] for i in range(3)])
    ):
      return True
    return False

  def has_drawn(self):
    for row in range(3):
      for col in range(3):
        if self.board[row][col] is None:
          return False
    return True

  def is_3inarow(self, list):
    if (list[0] == self.current_player and
        list[1] == self.current_player and
        list[2] == self.current_player):
      return True
    return False

  def paintEvent(self, _):
    cell_width = self.width() / 3
    cell_height = self.height() / 3

    painter = QPainter(self)
    pen = QPen(Qt.black, 2)
    painter.setPen(pen)
    painter.drawLine(cell_width, 0, cell_width, self.height())
    painter.drawLine(2 * cell_width, 0, 2 * cell_width, self.height())
    painter.drawLine(0, cell_height, self.width(), cell_height)
    painter.drawLine(0, 2 * cell_height, self.width(), 2 * cell_height)

    font = QFont("Arial", 48)
    painter.setFont(font)

    for row in range(3):
      for col in range(3):
        if self.board[row][col] is not None:
          rect = QRect(col * cell_width, row * cell_height, cell_width, cell_height)
          painter.drawText(rect, Qt.AlignCenter, self.board[row][col])