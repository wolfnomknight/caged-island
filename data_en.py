import random
from assets import texts_en
from assets import art
from menus import Menus
from replit import clear
from meow import invalid_input

# Criação do objeto principal de menu
main_menu = Menus()
menu = Menus.menu

# Variável de controle da situação do jogo, começa em 'casa'
situacao = "home"


# Definição dos nomes
def name_generator(name_1, name_2):
  return random.choice(name_1) + random.choice(name_2)

warrior_name = name_generator(texts_en.warrior_names_1, texts_en.warrior_names_2)
wizard_name = name_generator(texts_en.wizard_names_1, texts_en.wizard_names_2)
dragon_name = name_generator(texts_en.dragon_names_1, texts_en.dragon_names_2)
titan_name = name_generator(texts_en.titan_names_1, texts_en.titan_names_2)

# Lingua (definida no game())
language = str()


def home(language):
  valid_input = False

  if main_menu.dragon_awake:
    main_menu.home_visits += 1
  
  if main_menu.home_visits > 1:
    main_menu.home_destroyed = True

  while not valid_input:

    try:
      if main_menu.home_destroyed:
        i = menu(text_lines=[texts_en.destroyed_home[0]], text_choices=[texts_en.destroyed_home[1]])
      else:
        if main_menu.armor_equiped:
          i = menu(text_lines=[texts_en.home[1]], text_choices=[texts_en.home[2]])
        else:
          i = menu(text_lines=[texts_en.home[0]], text_choices=[texts_en.home[2], texts_en.home[3]])

    except:
      clear()
      invalid_input.invalid_input(language)

    else:
      clear()
      if i == 1:
        valid_input = True
        return "travel"
      elif i == 2 and not main_menu.home_destroyed and not main_menu.armor_equiped:
        print(texts_en.equip_armor[0])
        main_menu.armor_equiped = True
        valid_input = True
        return "home"
      else:
        invalid_input.invalid_input(language)


def village(language):
  valid_input = False
  
  if main_menu.dragon_awake:
    main_menu.village_visits += 1
  
  if main_menu.village_visits > 2:
    main_menu.village_destroyed = True

  while not valid_input:
    try:
      if main_menu.village_destroyed:
        if main_menu.has_big_boat or main_menu.has_small_boat:
          i = menu(text_lines=[texts_en.destroyed_village[0]], text_choices=[texts_en.destroyed_village[1], texts_en.destroyed_village[2]])
        else:
          i = menu(text_lines=[texts_en.destroyed_village[0]], text_choices=[texts_en.destroyed_village[1]])
      elif not main_menu.village_destroyed:
        print(art.village)
        if main_menu.has_big_boat or main_menu.has_small_boat:
          i = menu(text_lines=[texts_en.village[0]], text_choices=[texts_en.village[1], texts_en.village[4]])
        else:
          i = menu(text_lines=[texts_en.village[0]], text_choices=[texts_en.village[1], texts_en.village[2], texts_en.village[3]])

    except:
      clear()
      invalid_input.invalid_input(language)

    else:
      clear()
      if i == 1:
        valid_input = True
        return "travel"
      elif i == 2:
        if main_menu.has_big_boat or main_menu.has_small_boat:
          valid_input = True
          return "boat"
        else:
          main_menu.has_big_boat = True
          print(texts_en.buy_big_boat[0])
      elif i == 3:
        main_menu.has_small_boat = True
        print(texts_en.buy_small_boat[0])
      else:
        invalid_input.invalid_input(language)


def boat(language):
  valid_input = False
  text_list = []
  option_list = [texts_en.small_boat[3], texts_en.small_boat[4], "", ""]

  while not valid_input:

    if main_menu.has_small_boat and main_menu.titan_in_party:
      main_menu.titan_in_party = False
      text_list.append(texts_en.small_boat_titan[0] + titan_name + texts_en.small_boat_titan[1])
    if main_menu.has_small_boat:
      print(art.boat)
      text_list.append(texts_en.small_boat[0])
      if main_menu.has_crystal:
        text_list.append(texts_en.small_boat[1])
        option_list[2] = texts_en.small_boat[5]
        if main_menu.crystal_charges > 1:
          text_list.append(texts_en.small_boat[2])
          option_list[2] = texts_en.small_boat[6]
    elif main_menu.has_big_boat:
      print(art.ship)
      text_list.append(texts_en.big_boat[0])
      if main_menu.titan_in_party:
        text_list.append(texts_en.big_boat[1] + titan_name + texts_en.big_boat[2])
      if main_menu.has_crystal:
        text_list.append(texts_en.big_boat[3])
        option_list[2] = texts_en.small_boat[5]
        if main_menu.crystal_charges > 1:
          text_list.append(texts_en.big_boat[4])
          option_list[2] = texts_en.small_boat[6]
    
    try:
      i = menu(text_list, option_list)
  
    except:
      clear()
      invalid_input.invalid_input(language)

    else:
      clear()
      if i == 1:
        valid_input = True
        return "village"
      elif i == 2:
        valid_input = True
        return "battle_ending"
      elif i == 3:
        valid_input = True
        return "rescue_ending"
      else:
        invalid_input.invalid_input(language)


