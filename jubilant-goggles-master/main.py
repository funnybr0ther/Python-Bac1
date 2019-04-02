#23-24 Mars 2019  Game Jam 2.0

import pygame as pg
import classes
import ressources
import functions as f
import time
import math
import random
#19h36 : Si Antoine & Thibaud ont un jour un enfant, il s'appelera Donatole
pg.init()

ressources.musiqueS.play(loops = -1)
w = 800
h = 600
win = pg.display.set_mode((w,h))
pg.display.set_caption("La vague 126 vas vous surprendre !!! Je n'y aurai jamais cru")
pg.display.set_icon(ressources.iconeI.convert_alpha())
clock = pg.time.Clock()
gameManager = classes.GameManager()
bckgrd = ressources.bckgI.convert()

run = True
gameRunning = True
while run:
    #Initialisation du jeu
    gameOverRun = True

    player = classes.Player(w/2,h/2, w, h)
    enemies = []
    blyat = []
    cooldown = 0
    omg = classes.OMG()
    circle = classes.Circle()
    scared = classes.ScaredSmiley()

    #Affiche le background
    win.blit(bckgrd, (0,0))
    pg.display.flip()

    #vagues
    wave = 0
    waveFinished = False

    #enemis a faire spawn
    counter_spawn = 0
    num_enemy = 0

    #liste des cible affecter part les sort
    target_circle = []
    target_scared = []

    isWaveBoss = False

    #Debut du jeu
    while gameRunning:

        #La queues des events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                gameRunning = False
                gameOverRun = False

            #Keys pour lancer les sorts
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1 and omg.wait == 0:
                    omg.omgTime = 100
                    omg.wait = omg.cooldown
                if event.key == pg.K_2 and circle.wait == 0:
                    circle.csize = 1
                    target_circle = list(enemies)
                    circle.wait = circle.cooldown
                if event.key == pg.K_3 and scared.wait == 0:
                    scared.scaredTime = 300
                    target_scared = list(enemies)
                    scared.wait = scared.cooldown

        #Tir du joueur
        if pg.mouse.get_pressed()[0] and cooldown <= 0:
            blyat.append(player.shoot())
            cooldown = 1/player.fireRate

        #Controlle des vagues

        #Vague fini
        if waveFinished:
            ressources.waveClearE.play()
            gameManager.waveClear = True
            gameManager.counter_wc = 0
            wave += 1
            if wave == 26:
                wave = 27
            if wave == 1001:
                wave = 26
            waveFinished = False
            if wave % 10 == 0: isWaveBoss = True

        #Vague en cour
        else:
            #Test si il y a encore des enemis en vie ou a cree
            if num_enemy <= 0 and len(enemies) == 0:
                #Vague de boss
                if isWaveBoss:
                    print(wave, num_enemy)
                    f.generateBoss(wave,w,h,player,win,enemies, gameManager)
                    isWaveBoss = False
                else:
                    #print(num_enemy, enemies)
                    waveFinished = True
                    counter_spawn = 0
                    num_enemy = 2*round(math.sqrt(wave))
                    f.generateEnemy(w,h,enemies,player, 0)

            #regarde si il doit cree des enemis
            if num_enemy > 0 and counter_spawn % 20 == 0:
                print(num_enemy)
                f.generateEnemy(w,h,enemies,player, random.randint(0,1))
                num_enemy -= 1

        counter_spawn += 1
        if cooldown >= 0: cooldown -= 1

        #recolte les instance de bullet chez les enemis
        enemies_blyat = []
        for e in enemies:
            try:
                enemies_blyat.extend(e.bullets)
            except:
                pass

        #dessine le background
        win.blit(bckgrd, (0,0))

        #verifie les collisions
        f.testColide(player, enemies, blyat, enemies_blyat, win)

        #test si le player est en vie
        if player.dead():
            gameRunning = False


        to_remove = []

        #Updates et draw toute les objets
        for gameObjects in ([player],enemies,blyat):
            for go in gameObjects:
                go.update()
                go.draw(win)
                if not go.exist:
                    to_remove.append(go)

        #Supprime les refferences des objet mort
        for go in to_remove:
            for gameObjects in (enemies,blyat):
                try:
                    gameObjects.remove(go)
                except:
                    try:
                        target_scared.remove(go)
                    except:
                        try:
                            target_circle.remove(go)
                        except:
                            pass


        #fait les sort
        omg.effet(player, win)
        circle.effet(target_circle, win,w,h)
        scared.effet(target_scared, win)

        #Les affichages des textes

        #Annonce des vagues de boss
        if gameManager.isWarning:
            gameManager.counter_w += 1
            f.texts(f"Vague {wave} : SA TOURNE MAL",0,0,win,h//20,w,h, milieu = True)
            if gameManager.counter_w >= 30:
                gameManager.isWarning = False

        #Annonce des vagues
        elif gameManager.waveClear:
            gameManager.counter_wc += 1
            f.texts(f"Vague {wave}",h*1//3,h*2//3,win,h//20,w,h,milieu = True)
            if gameManager.counter_wc >= 20:
                gameManager.waveClear = False

        #GUI
        f.texts(f"Vies: {player.hp}",w-100,10,win,30)
        f.texts(f"Vague {wave}",10,10,win,50)
        if omg.wait != 0:
            f.texts('1 - OMG: '+str(omg.wait//30),10,h-30,win,20)
        else:
            f.texts('1 - OMG OK',10,h-30,win,20)
        if circle.wait != 0:
            f.texts(f'2 - Red Circle: {circle.wait//30}',(w//2)-100,h-30,win,20)
        else:
            f.texts('2 - Red Circle OK',(w//2)-100,h-30,win,20)
        if scared.wait != 0:
            f.texts(f'3 - Scared Smiley: {scared.wait//30}',w-200,h-30,win,20)
        else:
            f.texts('3 - Scared Smiley OK',w-200,h-30,win,20)
        clock.tick(30)

        #Met a jour l'ecran
        pg.display.flip()


    #GameOver
    while gameOverRun:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                gameOverRun = False
            if event.type == pg.KEYDOWN:
                gameOverRun = False

        f.texts("GAME OVER", (w//2)-100, (h//2)-20, win, 50)
        f.texts("press ANY key to restart", (w//2) - 60, (h//2)+30, win, 20)
        pg.display.flip()

    gameRunning = True

pg.quit()
