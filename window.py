#########
#modules#
#########

import turtle
import winsound
from pathlib import Path
#from global_vars import *


#########################
#SPRITES AND BACKGROUNDS#
#########################

choice = input("enter 1 or 2: ")
Choices = False

while Choices == False:
    if choice == "1":
        pill = "mislead_Sprites/type1/pellet.gif"
        megaman = "mislead_Sprites/type1/megaman.gif"
        megaman2 = "mislead_Sprites/type1/megaman2.gif"
        megaman3 = "mislead_Sprites/type1/megaman3.gif"
        megaman4 = "mislead_Sprites/type1/megaman4.gif"
        megaman_crouch = "mislead_Sprites/type1/megaman_crouch.gif"
        megaman_left_crouch = "mislead_Sprites/type1/megaman_left_crouch.gif"
        megaman_jump = "mislead_Sprites/type1/megaman_jump.gif"
        megaman_left_jump = "mislead_Sprites/type1/megaman_left_jump.gif"
        megaman_left = "mislead_Sprites/type1/megaman_left.gif"
        megaman_left2 = "mislead_Sprites/type1/megaman_left2.gif"
        megaman_left3 = "mislead_Sprites/type1/megaman_left3.gif"
        megaman_left4 = "mislead_Sprites/type1/megaman_left4.gif"
        image = "mislead_Sprites/type1/stage.png"
        Choices = True
    elif choice == "2":
        pill = "mislead_Sprites/type2/pellet.gif"
        mega = "mislead_Sprites/type2/mega.gif"
        mega_left = "mislead_Sprites/type2/mega_left.gif"
        megaman = "mislead_Sprites/type2/megaman.gif"
        megaman2 = "mislead_Sprites/type2/megaman2.gif"
        megaman3 = "mislead_Sprites/type2/megaman3.gif"
        megaman4 = "mislead_Sprites/type2/megaman4.gif"
        megaman_crouch = "mislead_Sprites/type2/megaman_crouch.gif"
        megaman_left_crouch = "mislead_Sprites/type2/megaman_left_crouch.gif"
        megaman_jump = "mislead_Sprites/type2/megaman_jump.gif"
        megaman_left_jump = "mislead_Sprites/type2/megaman_left_jump.gif"
        megaman_left = "mislead_Sprites/type2/megaman_left.gif"
        megaman_left2 = "mislead_Sprites/type2/megaman_left2.gif"
        megaman_left3 = "mislead_Sprites/type2/megaman_left3.gif"
        megaman_left4 = "mislead_Sprites/type2/megaman_left4.gif"
        image = "mislead_Sprites/type2/stage2.png"
        Choices = True
    else:
        choice = input("incorrect input, type number (1 or 2): ")


##############
#Screen SETUP#
##############

wn = turtle.Screen()
wn.title("Misleads Dungeon")
wn.setup(width = 800, height = 600)
wn.bgcolor("black")
wn.bgpic(image)
#wn.tracer(0)
#screentext
#choice = wn.textinput("DML", "CHOOSE YOUR CHARACTER,\n1.) PROTOMAN, OR MEGAMAN (1 OR 2): ")

#######
#SOUND#
#######
winsound.PlaySound("mmbn3_theme.wav", winsound.SND_ASYNC)
##################
#ADD SPRITE SHAPE#
##################
#if choice == "2":
#    wn.addshape(mega)
#    wn.addshape(mega_left)
wn.addshape(pill)
wn.addshape(megaman)
wn.addshape(megaman2)
wn.addshape(megaman3)
wn.addshape(megaman4)
wn.addshape(megaman_crouch)
wn.addshape(megaman_left_crouch)
wn.addshape(megaman_jump)
wn.addshape(megaman_left_jump)
wn.addshape(megaman_left)
wn.addshape(megaman_left2)
wn.addshape(megaman_left3)
wn.addshape(megaman_left4)

##################
#CHARACTER OBJECT#
##################

char = turtle.Turtle()
char.shape(megaman)
char.penup()
char.speed(0)
char.goto(-350, 0)
char.dx = 10
char.dy = 10

###############
#PELLET OBJECT#
###############
pellet = turtle.Turtle()
pellet.penup()
pellet.speed(0)
pellet.dx = 30


##########################
#ANIMATION POSITION CHECK#
##########################

