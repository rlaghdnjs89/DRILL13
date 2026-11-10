from pico2d import *

import game_framework
import game_world
import item_mode
import title_mode
from boy import Boy
from grass import Grass

ITEM_NAMES = {
    None: 'No Ball',
    'SmallBall': 'Small Ball',
    'BigBall': 'Big Ball',
}

boy = None
paused = False
paused_at = 0.0
pause_font = None
hint_font = None


def toggle_pause():
    global paused, paused_at
    if not paused:
        paused = True
        paused_at = get_time()
    else:
        paused = False
        # 멈춰 있던 시간만큼 IDLE 타이머를 밀어서, 재개하자마자 잠들지 않게 함
        boy.idle_started_at += get_time() - paused_at


def handle_events():
    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            toggle_pause()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i and not paused:
            game_framework.push_mode(item_mode)
            return
        elif paused:
            # 일시정지 중에는 키를 뗀 이벤트만 전달 (방향키를 누른 채 멈췄다가 떼는 경우 처리)
            if event.type == SDL_KEYUP:
                boy.handle_event(event)
        else:
            boy.handle_event(event)


def init():
    global boy, paused, pause_font, hint_font
    paused = False

    if pause_font is None:
        pause_font = load_font('ENCR10B.TTF', 60)
        hint_font = load_font('ENCR10B.TTF', 20)

    grass = Grass()
    game_world.add_oject(grass, 0)

    boy = Boy()
    game_world.add_oject(boy, 1)


def update():
    if paused:
        return
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    hint_font.draw(10, get_canvas_height() - 20,
                   f'Item: {ITEM_NAMES[boy.item]}  (I: select)', (0, 0, 0))
    if paused:
        pause_font.draw(290, 330, 'PAUSED', (255, 255, 0))
        hint_font.draw(298, 270, 'Press P to resume', (255, 255, 255))
    update_canvas()


def finish():
    game_world.clear()


def pause():
    # 아이템 선택 창에서는 좌우로 이동할 수 없으므로, 달리던 중이면 그 자리에 멈춰 서게 함
    boy.pressed_keys.clear()
    if boy.state == 'RUN':
        boy.dir = 0
        boy.stop_run()


def resume():
    # 선택 창에 있는 동안 뗀 방향키 이벤트는 boy에게 전달되지 않았으므로 입력 상태를 초기화
    boy.pressed_keys.clear()
