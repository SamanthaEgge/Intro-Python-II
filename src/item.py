class Items:
  def __init__(self, name, description, value):
    self.name = name
    self.description = description
    self.value = value

class Treasures(Items):
  def __init__(self, rarity):
    super().__init__(self, name, description, value)
    self.rarity = rarity

class Weapons(Items):
  def __init__(self, wpn_type, dmg):
    super().__init__(self, name, description, value)
    self.wpn_type = wpn_type
    self.dmg = dmg

class Utilities(Items):
  def __init__(self, utility):
    super().__init__(self, name, description)
    self.utility = utiltity
