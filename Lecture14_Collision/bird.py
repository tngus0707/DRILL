import game_framework
import random
from pico2d import *

import game_world

# Bird Run Speed
PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
RUN_SPEED_KMPH = 25.0  # 25Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class Bird:
    # def __init__(self):
    #     self.x, self.y = 1600 // 2, 200
    #     self.image = load_image('bird100x100x14.png')
    #     self.dir = 1
    #     self.velocity = 0
    #     self.frame = 0
    #
    # def do(bird):
    #     # boy.frame = (boy.frame + 1) % 8
    #     bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
    #     bird.x += bird.velocity * game_framework.frame_time
    #     bird.x = clamp(25, bird.x, 1600 - 25)
    #
    # def update(self):
    #     self.x -= self.fall_speed * game_framework.frame_time

    def __init__(self):
        self.frame = 0
        self.image = load_image('bird100x100x14.png')
        self.image2 = load_image('bird100x100x14_2.png')
        self.x, self.y = random.randint(0, 1600-1), 150

    def do(bird):
        bird.frame = (bird.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):

        if(self.x < 1500):
            self.x += 5
        if (self.x > 1500):
            self.x -= 5

    def draw(bird):
        bird.image.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)
        bird.frame = (bird.frame + 1) % 14
        if(bird.x > 1500):
            bird.image2.clip_draw(int(bird.frame) * 100, 0, 100, 100, bird.x, bird.y)
            bird.frame = (bird.frame + 1) % 14




