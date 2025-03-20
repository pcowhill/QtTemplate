from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QFileDialog
from PySide6.QtOpenGLWidgets import QOpenGLWidget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QTimer
from OpenGL.GL import *
from OpenGL.GLU import *
from stl import mesh
import numpy as np

from config import settings


class GLWidget(QOpenGLWidget):
  def __init__(self):
    super().__init__()
    self.angle = 0  # Initialize rotation angle
    self.timer = QTimer()
    self.timer.timeout.connect(self.update_animation)
    self.timer.start(16)  # ~60 frames per second
    self.model_type = settings.ROTATE3D_DISPLAYED_MODEL_DEFAULT
    self.load_rhomboid_dodecahedron()
    self.custom_model = None

  def initializeGL(self):
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Set background color to black
    glEnable(GL_DEPTH_TEST)  # Enable depth testing
  
  def resizeGL(self, width, height):
    if height == 0:
      height = 1  # Prevent division by zero

    glViewport(0, 0, width, height)  # Set the viewport to cover the new window

    glMatrixMode(GL_PROJECTION)  # Switch to the projection matrix
    glLoadIdentity()  # Reset the projection matrix

    use_orthographic_projection = False

    aspect = width / height
    if use_orthographic_projection:
      if width >= height:
        glOrtho(-1.0 * aspect, 1.0 * aspect, -1.0, 1.0, -1.0, 1.0)
      else:
        glOrtho(-1.0, 1.0, -1.0 / aspect, 1.0 / aspect, -1.0, 1.0)
    else:
      gluPerspective(45.0, aspect, 0.1, 100.0)
      gluLookAt(
        3, -1, 0,
        0, 0, 0,
        0, 1, 0
      )

    glMatrixMode(GL_MODELVIEW)  # Switch back to the modelview matrix

  def paintGL(self):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen

    # Set matrix mode to modelview
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  # Reset transformations

    glRotatef(self.angle, 0.0, 1.0, 0.0)  # Rotate around the y-axis
    glRotatef((self.angle * 2 % 360), 0.5, 0.0, 0.0)  # Rotate around the x-axis

    # Draw the object
    if self.model_type == settings.ROTATE3D_MODELS.CUBE:
      self.draw_cube()
    elif self.model_type == settings.ROTATE3D_MODELS.TRIANGLE:
      self.draw_triangle()
    elif self.model_type == settings.ROTATE3D_MODELS.RHOMBOID_DODECAHEDRON:
      self.draw_rhombic_dodecahedron()
    elif self.model_type == settings.ROTATE3D_MODELS.CUSTOM_MODEL:
      self.draw_custom_model()

    glFlush()

  def draw_cube(self):
    glBegin(GL_QUADS)

    # Front face (red)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)

    # Back face (green)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)

    # Top face (blue)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, 0.5, -0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, 0.5, -0.5)

    # Bottom face (yellow)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, -0.5, 0.5)
    glVertex3f(-0.5, -0.5, 0.5)

    # Right face (magenta)
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(0.5, -0.5, -0.5)
    glVertex3f(0.5, 0.5, -0.5)
    glVertex3f(0.5, 0.5, 0.5)
    glVertex3f(0.5, -0.5, 0.5)

    # Left face (cyan)
    glColor3f(0.0, 1.0, 1.0)
    glVertex3f(-0.5, -0.5, -0.5)
    glVertex3f(-0.5, -0.5, 0.5)
    glVertex3f(-0.5, 0.5, 0.5)
    glVertex3f(-0.5, 0.5, -0.5)

    glEnd()
  
  def draw_triangle(self):
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)  # Red
    glVertex2f(-0.5, -0.5)
    glColor3f(0.0, 1.0, 0.0)  # Green
    glVertex2f(0.5, -0.5)
    glColor3f(0.0, 0.0, 1.0)  # Blue
    glVertex2f(0.0, 0.5)
    glEnd()

  def load_rhomboid_dodecahedron(self):
    self.model = mesh.Mesh.from_file(settings.ROTATE3D_RHOMBOID_DODECAHEDRON_FILE)
    self.model.vectors = self.model.vectors / np.max(np.abs(self.model.vectors))

  def draw_rhombic_dodecahedron(self):
    if self.model:

      # Establish the colors for each of the faces of the polyhedron.
      # Each face is comprised of two of the triangles
      colors = np.array([
        [1.0, 0.0, 0.0], # Face 01: Red
        [1.0, 1.0, 0.0], # Face 04: Yellow
        [1.0, 0.0, 1.0], # Face 05: Magenta
        [0.3, 0.3, 0.3], # Face 12: Dark Gray
        [0.0, 1.0, 0.0], # Face 02: Green
        [1.0, 0.0, 0.0], # Face 01: Red
        [0.0, 0.0, 1.0], # Face 03: Blue
        [0.0, 1.0, 0.0], # Face 02: Green
        [0.0, 1.0, 1.0], # Face 06: Cyan
        [1.0, 0.5, 0.0], # Face 07: Orange
        [0.0, 0.0, 1.0], # Face 03: Blue
        [0.0, 1.0, 1.0], # Face 06: Cyan
        [1.0, 1.0, 0.0], # Face 04: Yellow
        [1.0, 0.0, 1.0], # Face 05: Magenta
        [1.0, 0.4, 0.6], # Face 11: Pink
        [0.5, 1.0, 0.0], # Face 09: Lime
        [0.0, 0.5, 0.5], # Face 10: Turquoise
        [0.5, 0.0, 0.5], # Face 08: Purple
        [1.0, 0.5, 0.0], # Face 07: Orange
        [1.0, 0.4, 0.6], # Face 11: Pink
        [0.5, 0.0, 0.5], # Face 08: Purple
        [0.5, 1.0, 0.0], # Face 09: Lime
        [0.3, 0.3, 0.3], # Face 12: Dark Gray
        [0.0, 0.5, 0.5]  # Face 10: Turquoise
      ])

      glBegin(GL_TRIANGLES)
      for id, triangle in enumerate(self.model.vectors):
        glColor3f(*colors[id])
        for vertex in triangle:
          glVertex3f(*vertex)
      glEnd()

  def draw_custom_model(self):
    if self.custom_model:
      np.random.seed(42)
      glBegin(GL_TRIANGLES)
      for triangle in self.custom_model.vectors:
        glColor3f(0.0, 0.25 + np.random.rand()/2, 0.0)
        for vertex in triangle:
          glVertex3f(*vertex)
      glEnd()

  def update_animation(self):
    self.angle += 1  # Increment the rotation angle
    if self.angle >= 360:
        self.angle = 0
    self.update()  # Trigger a repaint

  def cycle_model(self):
    if self.model_type == settings.ROTATE3D_MODELS.CUBE:
      self.model_type = settings.ROTATE3D_MODELS.TRIANGLE
    elif self.model_type == settings.ROTATE3D_MODELS.TRIANGLE:
      self.model_type = settings.ROTATE3D_MODELS.RHOMBOID_DODECAHEDRON
    elif self.model_type == settings.ROTATE3D_MODELS.RHOMBOID_DODECAHEDRON:
      if self.custom_model:
        self.model_type = settings.ROTATE3D_MODELS.CUSTOM_MODEL
      else:
        self.model_type = settings.ROTATE3D_MODELS.CUBE
    elif self.model_type == settings.ROTATE3D_MODELS.CUSTOM_MODEL:
      self.model_type = settings.ROTATE3D_MODELS.CUBE

  def open_custom_stl(self):
    caption = "Open File"
    dir = ""
    filter = "STL Files (*.stl);;All Files (*)"
    file_name, _ = QFileDialog.getOpenFileName(self, caption, dir, filter)
    if file_name:
      self.custom_model = mesh.Mesh.from_file(file_name)
      min_coords = np.min(self.custom_model.vectors.reshape(-1, 3), axis=0)
      max_coords = np.max(self.custom_model.vectors.reshape(-1, 3), axis=0)
      center = (min_coords + max_coords) / 2
      self.custom_model.vectors = self.custom_model.vectors - center
      self.custom_model.vectors = self.custom_model.vectors / np.max(np.abs(self.custom_model.vectors))
      self.model_type = settings.ROTATE3D_MODELS.CUSTOM_MODEL


