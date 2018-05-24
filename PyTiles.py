import pygame
import random
import time

pygame.init()

display_width = 600
display_height = 800

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
grey = (100, 100, 100)

gap = 2
tile_width = (display_width - 10) / 4
tile_height = display_height * 0.25 - gap  # tile_width * 1.5
grid = [gap,
        (tile_width + gap * 2),
        (tile_width * 2 + gap * 3),
        (tile_width * 3 + gap * 4)]

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Py Tiles")
clock = pygame.time.Clock()


class Tiles:
    posy = -tile_height
    posx = random.choice(grid)
    pressed = False

    def tile(self):

        if self.pressed is True:
            color = grey
        else:
            color = black

        pygame.draw.rect(gameDisplay, color, [self.posx, self.posy, tile_width, tile_height])


def quitgame():
    pygame.quit()
    quit()


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def text(x, y, message, size, type, color):
    font = pygame.font.Font(type, size)
    text_surf, text_rect = text_objects(message, font, color)
    text_rect.center = (x, y)
    gameDisplay.blit(text_surf, text_rect)


def button(msg, x, y, width, height, icolor, acolor, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, acolor, (x, y, width, height))
        if click[0] == 1:  # and action is not None
            action()

    else:
        pygame.draw.rect(gameDisplay, icolor, (x, y, width, height))

    text((x + (width / 2)), (y + (height / 2)), msg, 20, "resources/FreeSansBold.ttf", white)


def gameover():
    text((display_width / 2), (display_height / 2), "Game Over", 100, "resources/ARCADE.TTF", red)
    pygame.display.update()
    time.sleep(2)
    game()


def start_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        gameDisplay.fill(white)
        text((display_width / 2), (display_height / 2 - 50), "Py Tiles", 115, "resources/ARCADE.TTF", black)
        button("Go!", (display_width / 2 - 75), (display_height * 0.65), 150, 50, black, grey, game)
        button("Exit", (display_width / 2 - 75), (display_height * 0.75), 150, 50, black, grey, quitgame)

        pygame.display.update()
        clock.tick(15)


def game():
    tile1 = Tiles()
    tile2 = Tiles()
    tile3 = Tiles()
    tile4 = Tiles()
    tile5 = Tiles()
    tile_list = [tile1, tile2, tile3, tile4, tile5]
    mult = 1
    accelerator = 1

    for tile in tile_list:
        tile.posx = random.choice(grid)
        tile.posy += -tile_height * mult - gap * (mult + 1)
        mult += 1

    tile_speed = 6
    score = 0

    while True:

        tileposy_list = []

        for tile in tile_list:

            if tile.pressed is False:
                tileposy_list.append(tile.posy)

        tileposy_list.sort()
        tileposy_list.reverse()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:

                if not tileposy_list:
                    pass

                else:
                    if event.key == pygame.K_h:
                        if tile1.posx == grid[0] and tile1.posy == tileposy_list[0]:
                            tile1.pressed = True
                            score += 1

                        elif tile2.posx == grid[0] and tile2.posy == tileposy_list[0]:
                            tile2.pressed = True
                            score += 1

                        elif tile3.posx == grid[0] and tile3.posy == tileposy_list[0]:
                            tile3.pressed = True
                            score += 1

                        elif tile4.posx == grid[0] and tile4.posy == tileposy_list[0]:
                            tile4.pressed = True
                            score += 1

                        elif tile5.posx == grid[0] and tile5.posy == tileposy_list[0]:
                            tile5.pressed = True
                            score += 1

                        else:
                            gameover()

                    if event.key == pygame.K_j:
                        if tile1.posx == grid[1] and tile1.posy == tileposy_list[0]:
                            tile1.pressed = True
                            score += 1

                        elif tile2.posx == grid[1] and tile2.posy == tileposy_list[0]:
                            tile2.pressed = True
                            score += 1

                        elif tile3.posx == grid[1] and tile3.posy == tileposy_list[0]:
                            tile3.pressed = True
                            score += 1

                        elif tile4.posx == grid[1] and tile4.posy == tileposy_list[0]:
                            tile4.pressed = True
                            score += 1

                        elif tile5.posx == grid[1] and tile5.posy == tileposy_list[0]:
                            tile5.pressed = True
                            score += 1

                        else:
                            gameover()

                    if event.key == pygame.K_k:
                        if tile1.posx == grid[2] and tile1.posy == tileposy_list[0]:
                            tile1.pressed = True
                            score += 1

                        elif tile2.posx == grid[2] and tile2.posy == tileposy_list[0]:
                            tile2.pressed = True
                            score += 1

                        elif tile3.posx == grid[2] and tile3.posy == tileposy_list[0]:
                            tile3.pressed = True
                            score += 1

                        elif tile4.posx == grid[2] and tile4.posy == tileposy_list[0]:
                            tile4.pressed = True
                            score += 1

                        elif tile5.posx == grid[2] and tile5.posy == tileposy_list[0]:
                            tile5.pressed = True
                            score += 1

                        else:
                            gameover()

                    if event.key == pygame.K_l:
                        if tile1.posx == grid[3] and tile1.posy == tileposy_list[0]:
                            tile1.pressed = True
                            score += 1

                        elif tile2.posx == grid[3] and tile2.posy == tileposy_list[0]:
                            tile2.pressed = True
                            score += 1

                        elif tile3.posx == grid[3] and tile3.posy == tileposy_list[0]:
                            tile3.pressed = True
                            score += 1

                        elif tile4.posx == grid[3] and tile4.posy == tileposy_list[0]:
                            tile4.pressed = True
                            score += 1

                        elif tile5.posx == grid[3] and tile5.posy == tileposy_list[0]:
                            tile5.pressed = True
                            score += 1

                        else:
                            gameover()

        gameDisplay.fill(white)

        for tile in tile_list:
            tile.tile()
            tile.posy += tile_speed

        text(35, 15, "Score: " + str(score), 15, "resources/FreeSansBold.ttf", red)

        for tile in tile_list:

            if tile.posy > display_height:
                if tile.pressed is not True:
                    gameover()
                else:
                    tile_index = tile_list.index(tile)
                    tile.posy = tile_list[tile_index - 1].posy - tile_height - gap
                    tile.posx = random.choice(grid)
                    tile.pressed = False
                    if score < 20:
                        continue
                    elif score % 20 == 0:
                        tile_speed += accelerator

        text((grid[0] + (tile_width / 2)), (display_height - 30), "H", 30, "resources/FreeSansBold.ttf", black)
        text((grid[1] + (tile_width / 2)), (display_height - 30), "J", 30, "resources/FreeSansBold.ttf", black)
        text((grid[2] + (tile_width / 2)), (display_height - 30), "K", 30, "resources/FreeSansBold.ttf", black)
        text((grid[3] + (tile_width / 2)), (display_height - 30), "L", 30, "resources/FreeSansBold.ttf", black)

        pygame.display.update()
        clock.tick(60)


start_menu()
