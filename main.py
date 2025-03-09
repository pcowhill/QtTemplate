import sys
from PySide6.QtWidgets import QApplication

from src.controllers.GenericController import GenericController
from src.models.GenericModel import GenericModel
from src.views.MainWindow import MainWindow


def main():
  """
  This is the primary entrypoint of the project.
  To run this project, invoke this script. Ensure that the conda environment
  described within the README.md is activated prior to attempting to run this.
  Usage:
    python main.py
  """
  application = QApplication(sys.argv)

  # Initialize Data Models
  generic_model = GenericModel()

  # Initialize Controllers
  generic_controller = GenericController(generic_model)

  main_window = MainWindow(generic_controller)
  main_window.show()

  sys.exit(application.exec())


if __name__ == '__main__':
  main()
