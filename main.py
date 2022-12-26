import pygame as pg
from pointer import Pointer
from ball import Ball
from text import Text
from time import perf_counter


def main():
    w, h = 1280, 720
    clock = pg.time.Clock()

    difficulty = 10

    try:
        ball_num = int(input("enter the difficulty: "))
    except ValueError:
        print("enter a number next time")
        return

    colour = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255)
    }

    dis = pg.display.set_mode((w, h))
    pg.display.set_caption('Don\'t Touch')

    pg.mouse.set_visible(False)

    done = False

    pointer = Pointer(5, colour['black'])
    balls = [Ball(0, 0, w, h, 10, colour['red'], i) for i in range(ball_num)]

    first_time = perf_counter()
    get_harder_time = perf_counter()

    while not done:
        clock.tick(60)
        pg.display.update()
        dis.fill(colour['white'])
        mouse_pos = pg.mouse.get_pos()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return

        second_time = perf_counter()

        Text(round(second_time-first_time, 1), colour['black'], dis, w/2-25, 30)

        for ball in balls:
            if ball.collided:
                print(f"You Lived For {round(second_time-first_time, 1)} Seconds, You Were Killed By Ball Number {ball.ball_number+1}")
                return

        if second_time-get_harder_time >= difficulty:
            for ball in balls:
                ball.get_harder()
                get_harder_time = perf_counter()

        pointer.draw(dis, mouse_pos)

        for ball in balls:
            ball.move()
            ball.draw(dis)
            ball.collide(mouse_pos[0], mouse_pos[1], pointer.radius)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
