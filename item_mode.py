from pico2d import *

import game_framework


def init():
    pass


def finish():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def update():
    pass


def render():
    clear_canvas()
    update_canvas()


def pause():
    pass


def resume():
    pass
