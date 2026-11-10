from pico2d import *

import game_framework
import game_world
import play_mode

# 0: 공 없음, 1: 작은 공, 2: 큰 공
ITEM_KEYS = {
    SDLK_0: None,
    SDLK_1: 'SmallBall',
    SDLK_2: 'BigBall',
}

image = None


def init():
    global image
    image = load_image('item_select.png')


def finish():
    global image
    del image
    image = None


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            # 아무것도 바꾸지 않고 플레이 모드로 돌아간다
            game_framework.pop_mode()
            return
        elif event.type == SDL_KEYDOWN and event.key in ITEM_KEYS:
            play_mode.boy.item = ITEM_KEYS[event.key]
            game_framework.pop_mode()
            return


def update():
    pass


def render():
    clear_canvas()
    # 뒤에 멈춰 있는 플레이 화면을 그대로 그리고, 그 위에 선택 창을 띄운다
    game_world.render()
    image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()


def pause():
    pass


def resume():
    pass
