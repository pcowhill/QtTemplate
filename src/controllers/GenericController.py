class GenericController:
  """
  A controller that does not contain any rigid capabilities.  It can only
  interact in primitive ways with its assigned model.  This controller is
  great for prototyping; however, it is recomended to eventually create a more
  robust controller for more well-defined elements of the project.
  """
  def __init__(self, model):
    self.model = model

  def update(self, *args):
    self.model.set(*args)

  def fetch(self, *args):
    return self.model.get(*args)
