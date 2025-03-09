"""
This file is used for defining application settings and constants which are
imported throughout the project when needed.
"""

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