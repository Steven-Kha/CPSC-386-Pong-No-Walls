# By Steven Kha 2018

import sys
import pygame
from ball import Ball
import random

def check_high_scores(stats, sb):
    """Check to see if there's a new high score."""

    if stats.level >= stats.high_level:
        stats.high_level = stats.level
        if stats.p1_score > stats.high_score:
            stats.high_score = stats.p1_score
            print("high level: " + str(stats.high_level))
            print("high score: " + str(stats.high_score))
    sb.prep_high_score()
    sb.prep_high_level()

def check_ball_edges(ai_settings, balls):
    # step 1 make sure it bounces from left and right
    # step 2 make sure it doesn't bounch from the left
    # step 3 make sure it bounces when it collides with the paddle

    for ball in balls.sprites():
        if ball.check_edges_horizontal():
            change_ball_direction_horizontal(ai_settings, balls)
            break
        elif ball.check_edges_vertical():
            change_ball_direction_vertical(ai_settings, balls)
            break

def check_top_paddle_edges(ai_settings, top_paddle):
    if top_paddle.check_edges():
        # top_paddle.rect.x += ai_settings.top_paddle_speed_factor
        ai_settings.top_paddle_x_direction *= -1

def check_bottom_right_edges(ai_settings, bottom_right):
    if bottom_right.check_edges():
        # bottom_right.rect.x += ai_settings.bottom_right_speed_factor
        ai_settings.bottom_right_x_direction *= -1

def check_right_edges(ai_settings, right_paddle):
    if right_paddle.check_edges():
        # right_paddle.rect.y += ai_settings.right_paddle_speed_factor
        ai_settings.right_paddle_y_direction *= -1

def change_ball_direction_horizontal(ai_settings, balls):
    ''' The ball should only change horizontal direction if it touches the left or
    right side of the screen'''
    for ball in balls.sprites():
        # print("Number of balls.sprites: " + str(balls.sprites))
        ball.rect.x += ai_settings.ball_speed_factor
    ai_settings.ball_x_direction *= -1

def change_ball_direction_vertical(ai_settings, balls):
    for ball in balls.sprites():
        # print("Number of balls.sprites: " + str(balls.sprites))
        ball.rect.y -= ai_settings.ball_speed_factor
    ai_settings.ball_y_direction *= -1

def update_top_paddle(ai_settings, top_paddle):
    check_top_paddle_edges(ai_settings, top_paddle)

def update_bottom_right(ai_settings, bottom_right):
    check_bottom_right_edges(ai_settings, bottom_right)

def update_right_paddle(ai_settings, right_paddle):
    check_right_edges(ai_settings, right_paddle)

