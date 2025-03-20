"""
This file is used for defining application settings and constants which are
imported throughout the project when needed.
"""
from enum import auto
from enum import Enum
import pathlib

MAIN_WINDOW_TITLE = "Qt Template"
MAIN_WINDOW_X_POSITION = 100
MAIN_WINDOW_Y_POSITION = 100
MAIN_WINDOW_WIDTH = 200
MAIN_WINDOW_HEIGHT = 200
MAIN_WINDOW_ICON = pathlib.Path(__file__).parent.parent / "resources" / "WindowIcon.png"
MAIN_WINDOW_ICON = str(MAIN_WINDOW_ICON.resolve())

FILE_EDITOR_WINDOW_TITLE = "File Editor"
FILE_EDITOR_WINDOW_X_POSITION = 400
FILE_EDITOR_WINDOW_Y_POSITION = 100
FILE_EDITOR_WINDOW_WIDTH = 1600
FILE_EDITOR_WINDOW_HEIGHT = 900
FILE_EDITOR_WINDOW_ICON = pathlib.Path(__file__).parent.parent / "resources" / "WindowIcon.png"
FILE_EDITOR_WINDOW_ICON = str(FILE_EDITOR_WINDOW_ICON.resolve())
FILE_EDITOR_STYLE_SHEET = pathlib.Path(__file__).parent.parent / "resources" / "FileEditor.qss"
FILE_EDITOR_STYLE_SHEET = str(FILE_EDITOR_STYLE_SHEET.resolve())

IMAGE_DRAW_WINDOW_TITLE = "Image Draw"
IMAGE_DRAW_WINDOW_X_POSITION = 400
IMAGE_DRAW_WINDOW_Y_POSITION = 100
IMAGE_DRAW_WINDOW_WIDTH = 100  # This is set low to wrap around the canvas widget
IMAGE_DRAW_WINDOW_HEIGHT = 100  # This is set low to wrap around the canvas widget
IMAGE_DRAW_WINDOW_ICON = pathlib.Path(__file__).parent.parent / "resources" / "WindowIcon.png"
IMAGE_DRAW_WINDOW_ICON = str(IMAGE_DRAW_WINDOW_ICON.resolve())
IMAGE_DRAW_CANVAS_WIDTH = 800
IMAGE_DRAW_CANVAS_HEIGHT = 600

ROTATE3D_WINDOW_TITLE = "Rotate 3D"
ROTATE3D_WINDOW_X_POSITION = 400
ROTATE3D_WINDOW_Y_POSITION = 100
ROTATE3D_WINDOW_WIDTH = 400
ROTATE3D_WINDOW_HEIGHT = 400
ROTATE3D_WINDOW_ICON = pathlib.Path(__file__).parent.parent / "resources" / "WindowIcon.png"
ROTATE3D_WINDOW_ICON = str(ROTATE3D_WINDOW_ICON.resolve())
class ROTATE3D_MODELS(Enum):
  TRIANGLE = auto()
  CUBE = auto()
  RHOMBOID_DODECAHEDRON = auto()
  CUSTOM_MODEL = auto()
ROTATE3D_DISPLAYED_MODEL_DEFAULT = ROTATE3D_MODELS.RHOMBOID_DODECAHEDRON
ROTATE3D_RHOMBOID_DODECAHEDRON_FILE = pathlib.Path(__file__).parent.parent / "resources" / "Rhombic_dodecahedron.stl"
ROTATE3D_RHOMBOID_DODECAHEDRON_FILE = str(ROTATE3D_RHOMBOID_DODECAHEDRON_FILE.resolve())

TICTACTOE_WINDOW_TITLE = "Tic Tac Toe"
TICTACTOE_WINDOW_X_POSITION = 400
TICTACTOE_WINDOW_Y_POSITION = 100
TICTACTOE_WINDOW_WIDTH = 300
TICTACTOE_WINDOW_HEIGHT = 300
TICTACTOE_WINDOW_ICON = pathlib.Path(__file__).parent.parent / "resources" / "WindowIcon.png"
TICTACTOE_WINDOW_ICON = str(TICTACTOE_WINDOW_ICON.resolve())
