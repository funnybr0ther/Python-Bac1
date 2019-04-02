import pygame.image as img
import pygame.mixer as mix
import pygame.display as disp
import pygame as pg
import os
mix.init()
disp.init()

#musics
def getSound(name):
#Takes the corresponding music in the ressources folder
    return mix.music.load(os.path.join("/home/guillaume/Documents/python/jubilant-goggles-master/Ressources",f'{name}.mp3'))

def getEffect(name):
#Takes the corresponding SFX in the ressource folder
    return mix.Sound(os.path.join("/home/guillaume/Documents/python/jubilant-goggles-master/Ressources",f'{name}.wav'))

#images
def getImg(name):
#Takes the corresponding picture in the ressources folder
    return img.load(os.path.join("/home/guillaume/Documents/python/jubilant-goggles-master/Ressources",f"{name}.png"))
scale = pg.transform.scale

pouceI = scale(getImg('pouce-bleu'),(40,40))
enemyI = scale(getImg('enemy'),(60,60))
enemyShooterI = scale(getImg('enemyShooter'),(60,60))
playerI = getImg('player')
r_arrowI = scale(getImg('r_arrow'),(40,40))
r_circleI = getImg('r_cercle')
scared_smileyI = scale(getImg('smiley'), (40,40))
bossI = pg.transform.scale(getImg('boss'),(160,160))
iconeI = getImg("icone")
bckgI = scale(getImg("bckg"),(800,600))

shootE = getEffect("shoot")
enemyDieE = getEffect("enemy_death")
hitEnemyE = getEffect("hitEnemy")
hitPlayerE = getEffect("hitPlayer")
spawnBossE = getEffect("spawnBoss")
waveClearE = getEffect("waveClear")

shootE.set_volume(0.15)
enemyDieE.set_volume(0.1)
hitEnemyE.set_volume(0.15)
hitPlayerE.set_volume(0.3)
spawnBossE.set_volume(0.7)
waveClearE.set_volume(0.5)


getSound('musique')
musiqueS = mix.music
