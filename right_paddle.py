# # By Steven Kha 2018

import pygame
pygame.init()
from pygame.sprite import Sprite

class Right_Paddle(Sprite):

    def __init__(self, ai_settings, screen):
        """Create the Right_Paddle and set its starting position."""
        super(Right_Paddle, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.rect = pygame.Rect(0, 0, ai_settings.right_paddle_width,
                                ai_settings.right_paddle_height)

        self.screen_rect = screen.get_rect()

        self.color = ai_settings.top_paddle_color

        self.height = float(ai_settings.right_paddle_height)

        #Right_Paddle starts at center right of screen
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
        #print("Reft Paddle position: " + str(self.rect))

        # Store a decimal value for the ship's center.
        self.y = float(self.rect.centery)

        self.speed_factor = ai_settings.right_paddle_speed_factor

        # Movement flag for continuous movement
        self.moving_up = False
        self.moving_down = False

    def update(self, ai_settings, balls):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        for ball in balls.sprites():
            if ball.rect.centerx > ai_settings.right_reflex:
                self.y += (ai_settings.right_paddle_y_direction *
                           ai_settings.right_paddle_speed_factor/ ai_settings.cpu_slow)

            else:
                self.y -= (ai_settings.right_paddle_y_direction *
                           ai_settings.right_paddle_speed_factor/ ai_settings.cpu_slow)

        self.rect.y = self.y

    def check_edges(self):
        if self.rect.top < 0:
            return True
        elif self.rect.bottom > 800:
            return True

    def center_right_paddle(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.midright


    def draw_right_paddle(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

# By Steven Kha 2018