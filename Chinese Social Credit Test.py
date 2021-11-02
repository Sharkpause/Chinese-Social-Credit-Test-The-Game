import pygame

pygame.init()
pygame.mixer.init()

width = 800
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Chinese Social Credit Test")
pygame.display.set_icon(pygame.image.load("china_flag.jpg"))

correct1 = pygame.image.load("15_Social_Credits.jpg")
correct1 = pygame.transform.scale(correct1, (width, height))

china_flag = pygame.image.load("china_flag.jpg")
china_flag = pygame.transform.scale(china_flag, (width, height))

wrong = pygame.image.load("3000000_Social_Credits.jpg")
wrong = pygame.transform.scale(wrong, (width, height))

execution = pygame.image.load("exec_date.jpg")
execution = pygame.transform.scale(execution, (width, height))

white = (255, 255, 255)
black = (0, 0, 0)

background_music = pygame.mixer.Sound("Dehao Zhang - Ching Chang Hon Chi (128 kbps).mp3")
background_stop = False
wrong_sound = pygame.mixer.Sound("Vine Boom Sound Effect Bass Boosted (128 kbps).mp3")
right_sound = pygame.mixer.Sound("Correct Sound Effect Bgm & Sound Effect (128 kbps).mp3")


class Button:
    def __init__(self, text: str, pos: tuple = (0, 0)):
        self.font = pygame.font.SysFont("Comic Sans MS", 50)
        self.text = self.font.render(text, True, white)
        self.rect = self.text.get_rect(topleft=pos)


class Player:
    def __init__(self):
        self.current = [0]
        self.running = [True]
        self.correct = [None]
        self.click_time = [0]
        self.passed_time = [0]


def menu(player: Player, clicked: bool):
    font = pygame.font.SysFont("Comic Sans MS", 50)

    title = font.render("Chinese Social Credit Test", True, white)
    play_but = Button("Play", (120, 300))
    quit_but = Button("Quit", (580, 300))

    window.blit(china_flag, (0, 0))
    window.blit(title, (80, 120))
    window.blit(play_but.text, (100, 300))
    window.blit(quit_but.text, (570, 300))

    if clicked:
        if play_but.rect.collidepoint(pygame.mouse.get_pos()):
            player.current[0] += 1
            p.correct[0] = True
        if quit_but.rect.collidepoint(pygame.mouse.get_pos()):
            player.running[0] = False
            p.correct[0] = False


