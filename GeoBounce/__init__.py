from .game import Game
from .sprites import GeoBox

import time

speed = 5

move_by = [speed, speed]

def move_box(game, box):
    if box.position[0] <= 0:
        move_by[0] = speed
    if box.position[0] + 50 >= game.dimensions[0]:
        move_by[0] = -speed
    if box.position[1] <= 0:
        move_by[1] = speed
    if box.position[1] + 50 >= game.dimensions[1]:
        move_by[1] = -speed

    box.move_by(move_by)

def main():
    game = Game("GeoBounce", dimensions=[1080, 720], resizable=[False, False])
    box = GeoBox(game._canvas, [0, 0])
    old_time = time.time()
    frame_rate = 1 / 100
    game.play()

    while True:
        if time.time() - frame_rate >= old_time:
            old_time = time.time()
        else:
            continue

        move_box(game, box)

        game.update()

if __name__ == "__main__":
    main()
