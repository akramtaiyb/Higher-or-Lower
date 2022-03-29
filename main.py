import pygame
import random

suit = ('Spades', 'Hearts', 'Clubs', 'Diamonds')
rank = ('A', '2', '3', '4', '5', '6', '7', '8', '9','10', 'J', 'Q', 'K')

class Card:
    def __init__(self):
        self.suit = random.choice(suit)
        self.rank = random.choice(rank)
        self.value = self.valueChooser()
        self.img =  self.cardPNG()
    
    def valueChooser(self) :
        if self.rank == 'A' :
            return 1
        elif self.rank == '2':
            return 2
        elif self.rank == '3':
            return 3
        elif self.rank == '4':
            return 4
        elif self.rank == '5':
            return 5
        elif self.rank == '6':
            return 6
        elif self.rank == '7':
            return 7
        elif self.rank == '8':
            return 8
        elif self.rank == '9':
            return 9
        elif self.rank == '10':
            return 10
        elif self.rank == 'J':
            return 11
        elif self.rank == 'Q':
            return 12
        elif self.rank == 'K':
            return 13
    
    def cardPNG(self):
        return pygame.image.load(f'boardgamepack/PNG/Cards/card{self.suit}{self.rank}.png')

class Deck:
    def __init__(self):
        self.cardsNbr = 8
        self.cardsOut = 0
    
    def afterCardOut(self):
        self.cardsNbr -= 1
        return self.cardsNbr

class Player:
    def __init__(self):
        self.userName = 'player' + str(random.randint(00000, 99999))
        self.score = 0
        self.choice = 0  

