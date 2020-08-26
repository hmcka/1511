#Pong
#Player must bounce the ball off their paddle to hit one of the three walls
#Programmed by Hethur Aluma | 4/8/20

from superwires import games, color

import random

games.init(screen_width = 640, screen_height = 480, fps = 150)

"""score = games.Text(value = 32,
                   size = 48,
                   color = color.white,
                   x = 610,
                   y = 30)
games.screen.add(score)"""

"""won_message = games.Message(value = "You won!",
                            size = 100,
                            color = color.yellow,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            lifetime = 250,
                            after_death = games.screen.quit)
games.screen.add(won_message)"""

"""gameover_message = games.Message(value = "Game Over :-(",
                            size = 100,
                            color = color.yellow,
                            x = games.screen.width/2,
                            y = games.screen.height/2,
                            lifetime = 850,
                            after_death = games.screen.quit)
games.screen.add(gameover_message)"""

#paddle_image = games.load_image("paddle.png")
#paddle = games.Sprite(image = paddle_image, x = 60, y = 240)
#games.screen.add(paddle)

class Ball(games.Sprite):
    """A bouncing ball"""
    image = games.load_image("ball.png")
    speed = 1

    def __init__(self, x = 140, y = 140):
        """Initializing a ball object"""
        super(Ball, self).__init__(image = Ball.image,
                                   x = 600, y = 240,
                                   dx = -3, dy = 1)
    
    def update(self):
        """Reverse a velocity component if the edge of screen is reached"""
        if self.right > games.screen.width: #or self.left < 0:
            self.dx = -self.dx

        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy

        self.handle_collide()

        if self.left < 60:
            self.end_game()

    def handle_collide(self):
        """Reverse a velocity if the paddle is hit"""
        if self.get_overlapping_sprites():
            self.dx = -self.dx

    def end_game(self):
        """End the game"""
        end_message = games.Message(value = "Game Over",
                                    size = 90,
                                    color = color.red,
                                    x = games.screen.width/2,
                                    y = games.screen.width/2 - 100,
                                    lifetime = 5 * games.screen.fps,
                                    after_death = games.screen.quit)
        games.screen.add(end_message)

class Paddle(games.Sprite):
    """A paddle controlled by the mouse"""
    image = games.load_image("paddle.png")

    def __init__(self):
        """Initializing paddle object"""
        super(Paddle, self).__init__(image = Paddle.image,
                        x = games.mouse.x,
                        y = games.mouse.y)

        self.score = games.Text(value = 0, size = 25, color = color.white,
                            top = 20, right = games.screen.width - 10)
        games.screen.add(self.score)
                                  
    def update(self):
        """Move to mouse coordinates"""
        self.x = 60
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        """Check for collision with ball"""
        for paddle in self.overlapping_sprites:
            self.score.value +=10

def main():
    wall_image = games.load_image("background.png", transparent = False)
    games.screen.background = wall_image

    the_ball = Ball()
    games.screen.add(the_ball)

    the_paddle = Paddle()
    games.screen.add(the_paddle)

    games.mouse.is_visible = False

    games.screen.event_grab = True

    games.screen.mainloop()

#kick it off
main()

