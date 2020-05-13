import pygame


screen = None

def Window(w = 500, h = 500):
    global screen
    pygame.init()
    screen = pygame.display.set_mode((w,h))
    return screen

class Button:
    def __init__(self,x,y,w= 0,h=0,text="",background = (255,255,255),font = "Calibri", font_size = 30, text_colour = (0,0,0), outline = False, outline_amount = 2, half_outline = False, offset = [0,0],action = None, action_arg = None, surface = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.surface = surface
        if self.surface == None:
            self.surface = screen
        self.text = text
        self.text_colour = text_colour
        self.background = background
        self.font = pygame.font.Font(pygame.font.match_font(font),font_size)
        self.outline = outline
        self.outline_amount = outline_amount
        self.half_outline = half_outline
        self.offset = offset
        self.action = action
        self.action_arg = action_arg
        self.hover = False
        if self.w == 0 or self.h == 0:
            if self.text != "":
                self.caclulate_size()
            else:
                raise ValueError("cannot calculate width and height without text")
    
    def caclulate_size(self):
        txt = self.font.render(self.text,False,(0,0,0))
        self.w = txt.get_width() + self.offset[0] if self.w == 0 else self.w
        self.h = txt.get_height() + self.offset[1] if self.h == 0 else self.h
    
    def update(self, mouse_pos, click):
        self.hover = False
        if mouse_pos[0] > self.x and mouse_pos[0] < self.x+self.w:
            if mouse_pos[1] > self.y and mouse_pos[1] < self.y+self.h:
                self.hover = True
                if click:
                    if self.action:
                        if self.action_arg:
                            self.action(self.action_arg)
                        else:
                            self.action()
        self.draw()
    
    def draw(self):
        if (self.outline or self.half_outline) and self.hover:
            pygame.draw.rect(self.surface,(0,0,0),(self.x - self.offset[0],self.y - self.offset[1],self.w + self.offset[1],self.h + self.offset[1]))
        if self.outline:
            pygame.draw.rect(self.surface,self.background,(self.x+self.outline_amount,self.y+self.outline_amount,self.w-self.outline_amount * 2,self.h-self.outline_amount*2))
        elif self.half_outline:
            pygame.draw.rect(self.surface,self.background,(self.x+self.outline_amount,self.y+self.outline_amount,self.w-self.outline_amount,self.h-outline_amount))
        else:
            pygame.draw.rect(self.surface,self.background,(self.x,self.y,self.w,self.h))
        
        txt = self.font.render(self.text,False,self.text_colour,self.background)
        self.surface.blit(txt,(self.x + (self.w - txt.get_width())//2, self.y + (self.h - txt.get_height())//2))



class TextBox:
    
    def __init__(self,x = 0, y = 0, w = 0, h = 0, text = "", background = False, font_size = 30, font = "Calibri", text_colour = (0,0,0)):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text_colour = text_colour
        self.text = text
        self.background = background
        self.font = pygame.font.Font(pygame.font.match_font(font),font_size)
    
    def Add_char(self,key):
        if key == 8:
            self.text = self.text[:-1]
        else:
            char = pygame.key.name(key)
            self.text += char
    
    def Get_obj(self):
        if self.background:
            pygame.draw.rect(screen, self.background, (x,y,w,h))
        obj = self.font.render(self.text,True,self.text_colour)
        return obj
    
    def Get_pos(self):
        return (self.x,self.y)

