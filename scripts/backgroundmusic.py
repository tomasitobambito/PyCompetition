import pygame as pg

class my_background_music():
    def __init__(self, snd) -> None:
        pg.mixer.init()
        self.music = pg.mixer.music.load(snd)