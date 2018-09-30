# By Steven Kha 2018

class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        self.start_color = (0, 0, 0)

        # ai_moves faster to ball
        self.cpu_slow = 5

        # left paddle settings
        self.left_paddle_width = self.screen_width/32
        self.left_paddle_height = self.screen_height/ 3
        self.left_paddle_color = 0, 0, 255
        self.left_paddle_speed_factor = 1.5
        self.left_paddle_limit = 3

        # center line
        self.center_line_width = 5
        self.center_line_height = self.screen_height
        self.center_line_color = 255, 255, 255

        # bottom paddle settings
        self.bottom_paddle_width = 800/2.5
        self.bottom_paddle_height = self.screen_height / 32
        self.bottom_paddle_color = 0, 0, 255
        self.bottom_paddle_speed_factor = 2
        self.bottom_paddle_limit = 1

        self.top_left_width = 800 / 2.5
        self.top_left_height = self.screen_height / 32
        self.top_left_color = 0, 0, 255
        self.top_left_speed_factor = 2
        self.top_left_limit = 1

        # top paddle settings
        self.top_paddle_width = self.screen_width/5
        self.top_paddle_height = self.screen_height / 32
        self.top_paddle_color = 255,   0,   0
        self.top_paddle_speed_factor = 2
        self.top_paddle_limit = 1
        self.top_paddle_x_direction = 1

        # bottom right settings
        self.bottom_right_width = self.screen_width/5
        self.bottom_right_height = self.screen_height / 32
        self.bottom_right_color = 255, 0, 0
        self.bottom_right_speed_factor = 2
        self.bottom_right_limit = 1
        self.bottom_right_x_direction = 1

        # right paddle settings
        self.right_paddle_width = self.screen_width / 32
        self.right_paddle_height = self.screen_height / 6
        self.right_paddle_color = 255, 0, 0,
        self.right_paddle_speed_factor = 1.5
        self.right_paddle_limit = 1
        self.right_paddle_y_direction = 1
        self.right_reflex = (self.screen_width * 3)/4

        # ball settings
        self.ball_speed_factor = .6
        self.ball_width = 15
        self.ball_height = 15
        self.ball_color = 60, 60, 60
        self.balls_allowed = 1
        self.ball_x_direction = 1
        self.ball_y_direction = 1

        # pong scoring
        self.level = 1
        self.points = 1
        self.p1_score = 1
        self.cpu_score = 1

# By Steven Kha 2018