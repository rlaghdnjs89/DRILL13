from pico2d import get_canvas_width, load_image

import game_world

BALL_IMAGE_FILES = {
    'SmallBall': 'ball21x21.png',
    'BigBall': 'ball41x41.png',
}


class Ball:
    images = {}

    def __init__(self, x, y, velocity, kind='SmallBall'):
        if kind not in Ball.images:
            Ball.images[kind] = load_image(BALL_IMAGE_FILES[kind])
        self.image = Ball.images[kind]
        self.kind = kind
        self.x, self.y = x, y
        self.velocity = velocity

    def update(self):
        self.x += self.velocity
        if self.x < 0 or self.x > get_canvas_width():
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)
