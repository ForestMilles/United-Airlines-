import pygame
from pygame.locals import *

bright_black = (255,50,0)
bright_grey = (0,25,0)

display_width = 960
display_height = 768

Display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Checkin Here')

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(display, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    display.blit(textSurf, textRect)


def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def screenintro():
    pygame.init()
    display = pygame.display.set_mode((display_width, display_height))
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:

                button("Begin Checkin", 150, 450, 100, 50, grey,  bright_grey, button())
                button("Cancelt", 550, 450, 100, 50, black, bright_black, button())

if __name__ == '__main__':

    screenintro()

pygame.quit()
quit()



def security():
    age = input("Please enter your age.")
    if age == "<15":
        print("Please get a guardian")
        info()
    elif age == "15>=":
        print("Please enter your full name")
    else:
        print("Please enter your age")
        
def identification():
    choice = input("Please scan your passport by pressing the scan passport button and wait until the blue light turns on. If you want to go back to the info menu please press back.")
    if choice == "scan passport":
        security()
    elif choice == "go back":
        info()

def identification2():
    choice = input("Please enter you confirmation code on the keypad below or enter you first and last name" )
    if choice == "keypad":
        flight()
    elif choice == "name":
        name()

def flight():
    choice = input("you are taking flight 971 to Rekjavik, correct?")
    if choice == "yes":
        boardingpass()
    elif choice == "no":
        identification2()

def info():
    print("Good morning! Please enter your information or scan your passport. Thank you.")
    choice = input("you can enter your identification through passport or your confirmation code. Please select one option.")
    if choice == "passport": 
        identification()
    elif choice == "confirmation code":
        identification2()
    else:
        print("you can enter your identification through passport or your confirmation code. Please select one option.")
        info()
            
def security():
    age = input("Please enter your age.")
    if age == "<15":
        print("Please get a guardian")
        info()
    elif age == "15>-":
        print("Please enter your full name")
    else:
        print("Please enter your age")
               
info()