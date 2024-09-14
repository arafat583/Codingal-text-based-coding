import random
import pygame

class button():
    def __init__(self, x, y, pos, width, height):
     self.x = x
     self.y = y
     self.width = width
     self.height = height
     self.pos = pos

    def clicked(self, pos):
       self.pos = pygame.mouse.get_pos()
       if self.pos[0] > self.x and self.pos[0] < self.x + self.width:
          if self.pos[1] > self.y and self.pos[1] < self.y + self.height:
                 return True
         return False   
    
class RpsGame():
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((960, 640))
        pygame.display.set_caption("RPS Smasher")

        self.bg = pygame.image.load("r_button.png").convert_alpha()
        self.r_btn = pygame.image.load("p_button.png").convert_alpha()
        self.s_btn = pygame.image.load("s_button.png").convert_alpha()

        self.rock_btn = Button(30. 520, (30. 520), 300, 140)
        self.paper_btn = Button(240, 520, (340, 520),  300, 140)
        self.scissors_btn = Button(640, 520, (640, 520), 300, 140)

        self.font = pygame.font.Font(('Splatxh.ttf'), 90)
        self.text = self.font.render(f"", True, (2255, 255, 255))

        self.pl_score = 0
        self.pl_score = 0


def player(self):
    if self.rock_btn.clicked(30):
        self.p_postion = "rock"
        self.screen.blit(self.choose_rock, (120, 200))
    elif self.paper_btn.clicked(340):
        self.p_option = "paper"
    else:
        self.scissors_btn.clicked(640) 
        self.p_option = "scissors"
        self.screen.blit(self.choose_scissors, (120, 200))
    return self.p_option

def computer(self):
    self.pc_random_choice = ""
    option = ["rock", "paper", "scissors"] 
    pc_choice = random_choice(list(option))
    if pc_choice == "rock":
       self.pc_randome_choice = "rock"
       pc_choice = self.choose_rock
    elif pc_choice == "paper":
        self.pc_random_choice = "paper" 
        pc_choice = self.choose_paper 
    else:
        self.pc_random_choice = "scissors"
        pc_choice = self.choose_scissors    

def pl_score_cache(self):
    self.pl_score = 0
    self.pc_score = 0

    pl = self.p_option
    pc = self.pc_option        
