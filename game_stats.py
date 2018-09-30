# By Steven Kha 2018

class GameStats:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False
        self.start_game = False

        # When below wins, the message will display
        self.P1_WINS = False
        self.CPU_WINS = False

        self.score = 0
        self.p1_score = 0
        self.cpu_score = 0

        # use this for left and right level on the scoreboard
        self.level = 1

        # High score should never be reset.
        self.high_score = 0
        self.high_level = 1

    def reset_stats(self):
        self.left_paddle_left = self.ai_settings.left_paddle_limit

# By Steven Kha 2018