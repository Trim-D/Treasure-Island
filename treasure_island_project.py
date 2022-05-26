def start_game():
  treasure_ascii = ('''
  *******************************************************************************
            |                   |                  |                     |
   _________|________________.=""_;=.______________|_____________________|_______
  |                   |  ,-"_,=""     `"=.|                  |
  |___________________|__"=._o`"-._        `"=.______________|___________________
            |                `"=._o`"=._      _`"=._                     |
   _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
  |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
  |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
            |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
   _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
  |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
  |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
  ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
  /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
  ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
  /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
  ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
  /______/______/______/______/______/______/______/______/______/______/_____ /
  *******************************************************************************
  ''')
  print(treasure_ascii)
  print("Welcome to Treasure Island.")
  print("Your mission is to find the treasure.\n")

  #https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

  rip = ('''
                                   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
                                ¶¶¶¶¶¶             ¶¶¶¶¶¶¶
                            ¶¶¶¶                       ¶¶¶¶
                           ¶¶¶                             ¶¶
                          ¶¶                                ¶¶
                         ¶¶                                 ¶¶
                        ¶¶                                   ¶¶
                        ¶¶ ¶¶                             ¶¶ ¶¶
                        ¶¶ ¶¶                             ¶¶  ¶
                        ¶¶ ¶¶                             ¶¶  ¶
                       ¶¶  ¶¶                             ¶¶ ¶¶
                       ¶¶  ¶¶                            ¶¶  ¶¶
                        ¶¶ ¶¶  ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶   ¶¶ ¶¶
                         ¶¶¶¶ ¶¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶  ¶¶¶¶¶
                          ¶¶¶ ¶¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶  ¶¶¶
                  ¶¶¶      ¶¶  ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶   ¶¶      ¶¶¶¶
                 ¶¶¶¶¶     ¶¶   ¶¶¶¶¶¶¶   ¶¶¶   ¶¶¶¶¶¶¶   ¶¶     ¶¶¶¶¶¶
                ¶¶   ¶¶    ¶¶     ¶¶¶    ¶¶¶¶¶    ¶¶¶     ¶¶    ¶¶   ¶¶
               ¶¶¶    ¶¶¶¶  ¶¶          ¶¶¶¶¶¶¶          ¶¶  ¶¶¶¶    ¶¶¶
              ¶¶         ¶¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶       ¶¶¶¶¶¶¶¶¶        ¶¶
              ¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶    ¶¶¶¶¶¶¶¶      ¶¶¶¶¶¶¶¶
                ¶¶¶¶ ¶¶¶¶¶       ¶¶¶¶¶              ¶¶¶ ¶¶    ¶¶¶¶¶¶ ¶¶¶
                        ¶¶¶¶¶¶  ¶¶¶  ¶¶           ¶¶  ¶¶¶  ¶¶¶¶¶¶
                            ¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶¶¶¶¶¶ ¶¶ ¶¶¶¶¶¶
                                ¶¶ ¶¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶¶
                           ¶¶¶¶  ¶ ¶ ¶ ¶ ¶ ¶ ¶ ¶   ¶¶¶¶¶
                          ¶¶¶¶¶ ¶¶   ¶¶¶¶¶¶¶¶¶¶¶¶¶   ¶¶ ¶¶¶¶¶
                  ¶¶¶¶¶¶¶¶¶¶     ¶¶                 ¶¶      ¶¶¶¶¶¶¶¶¶
                 ¶¶           ¶¶¶¶¶¶¶             ¶¶¶¶¶¶¶¶          ¶¶
                  ¶¶¶     ¶¶¶¶¶     ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶     ¶¶¶
                    ¶¶   ¶¶¶           ¶¶¶¶¶¶¶¶¶           ¶¶¶   ¶¶
                    ¶¶  ¶¶                                   ¶¶  ¶¶
                    ¶¶¶¶                                     ¶¶¶¶''')
  # RIP art - https://textkool.com/en/text-art/scary

  #Game Start
  input("Press 'enter' to begin! ")
  import os
  clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
  clearConsole()

  print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠈⠉⠛⢷⣦⡀⠀⣀⣠⣤⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣀⣻⣿⣿⣿⣋⣀⡀⠀⠀⢀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⣠⠾⠛⠛⢻⣿⣿⣿⠟⠛⠛⠓⠢⠀⠀⠉⢿⣿⣆⣀⣠⣤⣀⣀⠀⠀⠀
                ⠀⠀⠘⠁⠀⠀⣰⡿⠛⠿⠿⣧⡀⠀⠀⢀⣤⣤⣤⣼⣿⣿⣿⡿⠟⠋⠉⠉⠀⠀
                ⠀⠀⠀⠀⠀⠠⠋⠀⠀⠀⠀⠘⣷⡀⠀⠀⠀⠀⠹⣿⣿⣿⠟⠻⢶⣄⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⢠⡿⠁⠀⠀⠀⠀⠈⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡄⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⣤⣤⣤⣤⣤⣤⡤⠄⠀⠀⣀⡀⢸⡇⢠⣤⣁⣀⠀⠀⠠⢤⣤⣤⣤⣤⣤⣤⠀
                ⠀⠀⠀⠀⠀⠀⣀⣤⣶⣾⣿⣿⣷⣤⣤⣾⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⠀⠀⠀
                ⠀⠀⠼⠿⣿⣿⠿⠛⠉⠉⠉⠙⠛⠿⣿⣿⠿⠛⠛⠛⠛⠿⢿⣿⣿⠿⠿⠇⠀⠀
                ⠀⢶⣤⣀⣀⣠⣴⠶⠛⠋⠙⠻⣦⣄⣀⣀⣠⣤⣴⠶⠶⣦⣄⣀⣀⣠⣤⣤⡶⠀
                ⠀⠀⠈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⠀⠀⠀''')
# Island art - https://emojicombos.com/island

  print("\nThe voyage across the ocean was long and treacherous, but it was worth it. Treasure Island is now in sight!\n")
  # Disembark scenario
  while True:
    try:
      disembark = int(input("Would you like to take a dinghy to shore, pull into the small dock, or take a swim in the beautiful ocean before the hunt begins?\n\nDinghy = 1\nDock = 2\nSwim = 3\n\nMake your selection: "))
    except ValueError:
      continue
    if 1 <= disembark <= 3:
      break
    else:
      print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****\n")

  # Disembark choices
  dinghy = ("\nDinghy it is! A good thing too because these are shark infested waters!  Now, let's hope that pirates don't 'borrow' your ship while you search for treasure.")
  dock = ("\nDock it is! Sadly, you damaged your hull when it struck something in the shallow shark infested waters. Let's hope the damage is not too severe.")
  swim_ocean = ("\nSwimming it is! It does appear to be a beautiful day to take a dip and the waters here are perfect; unfortunately, these waters are shark infested and you dove into a feeding frenzy.\n\nI am afraid you aren't going to survive this one.\n\n\nThank you so much for playing. I encourage you to play it again while making new decisions to see what fate has in store!")

  while True:
    if disembark == 1:
      print(dinghy)
    elif disembark == 2:
      print(dock)
    else:
      clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
      clearConsole()
      print(rip)
      print(swim_ocean)
      break

  #Keypress to continue
    input("\nPress 'enter'..")

    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()

    print('''
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⠿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿
                ⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿
                ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
                ⣿⠀⠀⣀⣀⣀⣀⣠⣤⣤⣤⣿⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿
                ⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⠉⠉⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠉⠉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⠿⠿⠿⠛⠛⠛⠂⠀⠀⠀⠀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⠛⠉⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣦⣤⣀⡀⠐⠒⠢⢤⣄⡀⠀⠀⠈⠉⠉⠙⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡉⠁⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠁⠀⠀⡀⠀⠀⡠⠞⠃⠀⣠⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⡏⠀⠀⣆⠀⠀⠻⣄⠀⠀⠀⣄⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣧⣤⣤⣬⣷⣤⣤⣤⣵⣤⣤⣬⣿⣦⣤⣤⣤⣤⣬⣭⣿⣿⣿⣿''')

# River art -- https://emojicombos.com/river

    print("\nSince making it ashore you have traveled through the jungle without delay - until now!  You have come to a large river which you need to cross!  It does not appear to be moving that fast and looks to be about waist deep.\n\nThere is a rope bridge you could use, though it looks well worn. A wooden raft sits just off the bank, though you would need a way to guide it. Swimming is an option, I mean it is a hot day and you passed up the chance before.  ")

  #River Crossing Scenario
    while True:
      try:
        river_crossing = int(input("\nHow would you like to cross the river?\n\nRope Bridge = 1\nRaft = 2\nSwim = 3\n\nMake your selection: "))
      except ValueError:
        continue
      if 1 <= river_crossing <= 3:
        break
      else:
        print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")

  #River crossing choices
    bridge = ("\nBridge it is! The bridge was definitely the safest option -- so it seemed! Half-way across, the rope holding one side of the bridge breaks and you splash into the river. Unfortunately, the river was not that deep and you are knocked unconscious as your head strikes a rock.\n\nSadly, I don't think you'll wake up any time soon.\n\n\nThank you so much for playing. I encourage you to play it again while making new decisions to see what fate has in store!")
    raft = ("\nRaft it is! The river was pretty calm and with the help of the large branch you found, you managed to guide yourself safely to the other side.")
    swim_river = ("\nSwimming it is! Sure, you got a little wet, but in this heat it was worth it!")

    if river_crossing == 2:
      print(raft)
    elif river_crossing == 3:
      print(swim_river)
    else:
      clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
      clearConsole()
      print(rip)
      print(bridge)
      break

  #Keypress to continue
    input("\nPress 'enter'..")

    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()

    print('''
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⣼⣿⣧⠈⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⠁⣸⣿⣿⣿⣷⡀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⠃⣰⣿⣿⣿⣿⣿⣷⡀⠻⣿⣿⣿⡿⢋⡙⢻⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⠃⣰⣿⣿⣿⣿⣿⣿⣿⣿⡄⠹⣿⡿⢀⣾⣷⡀⢹⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⠇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠘⠁⣼⣿⣿⣷⡀⢻⣿⣿⣿⣿
                ⣿⣿⣿⣿⠏⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⣸⣿⣿⣿⣿⣧⠀⣿⣿⣿⣿
                ⣿⣿⣿⡟⢀⣿⣿⣿⣿⣿⠿⠟⠻⢿⣿⣿⣿⣏⣰⣿⣿⣿⣿⣿⣿⣇⠸⣿⣿⣿
                ⣿⣿⡿⢁⣾⣿⣿⣿⠟⠁⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⢹⣿⣿
                ⣿⡿⠁⣼⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⢿⣿
                ⣿⣷⣾⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')

