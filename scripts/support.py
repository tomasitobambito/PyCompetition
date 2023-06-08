from os import walk
import pygame as pg

def import_folder(path):
    """Returns a list of surfaces for a given animation state, given the folder these images are located in.

    Args:
        path (str): Path to the folder with the animation frames. 

    Returns:
        [pygame.surface]: List of animation frames as pygame surfaces. 
    """    
    surfList = []
    for _, __, imgFiles in walk(path):
        for img in imgFiles:
            fullPath = f'{path}/{img}'
            imgSurf = pg.image.load(fullPath).convert_alpha()
            surfList.append(imgSurf)
    return surfList

def draw_text(surf, text, color, rect, font):
    """Function to draw center aligned multiline text. Cuts off all text that does not fit.

    Args:
        surf (pygame.surface.Surface): Surface to draw text onto.
        text (str): Text to draw.
        color ((int, int, int)): Color of the text.
        rect (pygame.rect.Rect): Rect limiting where text will be drawn.
        font (py.font.Font): Font to render the text with. 
    """    
    lineSpacing = -2
    spaceWidth = font.size(' ')[0]
    textHeight = font.size('Tg')[1]
    words = text.split(' ')

    images = [font.render(word, False, color) for word in words]

    maxLength = rect.w
    lineLengths = [0]
    lines = [[]]

    # split text into several lines and calculate their widths
    for image in images:
        width = image.get_width()
        lineLength = lineLengths[-1] + len(lines[-1]) * spaceWidth + width
        if len(lines[-1]) == 0 or lineLength <= maxLength:
            lineLengths[-1] += width
            lines[-1].append(image)
        else:
            lineLengths.append(width)
            lines.append([image])
    
    lineBottom = rect.y
    lastLine = 0

    # align each line to the center of the screen and draw
    for lineLength, lineImages in zip(lineLengths, lines):
        lineLeft = rect.x
        lineLeft += (rect.w - lineLength - (spaceWidth * (len(lineImages)) - 1)) // 2

        if lineBottom + textHeight > rect.y + rect.h:
            break
        lastLine += 1
        for i, image in enumerate(lineImages):
            x, y = lineLeft + (i * spaceWidth), lineBottom
            surf.blit(image, (round(x), y))
            lineLeft += image.get_width()
        
        lineBottom += textHeight + lineSpacing

def create_map(tileSet):
    images = []
    currentRow = []
    for i in range(len(tileSet)):
        for j in range(len(tileSet[i])):
            currentImage = pg.image.load(f"../graphics/map/{tileSet[i][j]}.png").convert_alpha()

            if i == 0 and j != 0:
                currentImage = pg.transform.rotate(currentImage, -90)
            elif j == len(tileSet[i]) - 1:
                currentImage = pg.transform.rotate(currentImage, 180)
            elif i == len(tileSet) - 1:
                currentImage = pg.transform.rotate(currentImage, 90)
          

            currentRow.append(currentImage)
        images.append(currentRow)
        currentRow = []
    
    return images