import pygame
from pygame.sprite import Sprite
class Ball(Sprite):
    """A class to manage balls fired from the left_paddle"""
    def __init__(self, ai_settings, screen, left_paddle):
        """Create a ball object at the left_paddle's current position."""
        super(Ball, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Create a ball rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.ball_width,
            ai_settings.ball_height)


        # self.rect.centery = self.screen_rect.centery
        # self.rect.left = self.screen_rect.left

        # self.rect.midright = self.screen_rect.midright

        self.rect.centery = self.screen_rect.centery
        self.rect.centerx = self.screen_rect.centerx
        # self.rect.centery = left_paddle.rect.centery
        # self.rect.centerx = left_paddle.rect.centerx
        # Do we need the x axis too?



        # Store the ball's position as a decimal value.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.color = ai_settings.ball_color
        self.speed_factor = ai_settings.ball_speed_factor

    def collision_left_right(self, stats, sb, left_paddle, right_paddle):
        # if self.ball.rect.colliderect(self.paddle.rect):
        if self.rect.colliderect(left_paddle.rect):
            return True
        if self.rect.colliderect(right_paddle.rect):
            return True

    def collision_top_bottom(self, top_paddle, bottom_paddle, top_left, bottom_right):
        if self.rect.colliderect(top_paddle.rect):
            return True
        if self.rect.colliderect(bottom_paddle.rect):
            return True
        if self.rect.colliderect(top_left.rect):
            return True
        if self.rect.colliderect(bottom_right):
            return True


    def check_edges_horizontal(self):
        """Return True if alien is at edge of screen."""
        # step 1 let the balls bounce from left and ride
        # step 2 ball should not bounce from left
        # step 3 ball should bounce from the paddle
        # step 4 ball should bounce from left and right
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def check_edges_vertical(self):
        if self.rect.bottom >= 800:
            return True
        elif self.rect.top <= 0:
            return True

    # def change_ball_direction_horizontal(self, ai_settings):
    #     ''' The ball should only change horizontal direction if it touches the left or
    #     right side of the screen'''
    #     self.rect.x += ai_settings.ball_speed_factor
    #     ai_settings.ball_x_direction *= -1
    #
    # def change_ball_direction_vertical(self, ai_settings):
    #
    #     self.rect.y -= ai_settings.ball_speed_factor
    #     ai_settings.ball_y_direction *= -1

    def update(self, ai_settings):
        """Move the ball up the screen."""
        # Update the decimal position of the ball.
        # step 1: focus on moving the ball to the right
        # step 2: focus on moving the ball to the top-right
        self.x += (ai_settings.ball_x_direction * ai_settings.ball_speed_factor)
        self.y -= (ai_settings.ball_y_direction * ai_settings.ball_speed_factor)
        # Update the rect position.
        self.rect.x = self.x
        self.rect.y = self.y

        # print("ball x direction: " + str(self.x))
    
    def draw_ball(self):
        """Draw the ball to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)



