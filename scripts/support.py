from os import walk
import pygame as pg

def import_folder(path):
    surfList = []
    for _, __, imgFiles in walk(path):
        for img in imgFiles:
            fullPath = f'{path}/{img}'
            imgSurf = pg.image.load(fullPath).convert_alpha()
            surfList.append(imgSurf)
    return surfList