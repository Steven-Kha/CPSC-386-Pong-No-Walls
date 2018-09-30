# # By Steven Kha 2018

import pygame
from pygame.sprite import Group
from left_paddle import Left_Paddle
from right_paddle import Right_Paddle
from bottom_paddle import Bottom_Paddle
from top_paddle import Top_Paddle
from top_left import Top_Left
from bottom_right import Bottom_Right
from center_line import Center_Line


from settings import Settings
from game_stats import GameStats
from button import Button

from scoreboard import Scoreboard
from title import Title

import game_functions as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    # start_game = False
    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))

    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Super Pong 64")

    start_game = False

    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats, "")
    title = Title(ai_settings, screen, "")


    # make the left paddle
    left_paddle = Left_Paddle(ai_settings, screen)
    right_paddle = Right_Paddle(ai_settings, screen)
    bottom_paddle = Bottom_Paddle(ai_settings, screen)
    top_paddle = Top_Paddle(ai_settings, screen)
    top_left = Top_Left(ai_settings, screen)
    center_line = Center_Line(ai_settings, screen)
    bottom_right = Bottom_Right(ai_settings, screen)
    balls = Group()


    play_button = Button(ai_settings, screen, "Play")


    # Start the main loop for the game
    while True:
        title.prep_title("")
        title.prep_rules("")
        gf.check_events(ai_settings, screen, stats, sb, play_button,
                        left_paddle, top_left, bottom_paddle, balls)

        if stats.game_active:

            left_paddle.update(ai_settings)
            right_paddle.update(ai_settings, balls)
            bottom_paddle.update(ai_settings)
            top_paddle.update(ai_settings, balls)
            bottom_right.update(ai_settings, balls)
            top_left.update(ai_settings)


            gf.update_balls(ai_settings, stats, screen, sb, left_paddle,
                right_paddle, bottom_paddle, top_paddle, top_left, bottom_right, balls)

            gf.update_top_paddle(ai_settings, top_paddle)
            gf.update_bottom_right(ai_settings, bottom_right)
            gf.update_right_paddle(ai_settings, right_paddle)

        gf.update_screen(ai_settings, screen, stats, sb, title, left_paddle, right_paddle,
                 bottom_paddle, center_line, top_paddle, top_left, bottom_right,
                         balls, play_button)


run_game()

