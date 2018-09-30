# # By Steven Kha 2018

import pygame
pygame.init()
from pygame.sprite import Sprite

class Center_Line(Sprite):

    def __init__(self, ai_settings, screen):
        """Create the left_paddle and set its starting position."""
        super(Center_Line, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.rect = pygame.Rect(0, 0, ai_settings.center_line_width,
                                ai_settings.center_line_height)

        self.screen_rect = screen.get_rect()

        self.color = ai_settings.center_line_color

        self.height = float(ai_settings.left_paddle_height)

        #left_paddle starts at center left of screen
        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        #print("Left Paddle position: " + str(self.rect))

        # # Store a decimal value for the ship's center.
        # self.center = float(self.rect.centery)
        #
        # # Movement flag for continuous movement
        # self.moving_up = False
        # self.moving_down = False

    # def update(self, ai_settings):
    #     """Update the ship's position based on the movement flag."""
    #     # Update the ship's center value, not the rect.
    #
    #     #stop paddle from going off the top edge
    #     # Y axis gets smaller when it goes up!
    #     if self.moving_up and self.rect.top > 0:
    #         self.center -= self.ai_settings.left_paddle_speed_factor
    #         # print("Left Paddle position: " + str(self.rect))
    #         # print("self.rect.top: " + str(self.rect.top) + " > "
    #         #     "self.screen_rect.top: " + str(self.screen_rect.top))
    #
    #     # stop paddle from going off the bottom edge y axis gettings
    #     # bigger when it moves down! When it reaches the end it is 800
    #     if self.moving_down and self.rect.bottom < 800:
    #         self.center += self.ai_settings.left_paddle_speed_factor
    #
    #         # print("self.rect.bottom: " + str(self.rect.bottom) + "< 800")
    #         # print("Left Paddle position: " + str(self.rect))
    #     # Update rect object from self.center.
    #
    #     self.rect.centery = self.center

    # def center_left_paddle(self):
    #     """Center the ship on the screen."""
    #     self.center = self.screen_rect.midleft


    def draw_center_line(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

# By Steven Kha 2018