def tower(language):
  valid_input = False
  text_list = []
  option_list = [texts_en.travel_option[0], "", "", "", "", "", ""]

  if main_menu.dragon_awake:
    main_menu.tower_visits += 1

  if main_menu.tower_visits > 2:
    main_menu.tower_destroyed = True

  while not valid_input:
    if main_menu.tower_destroyed:
      text_list.append(texts_en.tower_t[0])
    elif main_menu.has_crystal or main_menu.has_titan_orb or main_menu.has_sword:
      text_list.append(texts_en.tower_t[1])
    else:
      text_list.append(texts_en.tower_t[2])
      option_list[1] = texts_en.tower_t[3]
      option_list[2] = texts_en.tower_t[4]
      option_list[3] = texts_en.tower_t[5]
    
    try:
      i = menu(text_list, option_list)
    
    except:
      clear()
      invalid_input.invalid_input(language)
    
    else:
      clear()
      if i == 1:
        valid_input = True
        return "travel"
      if i == 2:
        if main_menu.has_crystal or main_menu.has_titan_orb or main_menu.has_sword:
          invalid_input.invalid_input(language)
        else:
          valid_input = True
          main_menu.has_sword = True
          input(texts_en.tower_t[6])
          return "tower"
      if i == 3:
        if main_menu.has_crystal or main_menu.has_titan_orb or main_menu.has_sword:
          invalid_input.invalid_input(language)
        else:
          valid_input = True
          main_menu.has_titan_orb = True
          input(texts_en.tower_t[7])
          return "tower"
      if i == 4:
        if main_menu.has_crystal or main_menu.has_titan_orb or main_menu.has_sword:
          invalid_input.invalid_input(language)
        else:
          valid_input = True
          main_menu.has_crystal = True
          input(texts_en.tower_t[8])
          return "tower"
      else:
        invalid_input.invalid_input(language)
  

def forest(language):
  valid_input = False
  text_list = []
  option_list = [texts_en.travel_option[0], "", "", ""]

  print(art.tree)

  while not valid_input:
    if main_menu.titan_in_party:
      text_list.append(texts_en.forest[0])
    elif not main_menu.titan_alive:
      text_list.append(texts_en.forest[1])
    elif main_menu.has_crystal and main_menu.titan_alive:
      text_list.append(texts_en.forest[2])
      option_list[1] = texts_en.forest[6]
    elif main_menu.has_titan_orb:
      text_list.append(texts_en.forest[3] + titan_name + texts_en.forest[4])
      option_list[1] = texts_en.forest[7]
    else:
      text_list.append(texts_en.forest[5])
  
    try:
      i = menu(text_list, option_list)
    
    except:
      clear()
      invalid_input.invalid_input(language)
    
    else:
      clear()
      if i == 1:
        valid_input = True
        return "travel"
      if i == 2:
        if main_menu.titan_alive and main_menu.has_crystal:
          if main_menu.armor_equiped:
            print(texts_en.forest[8])
            valid_input = True
            main_menu.titan_alive = False
            main_menu.crystal_charges += 1
            return "forest"
          else:
            print(texts_en.forest[9])
            valid_input = True
            return "death_ending"
        elif main_menu.has_titan_orb:
          main_menu.titan_in_party = True
          print(texts_en.forest[10] + titan_name + texts_en.forest[11])
          return "travel"
      else:
        invalid_input.invalid_input(language)