class Rotate3D(QMainWindow):
  def __init__(self):
    super().__init__()

    self._setup_gl_widget()

    self._set_basic_components()
    self._create_ui_elements()
  
  def _setup_gl_widget(self):
    container = QWidget()
    self.setCentralWidget(container)

    layout = QVBoxLayout()
    layout.setContentsMargins(0, 0, 0, 0)  # Margins inside window edges
    layout.setSpacing(0)  # Spacing between widgets

    self.gl_widget = GLWidget()
    open_stl_button = QPushButton("Open an STL File")
    open_stl_button.clicked.connect(self.gl_widget.open_custom_stl)
    cycle_button = QPushButton("Click here to Go to Next Model in Cycle")
    cycle_button.clicked.connect(self.gl_widget.cycle_model)

    layout.addWidget(open_stl_button)
    layout.addWidget(self.gl_widget)
    layout.addWidget(cycle_button)

    container.setLayout(layout)

  def _set_basic_components(self):
    self.setGeometry(
      settings.ROTATE3D_WINDOW_X_POSITION,
      settings.ROTATE3D_WINDOW_Y_POSITION,
      settings.ROTATE3D_WINDOW_WIDTH,
      settings.ROTATE3D_WINDOW_HEIGHT)
    self.setWindowTitle(settings.ROTATE3D_WINDOW_TITLE)
    self.setWindowIcon(QIcon(settings.ROTATE3D_WINDOW_ICON))

  def _create_ui_elements(self):
    pass

