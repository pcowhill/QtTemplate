"""
This file is used for defining application settings and constants which are
imported throughout the project when needed.
"""

import pathlib

WINDOW_TITLE = "Qt Template"
WINDOW_X_POSITION = 200
WINDOW_Y_POSITION = 200
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
WINDOW_ICON = pathlib.Path(__file__).parent.parent / "resources" / "WindowIcon.png"
WINDOW_ICON = WINDOW_ICON.resolve()