#pg 266

#                      (x,   y  width, height)
# Left Paddle position: <rect(0, 267, 37, 266)>

import pygame
pygame.init()
from pygame.sprite import Sprite

class Bottom_Paddle(Sprite):

    def __init__(self, ai_settings, screen):
        """Create the Bottom_Paddle and set its starting position."""
        super(Bottom_Paddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.rect = pygame.Rect(0, 0, ai_settings.bottom_paddle_width,
                                ai_settings.bottom_paddle_height)

        self.screen_rect = screen.get_rect()

        self.color = ai_settings.bottom_paddle_color

        self.height = float(ai_settings.bottom_paddle_height)

        #Bottom_Paddle starts at the bottom center of screen
        self.rect.centerx= 300
        self.rect.bottom = self.screen_rect.bottom

        #print("Bottom Paddle position: " + str(self.rect))

        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

        # Movement flag for continuous movement
        self.moving_left = False
        self.moving_right = False

    def update(self, ai_settings):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.

        #stop paddle from going off the top edge
        # Y axis gets smaller when it goes up!
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.bottom_paddle_speed_factor
            # print("Left Paddle position: " + str(self.rect))
            # print("self.rect.top: " + str(self.rect.top) + " > "
            #     "self.screen_rect.top: " + str(self.screen_rect.top))

        # stop paddle from going off the bottom edge y axis gettings
        # bigger when it moves down! When it reaches the end it is 800
        if self.moving_right and self.rect.right < 600:
            self.center += self.ai_settings.bottom_paddle_speed_factor

            # print("self.rect.bottom: " + str(self.rect.bottom) + "< 800")
            # print("Left Paddle position: " + str(self.rect))
        # Update rect object from self.center.

        self.rect.centerx = self.center

    def center_bottom_paddle(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.midleft


    def draw_bottom_paddle(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
