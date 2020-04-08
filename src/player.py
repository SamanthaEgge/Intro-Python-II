# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
  def __init__(self, name, gender, initial_room):
    self.name = name
    self.gender = gender
    self.current_room = initial_room
  
  def __str__(self):
    return 'Player "{self.name}" created!'.format(self=self)
  
  # def move_rooms(self):


# class Character:
#   def __init__(self, name, location):

# class Enemy(Character):
#   def __init__(self, ):

# class NPC(Character):
#   def __init__(self, ):