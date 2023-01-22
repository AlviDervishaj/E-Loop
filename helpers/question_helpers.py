from random import randrange
from colors import WHITE
from pygame import Surface, sprite, time, event, font, mouse
from constants import SCREEN_WIDTH, SURFACE, SCREEN_HEIGHT, NEW_QUESTION, ADDHEALTH
from .images_helpers import load_image, scale_image

# load question image and scale it
question_drop_surface: Surface = load_image("Questions", "Question_Drop.png")
QUESTION_DROP: Surface = scale_image(
    question_drop_surface, (question_drop_surface.get_width()*3, question_drop_surface.get_height()*3))

# load and scale all parts of the question pop-up
popup_surface: Surface = load_image("Questions", "Question_Popup.png")
question_surface: Surface = load_image("Questions", "Question.png")
button_surface: Surface = load_image("Questions", "Button.png")
buttondead_surface: Surface = load_image("Questions", "Button_Dead.png")

POPUP: Surface = scale_image(
    popup_surface, (popup_surface.get_width()*5, popup_surface.get_height()*4))
QUESTION: Surface = scale_image(
    question_surface, (question_surface.get_width()*4.5, question_surface.get_height()*4.5))
BUTTON: Surface = scale_image(
    button_surface, (button_surface.get_width()*4.5, button_surface.get_height()*4.5))
BUTTONDEAD: Surface = scale_image(
    buttondead_surface, (buttondead_surface.get_width()*4.5, buttondead_surface.get_height()*4.5))

# Spawn_time variable
Spawn_time = 0


# Define collision detection, later will detect collision with barriers as well
def question_collision_detect(question, character) -> None:
    if sprite.groupcollide(question, character, True, False):
        print("A new question appears")
        event.post(event.Event(NEW_QUESTION))


# Define Question_Drop class
class Question_Drop(sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = QUESTION_DROP
        self.rect = self.image.get_rect()
        self.rect.center = (randrange(40, SCREEN_WIDTH-39, 80), -200)
        self.velocity = 5

    def update(self, floor) -> None:
        self.rect.y += self.velocity
        self.collision(floor)
        # Hitbox Purposes only
        #draw.rect(SURFACE, (255, 0, 0), self.rect, 2)
    def collision(self, floor) -> None:
        if sprite.spritecollide(self,floor, False):
            self.velocity = 0


# Create function to generate question
def question_spawn() -> Question_Drop:
    return Question_Drop()


# Create function to generate question after set amount of seconds
def handle_question_spawn(group: sprite.Group, time_paused) -> None:
    global Spawn_time
    question_timer = time.get_ticks() - time_paused
    question_timer -= Spawn_time
    if len(group) < 1 and question_timer/1000 >200:

        Spawn_time = time.get_ticks()
        new_question = question_spawn()
        group.add(new_question)


# Create Pop-Up class
class Pop_Up(sprite.Sprite):
    def __init__(self, q1: str, b1: str, b2: str, b3: str, b4: str) -> None:
        super().__init__()
        self.image = POPUP
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.question = Question(q1)
        self.button1 = Button(
            b1, self.rect.topleft[0] + 54, self.rect.topleft[1] + 180, False)
        self.button2 = Button(
            b2, self.rect.topleft[0] + 302, self.rect.topleft[1] + 180, False)
        self.button3 = Button(
            b3, self.rect.topleft[0] + 54, self.rect.topleft[1] + 300, False)
        self.button4 = Button(
            b4, self.rect.topleft[0] + 302, self.rect.topleft[1] + 300, True)

    def update(self, clicked: bool) -> None:
        self.question.draw()
        self.button1.draw()
        self.button2.draw()
        self.button3.draw()
        self.button4.draw()
        self.button1.update(clicked)
        self.button2.update(clicked)
        self.button3.update(clicked)
        self.button4.update(clicked)
        if self.button1.dead == True or self.button2.dead == True or self.button3.dead == True or self.button4.dead == True:
            event.post(event.Event(NEW_QUESTION))
            self.kill()

# Create Question class
class Question(sprite.Sprite):
    def __init__(self, question_text: str) -> None:
        super().__init__()
        self.image = QUESTION
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2-110)
        self.font = font.Font('upheavtt.ttf', 20)
        self.text = self.font.render(question_text, True, WHITE)
        self.textrect = self.text.get_rect()
        self.textrect.center = self.rect.center

    def draw(self) -> None:
        SURFACE.blit(self.image, self.rect)
        SURFACE.blit(self.text, self.textrect)
    def update(self, isclicked) -> None:
        SURFACE.blit(self.image, self.rect)
        SURFACE.blit(self.text, self.textrect)

# Create Button class
class Button(sprite.Sprite):
    def __init__(self, question_text: str, posx: int, posy: int, correct: bool) -> None:
        super().__init__()
        self.image = BUTTON
        self.rect = self.image.get_rect()
        self.rect.topleft = (posx, posy)
        self.font = font.Font('upheavtt.ttf', 20)
        self.text = self.font.render(question_text, True, WHITE)
        self.textrect = self.text.get_rect()
        self.textrect.center = self.rect.center
        self.correct = correct
        self.dead = False
    def draw(self) -> None:
        SURFACE.blit(self.image, self.rect)
        SURFACE.blit(self.text, self.textrect)
    def update(self,clicked: bool) -> None:
        if clicked:
            if self.rect.collidepoint(mouse.get_pos()[0],mouse.get_pos()[1]):
                if not self.correct:
                    self.image = BUTTONDEAD
                else:
                    event.post(event.Event(ADDHEALTH))
                    self.dead = True
    
