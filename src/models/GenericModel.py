class GenericModel:
  """
  A model that does not contain any predefined structure.  It can interact in
  primitive ways with any controllers assigned to it.  This model is great for
  prototyping; hwoever, it is recomended to eventually create a more descriptive
  and explicit model once its use within the project is more well-defined.
  """
  def __init__(self):
    self.data = {}
  
  def set(self, key, value):
    self.data[key].value

  def get(self, key):
    return self.data[key]