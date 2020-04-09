# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, gender, initial_room):
    self.name = name
    self.gender = gender
    self.current_room = initial_room

  def move_player(self, direction):
    room_check = self.current_room.get_next_room(direction)
    if room_check:
      self.current_room = room_check
    else:
      print('This path does not exist')

  def __str__(self):
    return 'Player "{self.name}" created!'.format(self=self)


# class Character:
#   def __init__(self, name, location):

# class Enemy(Character):
#   def __init__(self, ):

# class NPC(Character):
#   def __init__(self, ):