position = 0
def positions():
    global position
    if position == -2:
        char.shape(mega_left)
    if position == -1:
        char.shape(mega)
    if position == 0:
        char.shape(megaman)
    if position == 1:
        char.shape(megaman2)
    if position == 2:
        char.shape(megaman3)
    if position == 3:
        char.shape(megaman4)
    if position == 4:
        char.shape(megaman_left)
    if position == 5:
        char.shape(megaman_left2)
    if position == 6:
        char.shape(megaman_left3)
    if position == 7:
        char.shape(megaman_left4)
    if position == 8:
        char.shape(megaman_jump)
    if position == 9:
        char.shape(megaman_crouch)
    if position == 10:
        char.shape(megaman_left_jump)
    if position == 11:
        char.shape(megaman_left_crouch)


#########################################
#POSITION CHECK/LEFT AND RIGHT ANIMATION#
#########################################
NUETRAL = True
RIGHT = False
LEFT = False
JUMP = False
MAX_HEIGHT = False
FALL = False
CROUCH = False
PELLET = False

def UP_MOVE():
    char.sety(char.ycor() + char.dy)
def DOWN_MOVE():
    char.sety(char.ycor() - char.dy)
def RIGHT_MOVE():
    char.setx(char.xcor() + char.dx)
def LEFT_MOVE():
    char.setx(char.xcor() - char.dx)

##################
#PELLET ANIMATION#
##################


def PELLET_MOVE():
    global position
    global PELLET
    char.dx = 20
    char.dy = 20
    pellet_pos = char.xcor()
    pellet.showturtle()
    pellet.shape(pill)
    pellet.color("green")
    if position == (0) or position == (1) or position == (2) or position == (3) or position == (8) or position == (9):
        pellet.setx(pellet.xcor() + pellet.dx)
        if pellet.xcor() >= (pellet_pos + 150):
            char.dx = 10
            char.dy = 10
            pellet.hideturtle()
            PELLET = False
    if position == (4) or position == (5) or position == (6) or position == (7) or position == (10) or position == (11):
        pellet.setx(pellet.xcor() - pellet.dx)
        if (pellet.xcor()) <= (pellet_pos - 150):
            char.dx = 10
            char.dy = 10
            pellet.hideturtle()
            PELLET = False

#################################
#ALL OTHER ANIMATION/CHECK FUNC.#
#################################
def walk_animation_right():
    global position
    if position == 8 or position == 10:
        return
    elif position >= 3 :
        position = 0
    position += 1
    positions()


def walk_animation_left():
    global position
    if position == 8 or position == 10:
        return
    elif position >= 7 or position < 4:
        position = 4
    position += 1
    positions()


def jump_check():
    global position
    if position == (0) or position == (1) or position == (2) or position == (3) or position == (8) or position == (9):
        position = 8
    if position == (4) or position == (5) or position == (6) or position == (7) or position == (10) or position == (11):
        position = 10
    positions()

def max_height_check():
    global MAX_HEIGHT
    if char.ycor() >= 80:
        MAX_HEIGHT = True
        while MAX_HEIGHT == True and char.ycor() >= 0:
            DOWN_MOVE()
            if RIGHT == True and char.ycor() >= 0:
                RIGHT_MOVE()
            if LEFT == True and char.ycor() >= 0:
                LEFT_MOVE()
            if char.ycor() <= 0:
                MAX_HEIGHT = False

def fall_check():
    global position
    if position == (0) or position == (1) or position == (2) or position == (3) or position == (8) or position == (9):
        position = 8
    if position == (4) or position == (5) or position == (6) or position == (7) or position == (10) or position == (11):
        position = 10
    positions()


def crouch_check():
    global position
    if position == (0) or position == (1) or position == (2) or position == (3) or position == (8) or position == (9):
        position = 9
    if position == (4) or position == (5) or position == (6) or position == (7) or position == (10) or position == (11):
        position = 11
    positions()

def uncrouch_check():
    global position
    if position == (0) or position == (1) or position == (2) or position == (3) or position == (8) or position == (9):
        position = 0
    if position == (4) or position == (5) or position == (6) or position == (7) or position == (10) or position == (11):
        position = 4
    positions()




###################
#KEYBIND FUNCTIONS#
###################


#################################
#WALKING RIGHT/NUETRAL FUNCTIONS#
#################################