# Cave art -- https://emojicombos.com/mountain-cave

  # Treasure Chest Scenario
    print("\nFirst the ocean, then a river, and now.. You guessed it! Right out of your run-of-the-mill adventure book, we have a Cave! Once inside you see the treasure chest. It is just sitting in the open for anyone to walk up and take. Could it really be that easy?\n")

    print("The way I see it, you have a few choices. You can put on a brave face, walk up there and grab it. If that does not seem overly appealing, then the rope bridge is not too far away. You could cut some of the rope from that bridge and make a lasso to toss around the chest and pull to you. Or, you could use a large branch that fits into one of the handles and try to drag the chest toward you.")

  #Treasure chest choices
    while True:
      try:
        treasure = int(input("\nHow would you like to retrieve the treasure chest?\n\nGrab it = 1\nLasso = 2\nLarge branch = 3\n\nMake your selection: "))
      except ValueError:
        continue
      if 1 <= treasure <= 3:
        break
      else:
        print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")

    grab = ("\nYou are a brave one! Fortunately, it really was that easy.  I mean, you still have to get this incredibly heavy chest back to your ship, but that should be easy for an adventurer such as yourself.")
    lasso = ("\nThat was a safe choice, sadly the rope was pretty worn out and broke without much effort. Hmm, I wonder if that would have happened had you tried to cross the bridge earlier?")
    branch = ("\nGood thinking, you can never be too saf.. OMG, how did that happen? The weight of the chest snapped the branch and it.. Well, you can use your imagination on how that branch ended up there. It is safe to say that you won't be surviving that one.\n\nThank you so much for playing. I encourage you to play it again while making new decisions to see what fate has in store!")

    if treasure == 1:
      print(grab)
    elif treasure == 2:
      print(lasso)
      input("\nPress 'enter'..")
      while True:
        try:
          treasure_alt = int(input("\nThe rope didn't work out, but you still need to get the treasure. How would you like to proceed?\n\nGrab it = 1\nLarge branch = 2\n\nMake your selection: "))
        except ValueError:
          continue
        if 1 <= treasure_alt <= 2:
          break
        else:
          print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
      if treasure_alt == 1:
        print(grab)
      elif treasure_alt == 2:
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print(rip)
        print(branch)
        break
    else:
      clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
      clearConsole()
      print(rip)
      print(branch)
      break

    input("\nPress 'enter'..")

    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()

    print('''
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⠿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿
                ⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿
                ⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
                ⣿⠀⠀⣀⣀⣀⣀⣠⣤⣤⣤⣿⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣿
                ⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⠉⠉⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⡀⠀⠀⠉⠉⠙⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⠿⠿⠿⠛⠛⠛⠂⠀⠀⠀⠀⢀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⠛⠉⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣦⣤⣀⡀⠐⠒⠢⢤⣄⡀⠀⠀⠈⠉⠉⠙⠛⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣀⡉⠁⠀⠀⠀⠀⠀⠀⠀⢀⠀⠈⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠁⠀⠀⡀⠀⠀⡠⠞⠃⠀⣠⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⡏⠀⠀⣆⠀⠀⠻⣄⠀⠀⠀⣄⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿
                ⣿⣿⣿⣿⣿⣿⣧⣤⣤⣬⣷⣤⣤⣤⣵⣤⣤⣬⣿⣦⣤⣤⣤⣤⣬⣭⣿⣿⣿⣿''')

