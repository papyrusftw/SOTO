from pygame import *
import random
import sys
import threading
import time
from WinnerWindow import Window
class Game:
    def __init__(self, NumPlayers, KeyBinds):
        init()
        self.NumPlayers = NumPlayers
        self.KeyBinds = KeyBinds
        self.map = display.set_mode((0, 0), FULLSCREEN)
        self.list_of_objects = []
        display.set_caption("prototype 0.1")
        self.backround = image.load("grass.png")
        self.backround = transform.scale(self.backround, (1920, 1080))
        self.haybale = image.load("haybale.png")
        self.rocks = image.load("rocks.png")
        mixer.init()
        mixer.music.load("game_music0_1.mp3")
        mixer.music.play(loops=-1)
        self.boom = mixer.Sound("boom.mp3")
        self.ActionKeys = {
            "A": K_a, "B": K_b, "C": K_c, "D": K_d, "E": K_e, "F": K_f, "G": K_g, "H": K_h,
            "I": K_i, "J": K_j, "K": K_k, "L": K_l, "M": K_m, "N": K_n, "O": K_o, "P": K_p,
            "Q": K_q, "R": K_r, "S": K_s, "T": K_t, "U": K_u, "V": K_v, "W": K_w, "X": K_x,
            "Y": K_y, "Z": K_z, "SPACE": K_SPACE, "arrowLeft": K_LEFT, "arrowUp": K_UP, "arrowRight": K_RIGHT,
            "arrowDown": K_DOWN
        }

        Models = [
            "t34_up.png", "t34_left.png", "t34_down.png", "t34_right.png",
            "tiger_up.png", "tiger_left.png", "tiger_down.png", "tiger_right.png",
            "sherman_up.png", "sherman_left.png", "sherman_down.png", "sherman_right.png",
            "Tiger_tank.png", "Tiger_tank_left.png", "Tiger_tank_down.png", "Tiger_tank_right.png",
            "Cromwell_down.png", "Cromwell_left.png", "Cromwell_down.png", "Cromwell_right.png",
            "kv2_up.png", "kv2_left.png", "kv2_down.png", "kv2_right.png"
        ]
        ModelsLoaded = []
        for i in range(len(Models)):
            load = image.load(Models[i])
            ModelsLoaded.append(load)
        self.pictures0 = {"1": ModelsLoaded[0], "2": ModelsLoaded[1], "3": ModelsLoaded[2], "4": ModelsLoaded[3]}
        self.pictures1 = {"1": ModelsLoaded[4], "2": ModelsLoaded[5], "3": ModelsLoaded[6], "4": ModelsLoaded[7]}
        self.pictures2 = {"1": ModelsLoaded[8], "2": ModelsLoaded[9], "3": ModelsLoaded[10], "4": ModelsLoaded[11]}
        self.pictures3 = {"1": ModelsLoaded[12], "2": ModelsLoaded[13], "3": ModelsLoaded[14], "4": ModelsLoaded[15]}
        self.pictures4 = {"1": ModelsLoaded[16], "2": ModelsLoaded[17], "3": ModelsLoaded[18], "4": ModelsLoaded[19]}
        self.pictures5 = {"1": ModelsLoaded[20], "2": ModelsLoaded[21], "3": ModelsLoaded[22], "4": ModelsLoaded[23]}

        self.Pictures = [self.pictures0, self.pictures1, self.pictures2, self.pictures3, self.pictures4, self.pictures5]
        self.ObjectSpawnPositions = [(650, 650), (987, 650), (846, 589), (1000, 591), (758, 460), (1153, 595)]
        self.objects = [self.haybale, self.rocks]

        class Objects:
            def __init__(self, screen, objects, position):
                self.screen = screen
                self.image = random.choice(objects)
                self.rect = self.image.get_rect()
                self.rect.topleft = position
            def blit(self):
                self.screen.blit(self.image, self.rect)

        for i in range(6):
            obj = Objects(self.map, self.objects, self.ObjectSpawnPositions[i])
            self.list_of_objects.append(obj)

        class Bullet:
            def __init__(self, screen, ima):
                self.ima = image.load(ima)
                self.rect = self.ima.get_rect()
                self.screen = screen
                self.x = 0
                self.y = 0
                self.GerDirectionx = 0
                self.GerDirectiony = 0
                self.Spawned = False
                self.owner = None

            def Spawn(self, x, y, direction, owner):
                self.Spawned = True
                self.direction = direction
                self.x = x
                self.y = y
                self.owner = owner
                if self.direction == "up":
                    self.GerDirectiony = -5
                    self.GerDirectionx = 0
                elif self.direction == "left":
                    self.GerDirectionx = -5
                    self.GerDirectiony = 0
                elif self.direction == "down":
                    self.GerDirectiony = 5
                    self.GerDirectionx = 0
                elif self.direction == "right":
                    self.GerDirectionx = 5
                    self.GerDirectiony = 0
                self.screen.blit(self.ima, (self.x + self.GerDirectionx, self.y + self.GerDirectionx))

            def MoveBullet(self, objects):
                if self.Spawned == True:
                    self.x += self.GerDirectionx
                    self.y += self.GerDirectiony
                    self.rect.x = self.x
                    self.rect.y = self.y
                    for obj in objects:
                        if self.rect.colliderect(obj.rect):
                            self.Spawned = False
                            return
                    self.screen.blit(self.ima, (self.x, self.y))

        class Tank:
            def __init__(self, screen, x, y, Keys, Letters, Pictures, BulletList, i):
                self.shot = mixer.Sound("fire_sound.mp3")
                self.bullet = i
                self.lives = 5
                self.BulletList = BulletList
                self.Letters = Letters
                self.Pictures = Pictures
                self.i = i
                self.x = x
                self.y = y
                self.Keys = Keys
                self.loaded = True
                self.ima = self.Pictures[i]["1"]
                self.rect = self.ima.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.alive = True
                self.prev_x = x
                self.prev_y = y
                screen.blit(self.ima, (self.x, self.y))
                self.direction = "up"

            def Reload(self):
                self.loaded = False
                time.sleep(2)
                self.loaded = True

            def Draw(self, screen, i, OtherTanks, objects):
                if self.alive == False:
                    return
                self.prev_x, self.prev_y = self.x, self.y
                Keys = key.get_pressed()

                if Keys[self.Letters[self.Keys[0]]]:
                    self.direction = "up"
                    self.y -= 2
                    self.ima = self.Pictures[self.i]["1"]
                elif Keys[self.Letters[self.Keys[1]]]:
                    self.direction = "left"
                    self.x -= 2
                    self.ima = self.Pictures[self.i]["2"]
                elif Keys[self.Letters[self.Keys[2]]]:
                    self.direction = "down"
                    self.y += 2
                    self.ima = self.Pictures[self.i]["3"]
                elif Keys[self.Letters[self.Keys[3]]]:
                    self.direction = "right"
                    self.x += 2
                    self.ima = self.Pictures[self.i]["4"]
                elif Keys[self.Letters[self.Keys[4]]]:
                    if self.loaded and self.alive:
                        self.shot.play()
                        self.BulletList[self.bullet].Spawn(self.x + 40, self.y + 40, self.direction, self.i)
                        threading.Thread(target=self.Reload).start()

                self.rect.x = self.x
                self.rect.y = self.y

                TankCollision = False
                for tank in OtherTanks:
                    if tank.i != self.i and tank.alive and self.rect.colliderect(tank.rect):
                        TankCollision = True

                if TankCollision:
                    self.x, self.y = self.prev_x, self.prev_y
                    self.rect.x, self.rect.y = self.x, self.y

                ObjectCollision = False
                for obj in objects:
                    if self.rect.colliderect(obj.rect):
                        ObjectCollision = True

                if ObjectCollision:
                    self.x, self.y = self.prev_x, self.prev_y
                    self.rect.x, self.rect.y = self.x, self.y

                self.x = max(0, min(self.x, 1920 - self.rect.width))
                self.y = max(0, min(self.y, 1080 - self.rect.height))
                screen.blit(self.ima, (self.x, self.y))

        self.PlayerList = []
        self.BulletList = []
        for i in range(NumPlayers):
            self.bullet = Bullet(self.map, "bullet.png")
            self.BulletList.append(self.bullet)

        SpawnPosition = [(100, 100), (1720, 100), (100, 780), (1720, 780), (340, 440), (1480, 440)]
        for i in range(NumPlayers):
            x, y = SpawnPosition[i]
            self.tank = Tank(self.map, x, y, KeyBinds[i], self.ActionKeys, self.Pictures, self.BulletList, i)
            self.PlayerList.append(self.tank)

    def CollisionCheck(self):
        for bullet in self.BulletList:
            if bullet.Spawned:
                for tank in self.PlayerList:
                    if tank.alive and bullet.owner != tank.i and bullet.rect.colliderect(tank.rect):
                        tank.lives -= 1
                        bullet.Spawned = False
                        if tank.lives <= 0:
                            tank.alive = False
                            self.boom.play()

    def Map(self):
        self.map.blit(self.backround, (0, 0))
        for obj in self.list_of_objects:
            obj.blit()
        self.CollisionCheck()
        for i, tank in enumerate(self.PlayerList):
            OtherTanks = [t for j, t in enumerate(self.PlayerList) if j != i]
            tank.Draw(self.map, i, OtherTanks, self.list_of_objects)
        for bullet in self.BulletList:
            bullet.MoveBullet(self.list_of_objects)
        display.update()

    def GameLoop(self):
        while True:
            for e in event.get():
                if e.type == QUIT:
                    quit()
                    return
                elif e.type == KEYDOWN and e.key == K_ESCAPE:
                    quit()
                    return
            dead = 0
            for number_alive in range(len(self.PlayerList)):
                if self.PlayerList[number_alive].alive != True:
                    dead += 1
            if dead != len(self.PlayerList) - 1:
                self.Map()
            else:
                mixer.music.stop()
                for number_alive in range(len(self.PlayerList)):
                    if self.PlayerList[number_alive].alive == True:
                        number = number_alive
                win = Window(number)
                quit()
                return