def char_right():
    global RIGHT
    RIGHT = True


def char_right_nuetral():
    global position
    global RIGHT
    RIGHT = False
    if position == 8 or position == 10:
        return
    position = 0
    positions()

################################
#WALKING LEFT/NUETRAL FUNCTIONS#
################################

def char_left():
    global LEFT
    LEFT = True

def char_left_nuetral():
    global position
    global LEFT
    LEFT = False
    if position == 8 or position == 10:
        return
    position = 4
    positions()


#######################
#PELLET SHOOT FUNCTION#
#######################
def pellet_shoot():
    global PELLET
    PELLET = True
    pellet.goto(char.xcor(), char.ycor())


#####################
#JUMP/FALL FUNCTIONS#
#####################

def char_jump():
    global JUMP
    global FALL
    FALL = False
    JUMP = True
    jump_check()


def char_fall():
    global JUMP
    global FALL
    JUMP = False
    FALL = True
    fall_check()

###########################
#CROUCH/UNCROUCH FUNCTIONS#
###########################

def char_crouch():
    global position
    global CROUCH
    CROUCH = True
    crouch_check()


def char_uncrouch():
    global position
    global CROUCH
    CROUCH = False
    if position == 8 or position == 10:
        return
    uncrouch_check()




###################
#KEYBOARD BINDINGS#
###################
wn.listen()
wn.onkeypress(char_right, "d")
wn.onkeyrelease(char_right_nuetral,"d")
wn.onkeypress(char_left, "a")
wn.onkeyrelease(char_left_nuetral,"a")
wn.onkeypress(char_jump, "w")
wn.onkeyrelease(char_fall,"w")
wn.onkeypress(char_crouch,"s")
wn.onkeyrelease(char_uncrouch,"s")
wn.onkeypress(pellet_shoot,"space")

while True:
    wn.update()
################################
#CONSTANT MOVEMENT OF CHARACTER#
################################





    if NUETRAL == True and PELLET == True:
        PELLET_MOVE()

    while JUMP == True and CROUCH == False:
        max_height_check()
        UP_MOVE()
        if PELLET == True:
            PELLET_MOVE()
        if LEFT == True:
            position = 10
            positions()
            LEFT_MOVE()
            if PELLET == True:
                PELLET_MOVE()
        if RIGHT == True:
            position = 8
            positions()
            RIGHT_MOVE()
            if PELLET == True:
                PELLET_MOVE()


    while LEFT == True:
        LEFT_MOVE()
        walk_animation_left()
        max_height_check()
        if PELLET == True:
            PELLET_MOVE()
        if JUMP == True:
            FALL = False
            UP_MOVE()
            if PELLET == True:
                PELLET_MOVE()
        if FALL == True:
            DOWN_MOVE()
            if PELLET == True:
                PELLET_MOVE()
            break


    while RIGHT == True:
        RIGHT_MOVE()
        walk_animation_right()
        max_height_check()
        if PELLET == True:
            PELLET_MOVE()
        if JUMP == True:
            FALL = False
            UP_MOVE()
            if PELLET == True:
                PELLET_MOVE()
        if FALL == True:
            DOWN_MOVE()
            if PELLET == True:
                PELLET_MOVE()
            break



    while FALL == True:
        JUMP == False
        DOWN_MOVE()
        if char.ycor() < 0:
            FALL = False
            uncrouch_check()
            char.sety(0)
            if PELLET == True:
                PELLET_MOVE()
            break
        if LEFT == True:
            position = 10
            positions()
            LEFT_MOVE()
            if PELLET == True:
                PELLET_MOVE()
        if RIGHT == True:
            position = 8
            positions()
            RIGHT_MOVE()
            if PELLET == True:
                PELLET_MOVE()
        if PELLET == True:
            PELLET_MOVE()

    while CROUCH == True:
        JUMP = False
        LEFT = False
        RIGHT = False
        crouch_check()
        if PELLET == True:
            PELLET_MOVE()
        if char.ycor() >= 0:
            DOWN_MOVE()
            if PELLET == True:
                PELLET_MOVE()
        if LEFT == True:
            LEFT_MOVE()
            PELLET_MOVE()
        if RIGHT == True:
            RIGHT_MOVE()
            if PELLET == True:
                PELLET_MOVE()

wn.mainloop()