# River art -- https://emojicombos.com/river

  # River Crossing #2 Scenario
    print("\nYou have made it back to the river, which appears to be deeper and moving a more swiftly than before, with your treasure chest full of gold and gems. I wonder if the weight of the treasure chest will alter your method of crossing this time.\n")

  # River Crossing #2 choices
    bridge_return = ("\nBridge it is! The bridge was definitely the safest option -- so it seemed!\n\nHalf-way across the bridge, the rope holding one side of the bridge breaks and you splash into the river. Unfortunately, your leg became entangled with the bridge and with the increased depth and speed of the river, you are pulled under the water.\n\nSadly, you were not able to recover and have drowned.\n\nThank you so much for playing. I encourage you to play it again while making new decisions to see what fate has in store!")
    raft_return = ("\nRaft it is! The river was moving more quickly, but with your trusty branch you, again, managed to guide yourself safely to the other side.")
    search = ("\nSearch it is! Well look at that -- a small canoe.")
    canoe = ("\nCanoe it is! You probably should have thought of looking around earlier, but no sense dwelling on the past. You easily managed to traverse the river in the canoe.")
    swim = ("\nSwim it is! Whoa, a log came out of nowhere and slammed right into you. Darn good thing you are such a strong swimmer or you would have never made it back to shore. I told you the river was moving more swiftly.")

  # Grabbed treasure and used raft during 1st river crossing
    if treasure == 1 and river_crossing == 2:
      print("There is still the rope bridge, as well as the raft.  Good thing you used the raft before, otherwise it would be on the other side of the river. You could search further down the bank and see if there is another way of crossing.")
      while True:
        try:
          river_crossing2 = int(input("\nHow would you like to cross the river?\n\nRope Bridge = 1\nRaft = 2\nSearch = 3\n\nMake your selection: "))
        except ValueError:
          continue
        if 1 <= river_crossing2 <= 3:
          break
        else:
          print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
      if river_crossing2 == 1:
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print(rip)
        print(bridge_return)
        break
      elif river_crossing2 == 2:
        print(raft_return)
      else:
        print(search)
        while True:
          try:
            search_choice = input("\nWould you like to take the canoe across? 'Y' or 'N'\n\nMake your selection: ").upper()
          except ValueError:
            continue
          if search_choice == "Y" or search_choice == "N":
            break
          else:
            print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
        if search_choice == "Y":
          print(canoe)
        else:
          print("\nYou sure? Okay, I guess you like carrying that heavy treasure chest around all day. Well, back the way you came.")
          while True:
            try:
              river_crossing3 = int(input("\nHow would you like to cross the river?\n\nRope Bridge = 1\nRaft = 2\n\nMake your selection: "))
            except ValueError:
              continue
            if 1 <= river_crossing3 <= 2:
              break
            else:
              print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
          if river_crossing3 == 1:
            clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print(rip)
            print(bridge_return)
            break
          else:
            print(raft)

  # Grabbed treasure and swam during 1st river crossing
    elif treasure == 1 and river_crossing == 3:
      print("There is still the rope bridge, as well as the raft. Sadly, you did not use it earlier, so it is still on the other side of the river. You could leave the treasure and swim over to retrieve the raft or search further down the bank and see if there is another way of crossing.")
      while True:
        try:
          river_crossing2_alt = int(input("How would you like to cross the river?\n\nRope Bridge = 1\nSwim = 2\nSearch = 3\n\nMake your selection: "))
        except ValueError:
          continue
        if 1 <= river_crossing2_alt <= 3:
          break
        else:
          print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
      if river_crossing2_alt == 1:
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print(rip)
        print(bridge_return)
        break
      elif river_crossing2_alt == 2:
        print(swim)
        while True:
          try:
            river_crossing2_final = int(input("\nThat sure was a nasty hit. There won't be anymore swimming today, so that leaves you with two options to get across this river.  You can take the rope bridge or search along the bank for another way of crossing, though that won't be pleasant given the pain your in from that log encounter.\n\nHow would you like to cross the river?\nRope Bridge = 1\nSearch = 2\n\nMake your selection: "))
          except ValueError:
            continue
          if 1 <= river_crossing2_final <= 2:
            break
          else:
            print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****\n")
        if river_crossing2_final == 1:
          clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
          clearConsole()
          print(rip)
          print(bridge_return)
          break
        else:
          print(search)
          while True:
            try:
              search_choice2 = input("Would you like to take the canoe across? 'Y' or 'N'\n\nMake your selection: ").upper()
            except ValueError:
              continue
            if search_choice2 == "Y" or search_choice2 == "N":
              break
            else:
              print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
          if search_choice2 == "Y":
            print(canoe)
          else:
            clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print(rip)
            print(f"\nYou sure? {bridge_return}")
            break
      else:
        print(search)
        while True:
          try:
            search_choice3 = input("Would you like to take the canoe across? 'Y' or 'N'\n\nMake your selection: ").upper()
          except ValueError:
            continue
          if search_choice3 == "Y" or search_choice3 == "N":
            break
          else:
            print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
        if search_choice3 == "Y":
          print(canoe)
        else:
          print("\nYou sure? Okay, I guess you like carrying that heavy treasure chest around all day. Well, back the way you came.")
          while True:
            try:
              river_crossing3_alt = int(input("How would you like to cross the river?\n\nRope Bridge = 1\nSwim = 2\n\nMake your selection: "))
            except ValueError:
              continue
            if 1 <= river_crossing3_alt <= 2:
              break
            else:
              print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
          if river_crossing3_alt == 1:
            clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
            clearConsole()
            print(rip)
            print(bridge_return)
            break
          else:
            print(swim)
            while True:
              try:
                river_crossing2_final2 = int(input("\nThat sure was a nasty hit. There won't be anymore swimming today, so that leaves you with two options to get across this river.  You can take the rope bridge or go back and use the canoe, though that won't be pleasant given the pain your in from that log encounter.\n\nHow would you like to cross the river?\nRope Bridge = 1\nCanoe = 2\n\nMake your selection: "))
              except ValueError:
                continue
              if 1 <= river_crossing2_final2 <= 2:
                break
              else:
                print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
            if river_crossing2_final2 == 1:
              clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
              clearConsole()
              print(rip)
              print(bridge_return)
              break
            else:
              print(canoe)

  # Used rope for lasso and crossed 1st river on raft
    elif treasure == 2 and river_crossing == 2:
      print("Well, the rope bridge was destroyed when you used a segment of it to make that terrible lasso. Fortunately, you used the raft to get across the river earlier, otherwise it would be on the other side and you would need to swim to retrieve it. The only other option is to search further down the bank and see if there is another way of crossing.\n")
      while True:
        try:
          river_crossing4 = int(input("\nHow would you like to cross the river?\n\nRaft = 1\nSearch = 2\n\nMake your selection: "))
        except ValueError:
          continue
        if 1 <= river_crossing4 <= 2:
          break
        else:
          print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
      if river_crossing4 == 1:
        print(raft)
      else:
        print(search)
        while True:
          try:
            search_choice4 = input("Would you like to take the canoe across? 'Y' or 'N'\n\nMake your selection: ").upper()
          except ValueError:
            continue
          if search_choice4 == "Y" or search_choice4 == "N":
            break
          else:
            print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
        if search_choice4 == "Y":
          print(canoe)
        else:
          print(f"\nWell, you destroyed the rope bridge with the lasso idea and you have turned down the canoe. Kind of limiting yourself here aren't you? Okay..\n{raft}\n")
          input("Press 'enter'..\n")

  # Used rope for lasso and swam 1st river on raft
    elif treasure == 2 and river_crossing == 3:
      print("Well, the rope bridge was destroyed when you used a segment of it to make that terrible lasso. Sadly, you swam across the river ealier so the raft is still on the other side. You could leave the treasure and swim over to retrieve the raft or search further down the bank and see if there is another way of crossing.\n")
      while True:
        try:
          river_crossing5 = int(input("How would you like to cross the river?\n\nSwim = 1\nSearch = 2\n\nMake your selection: "))
        except ValueError:
          continue
        if 1 <= river_crossing5 <= 2:
          break
        else:
          print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
      if river_crossing5 == 1:
        print(swim)
        print("\nThat sure was a nasty hit. There won't be anymore swimming today, so that leaves you with only one option. You have to search the bank for another way to cross. This will be quite uncomfortable after your log encounter and who knows what will happen if you have to defend yourself along the way.\n")
        input("Press 'enter'\n")
        print("Fortunately for you, there was a canoe not to far away and you were able to use it to safely traverse the river.\n")
      else:
        print(search)
        while True:
          try:
            search_choice5 = input("Would you like to take the canoe across? 'Y' or 'N'\n\nMake your selection: ").upper()
          except ValueError:
            continue
          if search_choice5 == "Y" or search_choice5 == "N":
            break
          else:
            print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
        if search_choice5 == "Y":
          print(canoe)
        else:
          print(f"\nWell, you destroyed the rope bridge with the lasso idea and you have turned down the canoe. Kind of limiting yourself here aren't you? Okay..{swim}")
          input("Press 'enter'..\n")
          print("That sure was a nasty hit. There won't be anymore swimming today, so using that raft is out. Looks like you'll just have to take your chances with the canoe.")
          input("Press 'enter'\n")
          print("Fortunately, you were still able to manage the canoe well enough to safely traverse the river.")

    input("\nPress 'enter'..")
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()

    pirate_ship = ('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠒⠒⠀⣠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠏⠈⠉⠉⠉⣠⡿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⢀⣠⢾⠿⡇⢈⣷⣤⣄⠀⠀⠀⠀⠉⠉⠛⠛⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠶⠦⠶⠒⠚⢉⣀⡤⠾⠛⠉⢹⠁⠈⠉⠒⠲⠤⠤⠤⠔⠒⢻⣻⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⡿⠀⢀⣀⣠⢼⡟⠁⠀⠀⠀⠀⣿⣧⡀⠀⠀⠀⠀⠀⢀⣴⡋⣻⣌⣡⣿⣶⣶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣴⣿⣚⣽⠟⠁⢸⣧⣦⣤⣄⣤⣄⣽⡻⣿⣆⡀⠀⠀⢶⣟⣛⣻⣿⣿⠶⠞⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠿⣷⢿⣿⡉⠁⠀⠀⣸⣿⣿⣿⠿⣿⠛⢛⣻⣾⣿⣿⠶⠂⠀⠀⠉⢀⣿⡟⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠏⢸⣿⡝⢦⣀⣰⠃⣸⣿⡤⣾⠿⠛⣋⡥⣤⠞⠁⠀⠀⠀⢀⣴⡟⢸⡅⢨⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⢻⠇⠀⣾⡟⢳⡤⣾⠟⢋⣉⡤⢤⡟⠚⠉⠀⢠⣿⠀⠀⠀⢀⡴⠋⡽⠀⣸⣇⣲⣤⣼⣷⠶⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⠋⢠⡏⠀⡸⠁⣇⡀⢻⡏⠈⠉⠀⠀⡾⠀⠀⠀⠀⡏⠘⡆⠀⠶⢿⠖⠒⠛⠋⠉⠉⠀⣴⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠞⠁⠀⠀⣼⠀⢠⠃⠀⣷⠀⣼⠻⣄⠀⠀⣼⠁⠀⠀⠀⠀⡇⠀⢹⡀⠀⡞⠀⠀⠀⠀⠀⠀⢸⡿⣶⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⡤⠞⠉⠀⠀⠀⠀⠀⢯⢀⡏⢸⠁⣿⠀⣧⠀⢹⡄⢠⠇⠀⠀⠀⠀⠀⢧⠀⠀⢳⠀⡇⢰⠀⠀⠀⠀⠀⢸⡇⢣⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣶⣋⣡⣤⣀⣀⣄⠀⡄⢠⠀⠘⣿⢀⡇⠀⣿⠀⢹⠀⡸⣿⡟⠀⢰⠀⡀⠀⠀⠸⡆⠀⠈⣇⢧⢸⣸⣀⡀⠀⠀⠈⣷⡈⡎⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠛⠛⠿⢿⣍⣉⠉⠛⠿⠿⣿⣷⣿⣿⣶⣶⣤⣼⠀⠀⣿⠀⠘⣧⣷⡿⢿⣦⣬⣧⣷⣤⡀⠀⠹⡄⠀⠘⣆⣴⣧⠁⢱⣄⢠⠀⠘⢧⡸⠈⢧⠀⠀⠀⠀⢀⠀⠀⠀
⠀⠀⠀⠀⠀⠉⠛⠷⣦⣤⣀⡀⠈⣹⠟⠻⣿⣿⣦⣀⣿⠀⠀⢹⣿⢷⣼⣿⣿⣏⣻⣷⠙⣤⣤⣽⣆⠀⠸⡍⠻⣷⣼⣿⣿⣷⣶⣬⣷⣦⠈⢧⠀⠀⠀⣹⣷⠄⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣷⣦⣴⣇⣀⠉⢻⣿⣄⣴⠋⠉⠻⣿⣿⠟⠿⣻⡟⠉⠉⠛⠛⠿⣷⣄⠹⡄⢯⣼⢿⣿⠋⠉⠙⠛⠻⣷⣬⣷⣴⣟⣿⣷⣾⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣾⣿⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀
⠀⠀⠀⠀⠀     ⠀⠀⠀⠀⠈⠻⠿⢿⠿⢿⡛⠿⠿⢿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿''')
    print(pirate_ship)

# Pirate ship art -- https://emojicombos.com/pirate-ship

  #Ship return scenario
    print("\nWhew, that was quite the adventure and it sure has paid off! Now that you have made it back to the ocean, there is only one thing left to do. It is time to get back on your ship, set sail and enjoy your newfound wealth!")

  #Ship return choices
    victory = ("\nCongratulations on finding the treasure and surviving long enough to enjoy it! Thank you so much for playing. I encourage you to play it again while making new decisions to see what fate has in store!")
    dinghy_return = ("\nTo the dinghy! Remembering that this ocean was teaming with sharks, you take your time and safely make it back to your ship. Once through the pass, you can start thinking of what you will buy first!\n")
    board_ship = ("\nTo the ship! As you climb aboard, you remember that your hull took that big hit when approaching the docks. A little concerning, but things appear to be okay. Besides, with the treasure she will be the envy of the seas very soon!\n")
    swim_return = ("\nOh my.. I can't believe you forgot that these waters were shark infested. I am afraid you aren't going to survive this one.\n\nThank you so much for playing. I encourage you to play it again while making new decisions to see what fate has in store!")

  # Disembarked with dingy
    if disembark == 1:
      while True:
        try:
          ocean_return = int(input("\nYour dinghy awaits, would you like to climb aboard and row back to your ship or take a short, refreshing swim near the docks?\n\nDinghy = 1\nSwim = 2\n\nMake your selection: "))
        except ValueError:
          continue
        if 1 <= ocean_return <= 2:
          break
        else:
          print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
      if ocean_return == 1:
        print(dinghy_return)
        input("Press 'enter'..\n")
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print(treasure_ascii)
        print(victory)
        break
      else:
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print(rip)
        print(swim_return)
        break
  # Pulled into dock
    elif disembark == 2:
      while True:
        try:
          dock_return = int(input("Your beautiful ship awaits its victor! Shall you board with your bounty or take a short, refreshing dip near the docks before setting sail?\n\nBoard = 1\nSwim = 2\n\nMake your selection: "))
        except ValueError:
          continue
        if 1 <= dock_return <= 2:
          break
        else:
          print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
      if dock_return == 1:
        print(board_ship)
        input("Press 'enter'..\n")
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print(pirate_ship)
        print("\nShortly after pulling away from the docks, your ship again strikes something beneath the waves. Sadly, the combination of blows has ruptured the hull and the ship is taking on water quickly.  There is no way you can turn around in time to make it back to the docks, the ship is doomed!\n")
        print("You have two choices, well three if we count going down with the ship, but I think we can agree to take that one off the table. So, you can try and launch the dinghy in hopes of saving the treasure, though there may not be time or you save yourself by diving into the ocean and swimming ashore.\n")
        while True:
          try:
            escape = int(input("How do you wish to escape the sinking ship?\n\nDinghy = 1\nSwim = 2\n\nMake your selection: "))
          except ValueError:
            continue
          if 1 <= escape <= 2:
            break
          else:
            print("\n**** Whoops, let's try that again. Remember to select one of the provided options.****")
        if escape == 1:
          print("\nTo the dinghy! It was close, but you just managed to get you and the treasure aboard before the ship went under. There are times when greed kills, but given the number of sharks now circling the area, it probably saved your life -- for now.")
          input("\nPress 'enter'..")
          clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
          clearConsole()

          print('''
                                      ⣤⠤⠒⠒⠒⠊⠉⠉⠙⠓⠒⠢⢤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⣀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⢀⡤⣾⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⡴⢿⣻⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀⠀
                        ⠀⠀⢠⣞⣷⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⡄⠀⠀
                        ⠀⢰⢟⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀
                        ⢀⣾⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣻⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀
                        ⢸⢻⣿⣿⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠉⠉⢻⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀
                        ⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠃⠀⠀⠈⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
                        ⢿⣿⣿⣿⣿⣶⣶⣦⣤⣤⣤⣀⡀⠀⠀⠀⡾⠀⠀⠀⠀⣽⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇
                        ⠀⠀⠀⠀⠉⠉⠉⠛⠛⠛⠛⠿⠿⠿⠛⠛⠃⠀⠀⢀⣼⣿⡿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠁
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠁⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢎⣻⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡽⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣽⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣼⣻⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣏⣾⣽⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣹⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣾⣦⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣧⣿⣿⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠙⠛⠓⠒⠒⠒⠒⠊⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣤⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠾⣭⣽⣯⠿⠛⠉⠉⠉⠉⠓⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣹⣦⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣷⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⡿⣧⣽⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣟⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⢽⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠻⠦⣄⣀⣀⣀⣠⠔⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
# Question mark art -- https://emojicombos.com/question-mark

          print("\nWill you make it back to the island or will the waves tip your dinghy and leave you at the mercy of the sharks? Perhaps another vessel will arrive in search of treasure and you can barter passage or commandeer it. Only the fates know such things.\n\nThank you so much for playing. I encourage you to play it again while making new decisions to see what fate has in store!")
          break
        else:
          clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
          clearConsole()
          print(rip)
          print(swim_return)
          break
      else:
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()
        print(rip)
        print(swim_return)
        break

# Restart game - prompt in different color
while True:
  start_game()
  replay = input("\n\033[36mWould you like to play again? 'Y' or 'N'\033[0m: ").upper()
  if replay == "Y":
    # Clear console to reduce clutter
    import os
    clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
    clearConsole()
    continue
  else:
    break
