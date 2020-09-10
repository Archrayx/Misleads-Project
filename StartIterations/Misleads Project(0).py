title = "The Dungeon Of Misleads"

print(title)

print (" ")
start = input("Type \"start\" To Begin The Dungeon Exploration: ")

if start == 'start':
    print (" ")
    print ("Your a Bold Soul I See. Welcome, And Lets Begin!!!")
    print (" ")
    print ("So The Rules Are Simple,")
    print (" ")
    print ("You Are in a Virtual World With Controls To a Heroic Character. Yay!!! \nYou will begin at the forefront of a dungeon. Inside the Dungeon You will\nuse The commands \"N\",\"S\",\"E\", and \"W\" to Traverse the virtual Environment")

answer1= input("Do you understand so far? \'yes\' or \'no\': ")

if answer1 == "yes":
    print ("Great!!!")
while answer1 == "no":
        print ( "\n\nI See You Need More Info\n\n")
        print(" 1)Dungeon\n 2)Virtual World\n 3)Commands")
        more_info1 = input("\n\nwhat dont you understand:")
        if more_info1 == ("dungeon" or "1"):
            print ("\n\n\nThe Dungeon Is a Cave filled with mystery and different hidden treasures.\nThe dungeon is the environment in which you explore and the main area in which \nyou explore to progress in the story.collect items and complete certain tasks\nto unlock an ending path of your choice for you're hero\n\n\n")
        if more_info1 == ("virtual world" or "2"):
            print( "\n\n\nA virtual world is a simulated space in this game in which your characters\nmoves around in. its like a pretend playground, or a cyber world. you will not\nbe able to see where you're character is physically but rather text based guidance\nwill be used. Follow the text and roam around to see mentally whats in your characters surroundings.\n\n\n")
        if more_info1 == ("commands" or "3"):
            print ("\n\n\nThe Commands are your Moving Mechanics. you tell your character to move in the direction\nof the command such that it corresponds to a compass. 'N', 'E', 'W', 'S' Relates to\nNorth, East, West, and South respectively.Based on your input, your character will virtually move that way. \nNOTE:IT IS RECOMMENDED TO KEEP YOUR CAPS LOCK TURNED 'ON', OTHERWISE YOU WILL HAVE TO HOLD\nSHIFT EACH TIME YOU INPUT A DIRECTION\n\n\n")
                           


name = input ("What Would you Want your character name to be?: ")

print( "okay " + name + ",Lets Get started" )