def update_balls(ai_settings, stats, screen, sb, left_paddle, right_paddle,
                 bottom_paddle, top_paddle, top_left, bottom_right, balls):
    # check the edges first to see if balls need to change directions
    # check_ball_edges(ai_settings, balls)
    """Update position of balls and get rid of old balls."""
    # Update balls positions.
    balls.update(ai_settings)

    if len(balls) == 0:
        sb.prep_cpu_wins("Press Space")
    # sb.prep_p1_wins("")
    for ball in balls.copy():
        # remove the ball if it hits the left side of the screen
        if ball.rect.left <= 0 or ball.rect.top <= 0 \
                and ball.rect.left < 600 or ball.rect.bottom >= 800\
                and ball.rect.left < 600:

            pygame.mixer.init()
            pygame.mixer.music.load('music\MetalClang.wav')
            pygame.mixer.music.play()
            x = random.randint(1, 2)
            if x % 2 == 0:
                change_ball_direction_horizontal(ai_settings, balls)
                change_ball_direction_vertical(ai_settings, balls)

            stats.cpu_score += 1
            sb.prep_cpu_score()
            balls.remove(ball)
            if stats.cpu_score > 4:
                sb.prep_cpu_wins("CPU WINS!")
                stats.cpu_score = 0
                stats.p1_score = 0
                stats.level = 1
                ai_settings.ball_speed_factor = .5
                ai_settings.top_paddle_speed_factor = 2
                ai_settings.bottom_paddle_speed_factor = 2
                ai_settings.top_left_speed_factor = 2
                ai_settings.bottom_right_speed_factor = 2
                ai_settings.cpu_slow = 5
                stats.game_active = False
                pygame.mouse.set_visible(True)

        # when cpu loses the ball
        elif ball.rect.right >= 1200 or ball.rect.right > 600\
                and ball.rect.top <= 0 or ball.rect.right > 600\
                and ball.rect.bottom >= 800:

            # init player won
            pygame.mixer.init()
            pygame.mixer.music.load('music\MetalClang.wav')
            pygame.mixer.music.play()

            x = random.randint(1, 2)
            if x % 2 == 0:
                change_ball_direction_horizontal(ai_settings, balls)
                change_ball_direction_vertical(ai_settings, balls)

            stats.p1_score += 1
            sb.prep_p1_score()
            balls.remove(ball)
            if stats.p1_score > 4:

                if ai_settings.cpu_slow > 0:
                    ai_settings.cpu_slow -= 1
                stats.level += 1
                sb.prep_p1_wins("P1 WINS!")
                if stats.level % 5 == 0:

                    ai_settings.top_paddle_speed_factor += .2
                    ai_settings.bottom_paddle_speed_factor += .2
                    ai_settings.top_left_speed_factor += .2
                    ai_settings.bottom_right_speed_factor += .2
                    print("Increase CPU speed!")
                    print("top paddle speed: " + str(ai_settings.top_paddle_speed_factor))

                sb.prep_left_level()
                sb.prep_right_level()
                stats.p1_score = 0
                sb.prep_p1_score()
                stats.cpu_score = 0
                sb.prep_cpu_score()

                if ai_settings.ball_speed_factor < 1.0:
                    ai_settings.ball_speed_factor += .1
                else:
                    ai_settings.ball_speed_factor += .02
                stats.high_score = 0

        check_high_scores(stats, sb)


    # check if ball hits the left or right paddle
    for ball in balls.sprites():
        if ball.collision_left_right(stats, sb, left_paddle, right_paddle):
            # print("it works - collided!")
            change_ball_direction_horizontal(ai_settings, balls)


    # chceck if ball hits the top or bottom paddle
    for ball in balls.sprites():
        if ball.collision_top_bottom(top_paddle, bottom_paddle, top_left, bottom_right):
            change_ball_direction_vertical(ai_settings, balls)

def check_keydown_events(event, ai_settings, screen, left_paddle,
         top_left, bottom_paddle, balls, sb):
    """Respond to keypresses."""
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        left_paddle.moving_up = True
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        left_paddle.moving_down = True

    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        bottom_paddle.moving_left = True
        top_left.moving_left = True
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        bottom_paddle.moving_right = True
        top_left.moving_right = True

    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add it to the bullets group.
        sb.prep_p1_wins("")
        sb.prep_cpu_wins("")
        if len(balls) < ai_settings.balls_allowed:
            new_ball = Ball(ai_settings, screen, left_paddle)
            # print("shooting ball(s)!" + str(len(balls)))
            balls.add(new_ball)

def check_events(ai_settings, screen, stats, sb, play_button,
         left_paddle, top_left, bottom_paddle, balls):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen,
                 left_paddle, top_left, bottom_paddle, balls, sb)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, left_paddle, top_left, bottom_paddle)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button,
                    left_paddle, balls, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, sb, play_button,
    left_paddle, balls, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Reset the game statisitcs
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images
        stats.cpu_score = 0
        stats.p1_score = 0
        sb.prep_p1_score()
        sb.prep_cpu_score()
        sb.prep_high_score()
        sb.prep_left_level()
        sb.prep_right_level()
        sb.prep_high_level()

def update_screen(ai_settings, screen, stats, sb, left_paddle, right_paddle,
                  bottom_paddle, center_line, top_paddle, top_left, bottom_right,
                  balls, play_button):
    # Redraw the screen during each pass through the loop.

    screen.fill(ai_settings.bg_color)

    center_line.draw_center_line()

    left_paddle.draw_left_paddle()

    right_paddle.draw_right_paddle()

    bottom_paddle.draw_bottom_paddle()

    top_paddle.draw_top_paddle()

    top_left.draw_top_left()

    bottom_right.draw_bottom_right()

    for ball in balls.sprites():
        ball.draw_ball()

    # Draw the score information.
    sb.show_score()


    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    pygame.display.flip()

def check_keyup_events(event, left_paddle, top_left, bottom_paddle):
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        left_paddle.moving_up = False
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        left_paddle.moving_down = False
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        bottom_paddle.moving_left = False
        top_left.moving_left = False
    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        bottom_paddle.moving_right = False
        top_left.moving_right = False

# By Steven Kha 2018
