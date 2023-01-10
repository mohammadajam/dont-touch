import pygame as pg
from time import perf_counter
from player import Player
from ball import Ball
from text import Text


def main():
    w, h = 1280, 720
    clock = pg.time.Clock()
    fps = 60
    colour = {
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }
    adding_time = 10
    
    dis = pg.display.set_mode((w, h))
    pg.display.set_caption("Don't Touch")
    
    player = Player(10, colour['black'])
    
    balls = []

    start_time = perf_counter()
    add_timer = perf_counter()

    while True:
        clock.tick(fps)
        pg.display.update()
        dis.fill(colour['white'])
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return
        current_time = perf_counter()

        if current_time-add_timer >= adding_time:
            balls.append(Ball(0, 0, w, h, 10, colour['red']))
            add_timer = perf_counter()
        
        timer = current_time-start_time
        

        player.draw(dis, mouse_pos)

        for ball in balls:
            ball.draw(dis)
            ball.move()
            if ball.collide(mouse_pos, player.radius):
                print(f"you lived for {round(timer)} seconds")
                return
        Text(round(timer), dis, w/2-10, 30, colour['black'])

if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
