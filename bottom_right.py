# By Steven Kha 2018

import pygame
pygame.init()
from pygame.sprite import Sprite

class Bottom_Right(Sprite):

    def __init__(self, ai_settings, screen):
        """Create the Top_Paddle and set its starting position."""
        super(Bottom_Right, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.rect = pygame.Rect(0, 0, ai_settings.bottom_right_width,
                                ai_settings.bottom_right_height)

        self.screen_rect = screen.get_rect()

        self.color = ai_settings.bottom_right_color

        self.height = float(ai_settings.bottom_right_height)

        #Top_Paddle starts at top center of screen
        self.rect.centerx = 900
        self.rect.bottom = self.screen_rect.bottom

        # print("Top Paddle position: " + str(self.rect))

        # Store a decimal value for the ship's center.
        self.x = float(self.rect.x)

        self.speed_factor = ai_settings.bottom_right_speed_factor

        # Movement flag for continuous movement
        self.moving_right = False
        self.moving_left = False

    def update(self, ai_settings, balls):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        for ball in balls.sprites():
                if ball.rect.centerx + ai_settings.cpu_slow > self.rect.centerx:
                    self.x += (ai_settings.bottom_right_x_direction *
                               ai_settings.bottom_right_speed_factor)
                else:
                    self.x -= (ai_settings.bottom_right_x_direction *
                               ai_settings.bottom_right_speed_factor)

        self.rect.x = self.x

    def center_bottom_right(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.midright

    def check_edges(self):
        if self.rect.left <= 600:
            return True
        elif self.rect.right >= 1200:
            return True

    def draw_bottom_right(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

# By Steven Kha 2018
