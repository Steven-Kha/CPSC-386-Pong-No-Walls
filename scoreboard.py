# By Steven Kha 2018
import pygame.font


class Scoreboard:
    """A class to report scoring information."""
    def __init__(self, ai_settings, screen, stats, msg):
        """Initialize scorekeeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        # Font settings for scoring information.

        self.p1_color = (0,   0,   255)
        self.cpu_color = (255, 0, 0)
        self.high_color = (0, 255, 0)

        self.font = pygame.font.SysFont(None, 48)
        # Prepare the initial score image.
        
        self.prep_p1_wins(msg)
        self.prep_cpu_wins(msg)
        
        self.prep_high_score_label()
        self.prep_high_level_label()

        self.prep_p1_score_label()
        self.prep_left_level_label()
        self.prep_right_level_label()
        self.prep_cpu_score_label()

        self.prep_p1_score()
        self.prep_left_level()

        self.prep_cpu_score()
        self.prep_right_level()

        self.prep_high_score()
        self.prep_high_level()


    def prep_p1_wins(self, msg):
        winner = msg
        self.p1_wins_image = self.font.render(winner, True,
            self.p1_color, self.ai_settings.bg_color)
        self.p1_wins_rect = self.p1_wins_image.get_rect()
        self.p1_wins_rect.centerx = self.screen_rect.centerx - 20
        self.p1_wins_rect.centery = self.screen_rect.centery

    def prep_cpu_wins(self, msg):
        winner = msg
        self.cpu_wins_image = self.font.render(winner, True,
                         self.p1_color, self.ai_settings.bg_color)
        self.cpu_wins_rect = self.cpu_wins_image.get_rect()
        self.cpu_wins_rect.centerx = self.screen_rect.centerx - 20
        self.cpu_wins_rect.centery = self.screen_rect.centery - 40

    def prep_left_level_label(self):
        label_str = "Lv:"
        self.left_level_label_image = self.font.render(label_str, True,
               self.p1_color, self.ai_settings.bg_color)
        self.left_level_label_rect = self.left_level_label_image.get_rect()
        self.left_level_label_rect.centerx = self.screen_rect.centerx - 445
        self.left_level_label_rect.top = 75

    def prep_left_level(self):
        """Turn the level into a rendered image."""
        self.left_level_image = self.font.render(str(self.stats.level), True,
                                                 self.p1_color, self.ai_settings.bg_color)
        # Position the level below the score.
        self.left_level_rect = self.left_level_image.get_rect()
        self.left_level_rect.right = self.p1_score_rect.right
        self.left_level_rect.top = self.p1_score_rect.bottom + 10
        
    def prep_right_level_label(self):
        label_str = "Lv:"
        self.right_level_label_image = self.font.render(label_str, True,
               self.cpu_color, self.ai_settings.bg_color)
        self.right_level_label_rect = self.right_level_label_image.get_rect()
        self.right_level_label_rect.centerx = self.screen_rect.centerx + 350
        self.right_level_label_rect.top = 75

    def prep_right_level(self):
        """Turn the level into a rendered image."""
        self.right_level_image = self.font.render(str(self.stats.level), True,
                                                  self.cpu_color, self.ai_settings.bg_color)
        # Position the level below the score.
        self.right_level_rect = self.right_level_image.get_rect()
        self.right_level_rect.right = self.cpu_score_rect.right
        self.right_level_rect.top = self.cpu_score_rect.bottom + 10

    def prep_p1_score_label(self):
        label_str = "P1 Score: "
        self.p1_score_label_image = self.font.render(label_str, True,
                                                       self.p1_color, self.ai_settings.bg_color)
        self.p1_score_label_rect = self.p1_score_label_image.get_rect()
        self.p1_score_label_rect.centerx = self.screen_rect.centerx - 490
        self.p1_score_label_rect.top = 30
        
    def prep_p1_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.p1_score)
        self.p1_score_image = self.font.render(score_str, True, self.p1_color,
                                               self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.p1_score_rect = self.p1_score_image.get_rect()
        self.p1_score_rect.centerx = self.screen_rect.centerx - 400
        self.p1_score_rect.top = 30
        
    def prep_high_score_label(self):
        label_str = "Hi Score: "
        self.high_score_label_image = self.font.render(label_str, True,
                                                      self.high_color, self.ai_settings.bg_color)
        self.high_score_label_rect = self.high_score_label_image.get_rect()
        self.high_score_label_rect.centerx = self.screen_rect.centerx - 90
        self.high_score_label_rect.top = 30
        
    def prep_high_level_label(self):
        label_str = "Hi Lv: "
        self.high_level_label_image = self.font.render(label_str, True,
                                                      self.high_color, self.ai_settings.bg_color)
        self.high_level_label_rect = self.high_level_label_image.get_rect()
        self.high_level_label_rect.centerx = self.screen_rect.centerx - 63
        self.high_level_label_rect.top = 75
        
    def prep_cpu_score_label(self):
        label_str = "CPU Score: "
        self.cpu_score_label_image = self.font.render(label_str, True,
                                                       self.cpu_color, self.ai_settings.bg_color)
        self.cpu_score_label_rect = self.cpu_score_label_image.get_rect()
        self.cpu_score_label_rect.centerx = self.screen_rect.centerx + 290
        self.cpu_score_label_rect.top = 30

    def prep_cpu_score(self):
        """Turn the score into a rendered image."""
        score_str = str(self.stats.cpu_score)
        self.cpu_score_image = self.font.render(score_str, True, self.cpu_color,
                                                self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.cpu_score_rect = self.cpu_score_image.get_rect()
        self.cpu_score_rect.centerx = self.screen_rect.centerx + 400
        self.cpu_score_rect.top = 30

    def prep_high_level(self):
        high_level = self.stats.high_level
        high_level_str = "{:,}".format(high_level)

        self.high_level_image = self.font.render(high_level_str, True,
             self.high_color, self.ai_settings.bg_color)

        self.high_level_rect = self.high_level_image.get_rect()
        self.high_level_rect.centerx = self.high_score_rect.centerx
        self.high_level_rect.top = self.high_score_rect.bottom + 10
        # print("high level rect: " + str(self.high_level_rect))

    def prep_high_score(self):
        high_score = self.stats.high_score

        high_score_str = "{:,}".format(high_score)

        self.high_score_image = self.font.render(high_score_str, True,
             self.high_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.p1_score_rect.top
        # print("high score rect: " + str(self.high_score_rect))

    def show_score(self):
        """Draw score to the screen."""

        self.screen.blit(self.p1_score_image, self.p1_score_rect)
        self.screen.blit(self.cpu_score_image, self.cpu_score_rect)

        self.screen.blit(self.left_level_image, self.left_level_rect)
        self.screen.blit(self.right_level_image, self.right_level_rect)

        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.high_level_image, self.high_level_rect)

        self.screen.blit(self.left_level_label_image, self.left_level_label_rect)
        self.screen.blit(self.p1_score_label_image, self.p1_score_label_rect)

        self.screen.blit(self.cpu_score_label_image, self.cpu_score_label_rect)
        self.screen.blit(self.right_level_label_image, self.right_level_label_rect)
        
        self.screen.blit(self.high_score_label_image, self.high_score_label_rect)
        self.screen.blit(self.high_level_label_image, self.high_level_label_rect)

        self.screen.blit(self.p1_wins_image, self.p1_wins_rect)
        self.screen.blit(self.cpu_wins_image, self.cpu_wins_rect)


# By Steven Kha 2018