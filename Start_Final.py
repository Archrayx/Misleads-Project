##############
#Import Tools#
##############
import os
######################
#PreDefined Functions#
######################

def start():
    clear = lambda: os.system('cls')


    ##############
    #Prints Title#
    ##############
    title = "The Dungeon Of Misleads"
    print('\n\n'+title+'\n\n')
    ###################
    #Startup From Menu#
    ###################
    start = input("Type 'start' To Begin The Dungeon Exploration: ").lower()
    while start != 'start':
            start = input("That isnt 'start', please type 'start': ").lower()
    if start == 'start':
            clear()
            print ("\n\nYour a Bold Soul I See. Welcome, And Lets Begin!!!\n\n")
            print ("So The Rules Are Simple,\n\n")
            print ("You Are in a Virtual World With Controls To a Heroic Character. Yay!!! \nYou will begin at the forefront of a dungeon. Inside the Dungeon You will\nuse The commands N,S,W,E to Traverse the virtual Environment")
    ############################
    #Do You Understand Debugged#
    ############################
    answer1 = input("Do you understand so far? (y/n): ").lower()
    while answer1 != ('y') and answer1 != ('n'):
            answer2 = input("Type 'y' or 'n': ")
            if answer2 == ('y') or answer2 == ('n'):
                    answer1 = answer2
                    clear()
    ###########################
    #More Info PreGame Prompt#
    ###########################
    while answer1 == 'n':

       print ( "\n\nI See You Need More Info\n\n")
       print (" 1)Dungeon\n 2)Virtual World\n 3)Commands\n 4)Equipment\n 5)<---Nothing(Continue)")
       more_info1 = input("\n\nwhat do you want to know: ").lower()
       clear()
     ###########
     #More Info#
     ###########
       if more_info1 == ('dungeon') or more_info1 == ('1'):
            print ("\n\n\nThe Dungeon Is a Cave filled with mystery and different hidden treasures.\nThe dungeon is the environment in which you explore and the main area in which \nyou explore to progress in the story. Collect items and complete certain tasks\nto unlock an ending path of your choice for you're hero.\n\n\n")

       elif more_info1 == ('virtual world') or more_info1 ==  ('2'):
            print( "\n\n\nA virtual world is a simulated space in this game in which your characters\nmoves around in. Its like a pretend playground, or a cyber world. You will not\nbe able to see where you're character is physically but rather text based guidance\nwill be used. Follow the text and roam around to see mentally whats in your characters surroundings.\n\n\n")

       elif more_info1 == more_info1 == ('equipment') or more_info1 == ('4'):
            print("\n\n\nIn Game you will be given opportunities to find 'Equipment' and 'Items' to\nhelp you through your journey getting through the dungeon. At the very beginning\nyou will be given the option to choose between extra equipment that will \neither increase item slots(Bag), strength(sword) or luck(flashlight). You will be able\nto find better extra equipment while exploring, but the starting options\n help with the users progress in different ways.\n\n\n")

       elif more_info1 == ('commands') or more_info1 == ('3'):
            print("\n\n\nThe Commands are your Moving Mechanics. You tell your character to move in the direction\nof the command such that it corresponds to a compass. 'N', 'E', 'W', 'S' Relates to\nNorth, East, West, and South respectively. Based on your input, your character will virtually move that way. \n\n\nNOTE:IT IS RECOMMENDED TO KEEP YOUR CAPS LOCK TURNED 'ON', OTHERWISE YOU WILL HAVE TO HOLD\nSHIFT EACH TIME YOU INPUT A DIRECTION\n\n\n")

       elif more_info1 == ('nothing') or more_info1 == ('5') or more_info1 ==  ('continue'):
            answer1 = 'y'
       else:
           print("\n\n\nType one of the more info options\n\n\n")
    ##########################
    #Character Custom Prompts#
    ##########################
    if answer1 == "y":
            clear()
            print ("\n\nGreat!!!\n\n")
            print("Next up is your playable character. You can customize your characters Color,\nEquipment, and Name. You will be given a list of colors to choose from and \nyou will put in whatever name you like along with your choice of equipment.\n\nAlso, ALL CHOICES MATTER.\n\n\ngood luck!!!\n\n")

    #######################################
    #Color Debugged + Are You Sure? Prompt#
    #######################################
    color1 = input("choose your color:\n1)blue\n2)yellow\n3)white\n4)pink\n\n").lower()
    while color1 == ('blue')  or color1 == ('yellow') or color1 == ('white') or color1 == ('pink'):
            ays2 = input("Are You Sure? (y/n): ").lower()
            if ays2 == 'y':
                clear()
                break
            elif ays2 == 'n':
                    color1 = 'random'


    while color1 != ('blue') and color1 != ('yellow') and color1 != ('white') and color1 != ('pink'):
            color2 = input("choose a color from the list: ").lower()
            if color2 == ('blue') or color2 == ('yellow') or color2 == ('white') or color2 == ('pink'):
                    ays2 = input("Are You Sure? (y/n): ").lower()
                    if ays2 == 'y':
                       color1 = color2
                       clear()
                    elif ays2 == 'n':
                       color1 = 'random'
                    else:
                        print('Your input wasn\'t a yes, so your answer was changed to no')
                        color1 = 'random'


    ########################################
    #Equipment Debug + Are You Sure? Prompt#
    ########################################
    equipment1 = input("What kind of extra equipment would you like to carry into the dungeon?\n\n1)Sword(strength)\n2)Bag(Inventory)\n3)Flashlight(luck)\n\n").lower()
    while equipment1 == ('sword') or equipment1 == ('bag') or equipment1 == ('flashlight') or equipment1 == ('1') or equipment1 == ('2') or equipment1 == ('3'):
          ays1 = input("Are you sure you? (y/n): ").lower()
          if ays1 == 'y':
              clear()
              break
          if ays1 == 'n':
             equipment1 = 'random'

    while equipment1 != ('sword') and equipment1 != ('bag') and equipment1 != ('flashlight') and equipment1 != ('1') and equipment1 != ('2') and equipment1 != ('3'):
            equipment2 = input("Choose an Appropriate Equipment: ").lower()
            if equipment2 == ('sword') or equipment2 == ('bag') or equipment2 == ('flashlight') or equipment2 == ('1') or equipment2 == ('2') or equipment2 == ('3'):
                    ays1 = input('Are you sure you? (y/n): ').lower()
                    if ays1 == 'y':
                       equipment1 = equipment2
                       clear()
                    elif ays1 == 'n':
                       equipment1 = 'random'
                    else:
                        print('Your input wasn\'t a yes, so your answer was changed to no')
                        equipment1 = 'random'



    ###############
    #Entering Name#
    ###############
    name_bool = True
    while name_bool == True :
        name = input ("What Would you Want your character name to be?: ")
        ays3 = input ("Are You Sure? (y/n):")
        while ays3 not in ('y', 'n'):
            ays3 = input(" Please type 'y' or 'n': ")
        if ays3 == 'y':
            name_bool = False




    print( "okay " + name + ", Lets Get started" )
    ############################################
    #Entering The Dungeon With Random Backstory#
    ############################################
start()
