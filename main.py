from replit import clear
from data import jogo, lang_choice
from data_en import game
from assets import texts
from assets import texts_en
from assets import art
from meow import credits

# Chama a seleção de linguagem
language = lang_choice()

# Variavel para ajudar a verificar se a opçao selecionada é valida
continuar = True


# Para seleção de linguagem portugues brasileiro
if language == "br":
  while continuar:
    # Menu inicial
    print(texts.intro[0])
    print(art.village)
    print("1. Novo jogo")
    print("2. Créditos")
    main_menu_choice = str(input("3. Sair\n")).lower()

    if main_menu_choice == "3" or main_menu_choice == "s" or main_menu_choice == "sair":
      clear()
      continuar = False

    elif main_menu_choice == "2" or main_menu_choice == "c" or main_menu_choice == "creditos":
      clear()
      credits.creditos()
      input("\n\n\nPressione enter para continuar...")
      clear()
    
    elif main_menu_choice == "1" or main_menu_choice == "n" or main_menu_choice == "novo jogo":
      clear()
      jogo()
      continuar = False
    
    else:
      clear()
      print(texts.invalid_input[0])


# Para seleção de linguagem em ingles
if language == "en":
  while continuar:
    print(texts_en.intro[0])
    print(art.village)
    print("1. New game")
    print("2. Credits")
    main_menu_choice = str(input("3. Quit\n")).lower()

    if main_menu_choice == "3" or main_menu_choice == "q" or main_menu_choice == "quit":
      clear()
      continuar = False

    elif main_menu_choice == "2" or main_menu_choice == "c" or main_menu_choice == "credits":
      clear()
      credits.credits()
      input("\n\n\nPress enter to continue...")
      clear()

    elif main_menu_choice == "1" or main_menu_choice == "n" or main_menu_choice == "new game":
      clear()
      game("en")
      continuar = False
    
    else:
      clear()
      print(texts_en.invalid_input[0])
