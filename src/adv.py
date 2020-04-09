from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
gender = input("Are you a boy or a girl? \n")
name = input("Now what did you say your name was? \n")

chris = Player(name, gender, room['outside'])
print(chris)
print("Commands: 'w' north, 'd' east, 's' south, 'a' west, 'q' quit, 'h' help")
print('~~~~~~~~~ \n \n \n')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

#### REPL Loop
# Read the user input (your Python commands).
# Evaluate your code (to work out what you mean).
# Print any results (so you can see the computer’s response).
# Loop back to step 1 (to continue the conversation

while True:
  print(chris.current_room.name)
  print(chris.current_room.description)
  print("")
  print("~~~")
  user_input = input('What do you do? ')
  user_input = user_input.lower()

  """ Modifying wasd input to directional. Need a cleaner way to do this """
  if user_input == 'w':
    user_input = 'n'
  elif user_input == 'd':
    user_input = 'e'
  elif user_input == 'a':
    user_input = 'w'
  else:
    pass
  
  print("")


  # Need a way to transfer WASD commands into NESW

  if user_input == 'q':
    print('Exiting the simulation')
    exit()
  elif user_input == 'n' or 'e' or 's' or 'w':
    print(user_input)
    chris.move_player(user_input)
  else:
    print("This isn't the time to use that!!!")








 """ Previous direction code """
  # elif user_input == 'n':
  #   if chris.current_room.n_to:
  #     chris.current_room = chris.current_room.n_to
  #   else:
  #     print('This path does not exist')
  # elif user_input == 'e':
  #   if chris.current_room.e_to:
  #     chris.current_room = chris.current_room.e_to
  #   else:
  #     print('This path does not exist')
  # elif user_input == 's':
  #   if chris.current_room.s_to:
  #     chris.current_room = chris.current_room.s_to
  #   else:
  #     print('This path does not exist')
  # elif user_input == 'w':
  #   if chris.current_room.w_to:
  #     chris.current_room = chris.current_room.w_to
  #   else:
  #     print('This path does not exist')
