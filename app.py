from math import floor
from typing import Tuple
import pygame
import json

pygame.init()

white = (255, 255, 255)
background = (18, 18, 19)
gray = (142, 142, 142)
orange = (233, 198, 1)
green = (87, 172, 87)

size = (800, 600)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

pygame.display.set_caption('Wordle solver')
font = pygame.font.SysFont('arial', 38, True)
font2 = pygame.font.SysFont('arial', 20, True)

class Letter():
    def __init__(self, letter: str, position: int, row: int, type: int):
        self.letter = letter
        self.position = position
        self.row = row
        self.type = type

class SquareLetter():
    def __init__(self, rect: pygame.Rect, surface: pygame.Surface, letter: Letter):
        self.rect = rect
        self.surface = surface
        self.letter = letter

class Element():
    def __init__(self, rect: pygame.Rect, surface: pygame.Surface, text: str, id: int, background: Tuple[int, int]):
        self.rect = rect
        self.surface = surface
        self.text = text
        self.id = id
        self.background = background

letter_objects = []
btn = pygame.Surface((100,40))
btn.fill(background)

output = pygame.Surface((100,40))
output.fill(gray)
default = Element(pygame.Rect(10,10,100,40), btn, "Reset", 0, background)
objects = [ default ]

line = 1

with open("wordle_words.json", "r") as f:
    words = json.load(f)

def checkWord():
    correct = []
    for word in words:
        valid = True
        for value in letter_objects:
            letter = value.letter
            if letter.letter in word and letter.type == 1:
                valid = False
            if letter.type == 2 and word[letter.position] == letter.letter:
                valid = False
            if letter.type == 3 and word[letter.position] != letter.letter:
                valid = False
            if letter.type == 2 and not letter.letter in word:
                valid = False
        if valid:
            correct.append(word)
    objects.clear()
    objects.append(default)
    for word in correct:
        surface = pygame.Surface((100, 30))
        surface.fill(background)

        element = Element(pygame.Rect(size[0]-surface.get_width()-10, (len(objects)-1)*30, 100, 30), surface, word, len(objects), background)
        objects.append(element)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                if floor((len(letter_objects)-1)/5)+1 == line:
                    letter_objects.pop(len(letter_objects)-1)
            elif event.key == pygame.K_RETURN:
                if len(letter_objects)%5 == 0 and line <= 6 and floor(len(letter_objects)/5) == line:
                    for letter in letter_objects[-5:]:
                        letter.letter.type = 1
                    checkWord()
                    line += 1
            elif event.unicode in "abcdefghijklmnopqrstuvwxyz" and event.unicode != "" and line <= 6:
                if floor(len(letter_objects)/5)+1 == line:
                    letter = Letter(event.unicode, len(letter_objects)%5, line, 0)

                    square = pygame.Surface((60,60))
                    spacing = 5
                    rectangle = (square.get_width()+spacing, square.get_height()+spacing)

                    rect = pygame.Rect(size[0]/2-rectangle[0]/2,letter.row*rectangle[1]+rectangle[1]/2,rectangle[0],rectangle[1])
                    rect.x = size[0]/2-rectangle[0]/2+(letter.position*rectangle[0])-rectangle[0]*2
                    
                    letter_objects.append(SquareLetter(rect, square, letter))
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_letters = [s for s in letter_objects if s.rect.collidepoint(pos)]
            if len(clicked_letters) > 0 and clicked_letters[0].letter.type > 0:
                clicked_letters[0].letter.type += 1
                if clicked_letters[0].letter.type > 3:
                    clicked_letters[0].letter.type = 1
                checkWord()
            clicked_buttons = [s for s in objects if s.rect.collidepoint(pos)]
            if len(clicked_buttons) > 0:
                if clicked_buttons[0].id == 0:
                    letter_objects.clear()
                    objects.clear()
                    objects.append(default)
                    line = 1
    
    screen.fill(background)
    for object in objects:
        text = font2.render(object.text.capitalize(), True, white, object.background)
        rect = object.rect

        textRect = text.get_rect()
        textRect.center = (rect.x + rect.width / 2, rect.y + rect.height / 2)

        screen.blit(object.surface, rect)
        screen.blit(text, textRect)
    for object in letter_objects:
        letter = object.letter
        square = pygame.Surface((60,60))
        spacing = 5
        rectangle = (square.get_width()+spacing, square.get_height()+spacing)

        rect = pygame.Rect(size[0]/2-rectangle[0]/2,letter.row*rectangle[1]+rectangle[1]/2,rectangle[0],rectangle[1])
        rect.x = size[0]/2-rectangle[0]/2+(letter.position*rectangle[0])-rectangle[0]*2

        if letter.type == 0:
            text = font.render(letter.letter.capitalize(), True, white, background)
            square.fill(background)
        if letter.type == 1:
            text = font.render(letter.letter.capitalize(), True, white, gray)
            square.fill(gray)
        if letter.type == 2:
            text = font.render(letter.letter.capitalize(), True, white, orange)
            square.fill(orange)
        if letter.type == 3:
            text = font.render(letter.letter.capitalize(), True, white, green)
            square.fill(green)
        
        textRect = text.get_rect()
        textRect.center = (rect.x + rect.width / 2 - spacing / 2, rect.y + rect.height / 2 - spacing / 2)

        screen.blit(square, rect)
        screen.blit(text, textRect)
    pygame.display.update()
    clock.tick(60)