def current_level(player: Player, clicked: bool):
    font = pygame.font.SysFont("Comic Sans MS", 50)

    if player.current[0] == 1:
        question = font.render("What is the best country?", True, white)
        a = Button("A. China", (100, 250))
        b = Button("B. idk", (100, 350))
        c = Button("C. Taiwan", (480, 250))
        d = Button("D. It is A", (480, 350))

        window.blit(china_flag, (0, 0))
        window.blit(question, (110, 80))

        window.blit(a.text, (100, 250))
        window.blit(b.text, (100, 350))
        window.blit(c.text, (480, 250))
        window.blit(d.text, (480, 350))

        if clicked:
            if a.rect.collidepoint(pygame.mouse.get_pos()):
                right_sound.play()
                player.click_time[0] = pygame.time.get_ticks()
                player.current[0] += 1
                player.correct[0] = True
            elif b.rect.collidepoint(pygame.mouse.get_pos()) or c.rect.collidepoint(pygame.mouse.get_pos()) or d.rect.collidepoint(pygame.mouse.get_pos()):
                wrong_sound.play()
                player.click_time[0] = pygame.time.get_ticks()
                player.current[0] += 1
                player.correct[0] = False
    elif player.current[0] == 2:
        question = font.render("Is Taiwan a country?", True, white)
        a = Button("A. Yes", (100, 300))
        b = Button("B. No", (400, 300))

        window.blit(china_flag, (0, 0))
        window.blit(question, (160, 80))
        window.blit(a.text, (160, 300))
        window.blit(b.text, (460, 300))

        if clicked:
            if b.rect.collidepoint(pygame.mouse.get_pos()):
                right_sound.play()
                player.click_time[0] = pygame.time.get_ticks()
                player.current[0] += 1
                player.correct[0] = True
            elif a.rect.collidepoint(pygame.mouse.get_pos()):
                wrong_sound.play()
                player.click_time[0] = pygame.time.get_ticks()
                player.correct[0] = False
    elif player.current[0] == 3:
        question = font.render("How many children do you have?", True, white)
        a = Button("A. -1", (100, 250))
        b = Button("B. 0", (100, 350))
        c = Button("C. 1", (580, 250))
        d = Button("D. 2", (580, 350))

        window.blit(china_flag, (0, 0))
        window.blit(question, (30, 80))
        window.blit(a.text, (100, 250))
        window.blit(b.text, (100, 350))
        window.blit(c.text, (580, 250))
        window.blit(d.text, (580, 350))

        if clicked:
            if c.rect.collidepoint(pygame.mouse.get_pos()):
                right_sound.play()
                player.current[0] += 1
                player.correct[0] = True
                player.click_time[0] = pygame.time.get_ticks()
            elif b.rect.collidepoint(pygame.mouse.get_pos()) or a.rect.collidepoint(pygame.mouse.get_pos()) or d.rect.collidepoint(pygame.mouse.get_pos()):
                wrong_sound.play()
                player.correct[0] = False
                player.click_time[0] = pygame.time.get_ticks()
    elif player.current[0] == 4:
        question = font.render("Do you consent to your village", True, white)
        question1 = font.render("being used as a nuclear", True, white)
        question2 = font.render("testing site?", True, white)
        a = Button("A. Yes", (100, 300))
        b = Button("B. No", (550, 300))

        window.blit(china_flag, (0, 0))
        window.blit(question, (50, 80))
        window.blit(question1, (130, 140))
        window.blit(question2, (220, 200))
        window.blit(a.text, (100, 300))
        window.blit(b.text, (550, 300))

        if clicked:
            if a.rect.collidepoint(pygame.mouse.get_pos()):
                right_sound.play()
                player.current[0] += 1
                player.correct[0] = True
                player.click_time[0] = pygame.time.get_ticks()
            elif b.rect.collidepoint(pygame.mouse.get_pos()):
                wrong_sound.play()
                player.current[0] += 1
                player.correct[0] = False
                player.click_time[0] = pygame.time.get_ticks()

    elif player.current[0] == 5:
        message = font.render("Congratulations!", True, white)
        message1 = font.render("You Passed the Test!", True, white)

        window.blit(china_flag, (0, 0))
        window.blit(message, (200, 200))
        window.blit(message1, (150, 260))


def result(player: Player):
    global background_stop

    if player.correct[0] == None: return
    if not player.correct[0]:
        player.passed_time[0] = pygame.time.get_ticks() - player.click_time[0]

        if not background_stop:
            background_music.stop()
            background_stop = True

        if player.passed_time[0] < 2000:
            window.blit(wrong, (0, 0))
        else:
            wrong_sound.stop()
            return True
    elif player.correct[0]:
        player.passed_time[0] = pygame.time.get_ticks() - player.click_time[0]

        if player.passed_time[0] < 2000:
            window.blit(correct1, (0, 0))
        else:
            right_sound.stop()
            return False


clock = pygame.time.Clock()
drawed = False
correct = True
playing = False
p = Player()

# Menu
background_music.play()
while p.running[0] and not playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            p.running[0] = False

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:
            menu(p, True)
            drawed = True


    if not drawed:
        menu(p, False)

    if p.correct[0] == True:
        playing = True

    clock.tick(60)
    drawed = False
    pygame.display.update()


# Main
p.correct[0] = None
while p.running[0] and correct:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            p.running[0] = False

        if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:
            current_level(p, True)
            result(p)
            drawed = True

    if not drawed:
        current_level(p, False)
        if result(p):
            correct = False

    drawed = False
    clock.tick(60)
    pygame.display.update()


# Wrong
p.click_time[0] = pygame.time.get_ticks()
while not correct:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correct = True
            p.running[0] = False

    p.passed_time[0] = pygame.time.get_ticks() - p.click_time[0]

    if p.passed_time[0] < 2000:
        window.blit(execution, (0, 0))
    else:
        correct = True

    pygame.display.update()

background_music.stop()
