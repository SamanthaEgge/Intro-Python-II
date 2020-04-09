# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
  def __init__(self, name, description, items=[]):
    self.name = name
    self.description = description
    self.n_to = None
    self.e_to = None
    self.s_to = None
    self.w_to = None

    """ Setting possible items to room. """
    if items is None:
      self.items = []
    else:
      self.items = items

  """ Grabbing direction from Player move_player to determine if room exists"""
  def get_next_room(self, direction):
    if hasattr(self, f"{direction}_to"):
      print('we made this?')
      print (self.n_to)
      return getattr(self, f"{direction}_to")
    return None