class Game:
    name = 'HIGHER or LOWE'
    creator = 'TAIYB AKRAM'
    creationYear = 2022
    def __init__(self):
        self.playerOne = Player()
        self.playerTwo = Player()    

    def winner(self):
        if self.playerOne.score > self.playerTwo.score:
            return 0
        elif self.playerOne.score < self.playerTwo.score:
            return 1
        else:
            return 2

    def compareCards(self, currentCard, nextCard):
        if nextCard.value > currentCard.value:
            if self.playerOne.choice == 1 and self.playerTwo.choice == 1 :
                self.playerOne.score += 20
                self.playerTwo.score += 20
            elif self.playerOne.choice == 1 and self.playerTwo.choice == 0 :
                self.playerOne.score += 20
                self.playerTwo.score -= 15
            elif self.playerOne.choice == 0 and self.playerTwo.choice == 0 :
                self.playerOne.score -= 15
                self.playerTwo.score -= 15
            elif self.playerOne.choice == 0 and self.playerTwo.choice == 1 :
                self.playerOne.score -= 15
                self.playerTwo.score += 20
        elif nextCard.value < currentCard.value:
            if self.playerOne.choice == 1 and self.playerTwo.choice == 1 :
                self.playerOne.score -= 15
                self.playerTwo.score -= 15
            elif self.playerOne.choice == 1 and self.playerTwo.choice == 0 :
                self.playerOne.score -= 15
                self.playerTwo.score += 20
            elif self.playerOne.choice == 0 and self.playerTwo.choice == 0 :
                self.playerOne.score += 20
                self.playerTwo.score += 20
            elif self.playerOne.choice == 0 and self.playerTwo.choice == 1 :
                self.playerOne.score += 20
                self.playerTwo.score -= 15
        else :
            self.playerOne.score -= 15
            self.playerTwo.score -= 15

    def changeUsername(self, p, n):
        p.userName = n
        

    def start(self):
        pygame.init()
        pygame.mixer.init()
        screen = pygame.display.set_mode((420, 680))
        currentCard = Card()
        nextCard = Card()
        deck = Deck()
        i = 0
        pygame.init()
        
        screen = pygame.display.set_mode((420, 680))

        bg = pygame.image.load('bg.png')

        pygame.display.set_caption("Higher or Lower (by TAIYB AKRAM)")
        textColor = (0, 255, 0)
        mainFont = pygame.font.Font("Fonts/Kenney Future Narrow.ttf",30)
        smallFont = pygame.font.Font("Fonts/Kenney Future Narrow.ttf",25)
        menuItem1 = '>'
        menuItem2 = ' '
        color_menuItem1 = (0, 255, 0)
        color_menuItem2 = (255, 255, 255)
        selected_mode = 1
        menu = False
        continuer = True
        esc = False
        intro = True
        menu_bg = pygame.image.load('menu-bg.png')
        mainLogo = pygame.image.load('main.png')
        text = self.playerOne.userName
        fps = 16
        clock = pygame.time.Clock()

        song = 'to-the-next-round.mp3'
        pygame.mixer.music.load(song)
        pygame.mixer.music.play(-1)

        cardSlide = 'boardgamepack/Bonus/cardSlide3.ogg'
        keyboard = 'select.wav'
        click = 'click.wav'
        switcher = 'select.wav'

        breaker = 'highscore.wav'
        
        i = 0
        while continuer:
            if intro == True:
                screen.blit(menu_bg, (0, 0))
                screen.blit(mainLogo, (0, 0))
                message = mainFont.render('Username:', True, textColor)
                message_rect = message.get_rect(center=(210, 360))
                screen.blit(message, message_rect)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            text = self.playerOne.userName
                            pygame.mixer.Channel(2).play(pygame.mixer.Sound(keyboard))
                        elif event.key == pygame.K_SPACE:
                            text += ' '
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                            pygame.mixer.Channel(2).play(pygame.mixer.Sound(keyboard))
                        elif event.key == pygame.K_RETURN:
                            pygame.mixer.Channel(3).play(pygame.mixer.Sound(click))
                            intro = False
                            menu = True
                        else:
                            text += event.unicode
                            pygame.mixer.Channel(2).play(pygame.mixer.Sound(keyboard))

                userNameDisp = smallFont.render(text, True, textColor)
                userNameDisp_rect = userNameDisp.get_rect(center=(210, 390))
                screen.blit(userNameDisp, (60, 400))
                
                
            
            if intro == False:
                self.playerOne.userName = text
                screen.blit(menu_bg,(0, 0))
                menu = mainFont.render('Playing Mode:', True, (255, 255, 255))
                screen.blit(menu,(40, 240))
                for event in pygame.event.get():
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            quit()
                        if event.type == pygame.KEYDOWN :
                            if event.key == pygame.K_UP:
                                menuItem1 = '>'
                                menuItem2 = ' '
                                color_menuItem1 = (0, 255, 0)
                                color_menuItem2 = (255, 255, 255)
                                selected_mode = 1
                                pygame.mixer.Channel(3).play(pygame.mixer.Sound(switcher))
                            elif event.key == pygame.K_DOWN:
                                menuItem1 = ' '
                                menuItem2 = '>'
                                color_menuItem1 = (255, 255, 255)
                                color_menuItem2 = (0, 255, 0)
                                selected_mode = 2
                                pygame.mixer.Channel(3).play(pygame.mixer.Sound(switcher))
                            elif event.key == pygame.K_RETURN:
                                menu = False
                                pygame.mixer.Channel(2).play(pygame.mixer.Sound(click))
                                if menuItem2 == ' ':
                                    self.playerTwo.userName = 'Robot'
                                elif menuItem2 == '*':
                                    self.foreverMode()
                item1 = mainFont.render(f'{menuItem1} With Robot.', True, color_menuItem1)
                item2 = mainFont.render(f'{menuItem2} Challenging Mode.', True, color_menuItem2)
                screen.blit(item1,(50, 290))
                screen.blit(item2,(50, 330))
                 

                while menu == False: 
                    if selected_mode == 1: 
                        if deck.cardsNbr >= 0:
                            screen.blit(bg, (0, 0))
                            image = pygame.transform.scale(currentCard.img, (140, 190))
                            screen.blit(image, (140, 255))
                            user = smallFont.render(f'{self.playerOne.userName}',True,textColor)
                            score = smallFont.render(f'score : {self.playerOne.score}',True,textColor)
                            screen.blit(user,(22,20))
                            screen.blit(score,(22,50))
                            robot = smallFont.render('Robot',True,(200,100,50))
                            robot_score = smallFont.render(f'score : {self.playerTwo.score}',True,(200,100,50))
                            screen.blit(robot,(240,20))
                            screen.blit(robot_score,(240,50))

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT :
                                    pygame.quit()
                                    quit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_UP and deck.cardsNbr >= 0:
                                        deck.afterCardOut()
                                        self.playerOne.choice = 1
                                        self.playerTwo.userName = 'Robot'
                                        if currentCard.value == 13:
                                            self.playerTwo.choice = 0
                                        elif currentCard.value == 1:
                                            self.playerTwo.choice = 1
                                        else:
                                            self.playerTwo.choice = random.randint(0, 1)
                                        self.compareCards(currentCard, nextCard)
                                        currentCard = nextCard
                                        nextCard = Card()
                                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(cardSlide))
                                    elif event.key == pygame.K_DOWN and deck.cardsNbr >= 0:
                                        deck.afterCardOut()
                                        self.playerOne.choice = 0
                                        self.playerTwo.userName = 'Robot'
                                        if currentCard.value == 13:
                                            self.playerTwo.choice = 0
                                        elif currentCard.value == 1:
                                            self.playerTwo.choice = 1
                                        else:
                                            self.playerTwo.choice = random.randint(0, 1)
                                        self.compareCards(currentCard, nextCard)
                                        currentCard = nextCard
                                        nextCard = Card()
                                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(cardSlide))
                                    elif event.key == pygame.K_ESCAPE:
                                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(click))
                                        self.playerOne.score = 0
                                        self.playerTwo.score = 0
                                        deck.cardsNbr = 8
                                        menu = True

                        if deck.cardsNbr < 0:
                            screen.blit(bg, (0, 0))
                            if self.winner() == 0:
                                winningMsg = smallFont.render(f'The winner is :', True, textColor)
                                winner = mainFont.render(f'{self.playerOne.userName}', True, textColor)
                                finalScore = smallFont.render(f'score: {self.playerOne.score} vs {self.playerTwo.score}', True, textColor)
                            elif self.winner() == 1:
                                winningMsg = smallFont.render(f'The winner is :', True, textColor)
                                winner = mainFont.render(f'{self.playerTwo.userName}', True, textColor)
                                finalScore = smallFont.render(f'score: {self.playerOne.score} vs {self.playerTwo.score}', True, textColor)
                            else:
                                winningMsg = smallFont.render('DRAW', True, textColor)
                                winner = mainFont.render('No winner!', True, textColor)
                                finalScore = smallFont.render(f'score: {self.playerOne.score} vs {self.playerTwo.score}', True, textColor)
                            winningMsg_rect = winningMsg.get_rect(center=(210, 280))
                            winner_rect = winner.get_rect(center=(210, 340))
                            finalScore_rect = finalScore.get_rect(center=(210, 380))
                            screen.blit(winningMsg, winningMsg_rect)
                            screen.blit(winner, winner_rect)
                            screen.blit(finalScore, finalScore_rect)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT :
                                    pygame.quit()
                                    quit()
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_RETURN:
                                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(click))
                                        self.playerOne.score = 0
                                        self.playerTwo.score = 0
                                        deck.cardsNbr = 8
                                    elif event.key == pygame.K_ESCAPE:
                                        pygame.mixer.Channel(2).play(pygame.mixer.Sound(click))
                                        self.playerOne.score = 0
                                        self.playerTwo.score = 0
                                        deck.cardsNbr = 8
                                        menu = True
                                    elif event.key == pygame.K_q:
                                        self.playerOne.score = 0
                                        self.playerTwo.score = 0
                                        deck.cardsNbr = 8
                                        pygame.quit()
                                        quit()
                    
                    elif selected_mode == 2:
                        if esc == False:
                            screen.blit(bg, (0, 0))
                            image = pygame.transform.scale(currentCard.img, (140, 190))
                            screen.blit(image, (140, 255))
                            user = mainFont.render(f'{self.playerOne.userName}',True,textColor)
                            score = mainFont.render(f'score : {self.playerOne.score}',True,textColor)
                            screen.blit(user,(22,20))
                            screen.blit(score,(22,50))
                            with open('highscores.txt', 'r') as data:
                                line = data.readlines()
                                highscore = int(line[0])
                            highscoreDisp = smallFont.render(f' Highscore : {highscore}', True, textColor)
                            highscoreDisp_rect = highscoreDisp.get_rect(center=(210, 640))
                            screen.blit(highscoreDisp, highscoreDisp_rect)
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT :
                                    pygame.quit()
                                    quit()
                                elif event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_UP and esc == False:
                                        self.playerOne.choice = 1
                                        self.compareCards(currentCard, nextCard)
                                        currentCard = nextCard
                                        nextCard = Card()
                                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(cardSlide))
                                    elif event.key == pygame.K_DOWN and esc == False:
                                        self.playerOne.choice = 0
                                        self.compareCards(currentCard, nextCard)
                                        currentCard = nextCard
                                        nextCard = Card()
                                        pygame.mixer.Channel(1).play(pygame.mixer.Sound(cardSlide))
                                    elif event.key == pygame.K_ESCAPE:
                                        esc = True
                                        screen.blit(bg, (0, 0))
                                        score = mainFont.render(f'Your score is: {self.playerOne.score}', True, textColor)
                                        screen.blit(score, (60, 300))
                                    with open('highscores.txt', 'r') as data:
                                        line = data.readlines()
                                        highscore = int(line[0])
                                        if self.playerOne.score >= highscore:
                                            pygame.mixer.Channel(1).play(pygame.mixer.Sound(breaker))
                                            newHighScore = True
                                        else:
                                            newHighScore = False
                                    if newHighScore == True:
                                        with open('highscores.txt', 'w') as data:
                                            data.write(f'{self.playerOne.score}')
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            quit()
                        if event.type == pygame.KEYDOWN:
                            self.playerOne.score = 0
                            if event.key == pygame.K_RETURN:
                                esc = False
                            if event.key == pygame.K_ESCAPE:
                                menu = True
                                esc = False
                    pygame.display.update()
                    clock.tick(fps) 
            pygame.display.update()
            clock.tick(fps) 
                         
game = Game()
game.start()