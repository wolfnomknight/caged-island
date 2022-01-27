class Menus:

  def __init__(self):
    self.has_sword = False
    self.armor_equiped = False
    self.has_crystal = False
    self.crystal_charges = 1
    self.has_titan_orb = False
    self.has_dragon_orb = False
    self.dragon_awake = False
    self.dragon_alive = True
    self.tower_destroyed = False
    self.tower_visits = 0
    self.village_destroyed = False
    self.village_visits = 0
    self.home_destroyed = False
    self.home_visits = 0
    self.titan_in_party = False
    self.titan_alive = True
    self.has_small_boat = False
    self.has_big_boat = False
    self.ending = False


  def menu(text_lines, text_choices):
    i = 1

    for line in text_lines:
      print(line)

    for choice in text_choices:
      if choice == "":
        pass
      else:
        print(f"{i}. " + str(choice))
        i += 1

    user_choice = int(input("\n"))
    return user_choice
  
