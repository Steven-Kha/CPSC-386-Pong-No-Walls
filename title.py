import pygame.sysfont

class Title:

    def __init__(self, ai_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        self.title_color = (255, 0, 0)
        self.rules_color = (0, 255, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_title(msg)
        self.prep_rules(msg)

    def prep_title(self, msg):
        title_str = msg
        self.title_image = self.font.render(title_str, True,
                    self.title_color, self.ai_settings.start_color)

        self.title_rect = self.title_image.get_rect()
        self.title_rect.centerx = self.screen_rect.centerx
        self.title_rect.centery = self.screen_rect.top + 20

    def prep_rules(self, msg):
        rules_str = msg
        self.rules_image = self.font.render(rules_str, True,
                    self.rules_color, self.ai_settings.start_color)

        self.rules_rect = self.rules_image.get_rect()
        self.rules_rect.centerx = self.screen_rect.centerx
        self.rules_rect.centery = self.screen_rect.top + 60


    def draw_button(self):
        self.screen.blit(self.title_image, self.title_rect)
        self.screen.blit(self.rules_image, self.rules_rect)
        print("Yo are you there?")