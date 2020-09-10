######################
#PreDefined Functions#
######################

def char_stats():
        power = 5
        luck = 5
        inventory = 4
        


##############
#Prints Title#
##############
title = "The Dungeon Of Misleads"
print('\n\n'+title+'\n\n')
###################
#Startup From Menu#
###################
start = input("Type'start' To Begin The Dungeon Exploration: ")
while start != 'start':
        start = input("That isnt 'start', please type 'start': ")
if start == 'start':
        print ("\n\nYour a Bold Soul I See. Welcome, And Lets Begin!!!\n\n")
        print ("So The Rules Are Simple,\n\n")
        print ("You Are in a Virtual World With Controls To a Heroic Character. Yay!!! \nYou will begin at the forefront of a dungeon. Inside the Dungeon You will\nuse The commands N,S,W,E to Traverse the virtual Environment")

############################
#Do You Understand Debugged#
############################
answer1 = input("Do you understand so far? 'yes' or 'no': ")
while answer1 != 'yes' and answer1 != 'no':
        answer2 = input("Type 'yes' or 'no': ")
        if answer2 == 'yes':
                answer1 = answer2
                break
        if answer2 == 'no':
                answer1 = answer2
                break
###########################
#More Info PreGame Prompts#
###########################
while answer1 == "no":
   print ( "\n\nI See You Need More Info\n\n")
   print (" 1)Dungeon\n 2)Virtual World\n 3)Commands\n 4)<---nothing(continue)")
   more_info1 = input("\n\nwhat do you want to know: ")
   if more_info1 == ('dungeon') or more_info1 == ('1') or more_info1 == ('Dungeon'):
        print ("\n\n\nThe Dungeon Is a Cave filled with mystery and different hidden treasures.\nThe dungeon is the environment in which you explore and the main area in which \nyou explore to progress in the story.collect items and complete certain tasks\nto unlock an ending path of your choice for you're hero\n\n\n")
   if more_info1 == ('virtual world') or more_info1 == ('2') or more_info1 == ('Virtual World'):
        print( "\n\n\nA virtual world is a simulated space in this game in which your characters\nmoves around in. its like a pretend playground, or a cyber world. you will not\nbe able to see where you're character is physically but rather text based guidance\nwill be used. Follow the text and roam around to see mentally whats in your characters surroundings.\n\n\n")
   if more_info1 == ("commands"):
        print("\n\n\nThe Commands are your Moving Mechanics. you tell your character to move in the direction\nof the command such that it corresponds to a compass. 'N', 'E', 'W', 'S' Relates to\nNorth, East, West, and South respectively.Based on your input, your character will virtually move that way. \n\n\nNOTE:IT IS RECOMMENDED TO KEEP YOUR CAPS LOCK TURNED 'ON', OTHERWISE YOU WILL HAVE TO HOLD\nSHIFT EACH TIME YOU INPUT A DIRECTION\n\n\n")
   if more_info1 == ("nothing"):
                answer1 = "yes"
##########################
#Character Custom Prompts#
##########################
if answer1 == "yes":
        print ("Great!!!")
        print("Next up is your playable character. You can customize your characters color and name.\nyou will be given a list of colors to choose from\nand you will put in whatever name you like.Also, The color and name sorta matters.\ngood luck")
color = input("choose your color:\n1)blue\n2)green\n3)white\n4)black")
name = input ("What Would you Want your character name to be?: ")
print( "okay " + name + ",Lets Get started" )
############################################
#Entering The Dungeon With Random Backstory#
############################################