def mountain(language):
  valid_input = False
  text_list = []
  option_list = [texts_en.travel_option[0], "", "", ""]

  print(art.mountains)

  while not valid_input:
    if main_menu.dragon_awake:
      text_list.append(texts_en.mountain[0] + dragon_name + texts_en.mountain[1])
    else:
      text_list.append(texts_en.mountain[2] + dragon_name + texts_en.mountain[3] + wizard_name + texts_en.mountain[4])
      option_list[1] = texts_en.mountain[7]
    
    try:
      i = menu(text_list, option_list)
    
    except:
      clear()
      invalid_input.invalid_input(language)
    
    else:
      clear()
      if i == 1:
        valid_input = True
        return "travel"
      if i == 2:
        if main_menu.dragon_awake:
          invalid_input.invalid_input(language)
        else:
          print(art.dragon)
          print(texts_en.mountain[5] + dragon_name + texts_en.mountain[6])
          main_menu.dragon_awake = True
          valid_input = True
          return "travel"
      else:
        invalid_input.invalid_input(language)


def death_ending(language):
  main_menu.ending = True

  print(texts_en.d_ending[0])
  if main_menu.dragon_awake and main_menu.dragon_alive:
    print(art.dragon)
    print(texts_en.d_ending[1] + dragon_name + texts_en.d_ending[2] + dragon_name + texts_en.d_ending[3])
  else:
    print(art.tomb)
    print(texts_en.d_ending[4]) 


def rescue_ending(language):
  main_menu.ending = True

  if main_menu.titan_alive:
    if main_menu.has_small_boat:
      print(art.ship)
      print(texts_en.r_ending[0])
    elif main_menu.has_big_boat:
      print(art.tomb)
      print(texts_en.r_ending[1])
  elif not main_menu.titan_alive:
    print(art.village)
    print(texts_en.r_ending[2])


def battle_ending(language):
  main_menu.ending = True
  if main_menu.titan_in_party:
    if main_menu.dragon_awake:
      print(texts_en.b_ending[0] + titan_name + texts_en.b_ending[1])
    if main_menu.village_destroyed:
      print(art.skull)
      print(texts_en.b_ending[2])
    elif not main_menu.village_destroyed:
      if main_menu.tower_destroyed:
        print(art.ship)
        print(texts_en.b_ending[3] + wizard_name + texts_en.b_ending[4])
      elif not main_menu.tower_destroyed:
        print(art.wizard)
        print(texts_en.b_ending[5] + wizard_name + texts_en.b_ending[6])
  elif not main_menu.titan_in_party:
    if main_menu.has_sword and main_menu.armor_equiped and main_menu.has_big_boat:
      print(art.sword)
      print(texts_en.b_ending[10])
    elif not main_menu.has_sword or not main_menu.armor_equiped or not main_menu.has_big_boat:
      death_ending(language)
    elif main_menu.has_dragon_orb:
      if main_menu.village_destroyed:
        print(art.skull)
        print(texts_en.b_ending[7])
      elif not main_menu.village_destroyed:
        if main_menu.tower_destroyed:
          print(art.warrior)
          print(texts_en.b_ending[8])
        elif not main_menu.tower_destroyed:
          print(art.dragon)
          print(texts_en.b_ending[9])


def travel(language):
  valid_input = False
  
  while not valid_input:
    try:
      i = menu(text_lines=[texts_en.travel[0]], text_choices=[texts_en.travel[1], texts_en.travel[2], texts_en.travel[3], texts_en.travel[4], texts_en.travel[5]])
    except:
      clear()
      invalid_input.invalid_input(language)
    
    else:
      if i == 1:
        clear()
        valid_input = True
        return "home"
      elif i == 2:
        clear()
        valid_input = True
        return "village"
      elif i == 3:
        clear()
        valid_input = True
        return "tower"
      elif i == 4:
        clear()
        valid_input = True
        return "forest"
      elif i == 5:
        clear()
        valid_input = True
        return "mountain"
      else:
        clear()
        invalid_input.invalid_input(language)


# Função principal do jogo (br) - chamada no main
def game(game_language):
  # Acesso à variável da situação do jogo
  global situacao
  # Acesso à variavel de linguagem - apenas para ingles porque a função que decide a lingua está no 'data' de portugues brasileiro
  global language
  language = game_language
  # Título
  print(art.title)
  print(texts_en.story[0] + warrior_name + texts_en.story[1] + dragon_name + texts_en.story[2])
  # Verificar se jogo acabou
  while not main_menu.ending:
    # O sistema do jogo consiste em repetir a instrução de mudar a situaçao enquando o jogo nao terminar. A situação é alterada pelas funções chamadas de acordo com as decisões do jogador
    situacao = eval(situacao)(language) 

