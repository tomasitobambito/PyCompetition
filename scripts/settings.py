import pygame as pg
from pygame.math import Vector2

GAME_NAME = "Exam Season Nightmares"

# screen
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Camera
LAYERS = {
	'background': 0,
	'tile': 1,
	'main': 2,
	'player': 3,
	'enemy': 4
}

# Map creationg
TILESIZE = 160

FIRSTTILEX = TILESIZE * 4
FIRSTTILEY = TILESIZE * 3

TILESET = [
	["c", "wt", "wt", "wt", "wt", "wt", "wt", "wt", "wt", "c"],
	["wl", "f", "f", "f", "f", "f", "f", "f", "f", "wr"],
	["wl", "f", "t", "f", "f", "f", "f", "t", "f", "wr"],
	["wl", "f", "f", "f", "f", "f", "f", "f", "f", "wr"],
	["wl", "f", "f", "f", "f", "f", "f", "f", "f", "wr"],
	["wl", "f", "f", "f", "d", "f", "f", "f", "f", "wr"],
	["wl", "f", "f", "f", "f", "f", "f", "f", "f", "wr"],
	["wl", "f", "t", "f", "f", "f", "f", "t", "f", "wr"],
	["wl", "f", "f", "f", "f", "f", "f", "f", "f", "wr"],
	["c", "wb", "wb", "wb", "wb", "wb", "wb", "wb", "wb", "c"]
]

COLLISION = [[tile != 'f' for tile in row] for row in TILESET]

# Player
PLAYERSPAWN = (TILESIZE * 8.5, TILESIZE * 7.5)

# Enemy
ENEMYSPAWNS = [
	(TILESIZE * 5.5, TILESIZE * 4.5), 
	(TILESIZE * 12.5, TILESIZE * 4.5), 
	(TILESIZE * 5.5, TILESIZE * 11.5), 
	(TILESIZE * 12.5, TILESIZE * 11.5)
]

FONT = '../data/m5x7.ttf'
