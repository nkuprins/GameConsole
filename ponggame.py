#import 

PLAYER_HEIGHT = 2
BALL_SIZE = 2
PLAYER_WIDTH = 2

class Pong:
    def __init__(self, x, y, world, player_y):
        self._ball_x_speed = -1
        self._ball_y_speed = 1
        self._ball_x = x
        self._ball_y = y
        self._world = world
        self._player_y = player_y

    def get_x(self):
        return self._ball_x
    
    def get_y(self):
        return self._ball_y
    
    def get_x_speed(self):
        return self._ball_x_speed
    
    def get_y_speed(self):
        return self._ball_y_speed
    
    def get_player_y(self):
        return self._player_y
    
    def hits_side_border(self):
        return self.get_x() >= self._world.get_width() - 1
    
    def hits_top_bottom_border(self):
        return self.get_y() >= self._world.get_height() - 1 or self.get_y() <= 0
    
    def hits_player(self):
        return self.get_x() == PLAYER_WIDTH and self.get_player_y() + PLAYER_HEIGHT >= self.get_y() and self.get_player_y() - PLAYER_HEIGHT <= self.get_y()
    
    def move(self):
        self._ball_x += self._ball_x_speed
        self._ball_y += self._ball_y_speed
        
        if self.hits_side_border():
            self._ball_x_speed *= -1
        elif self.hits_player():
            self._ball_x_speed = self._ball_x_speed * -1 + 1

        if self.hits_top_bottom_border():
            self._ball_y_speed *= -1

    def draw(self):
        for i in range(self._player_y - PLAYER_HEIGHT, self._player_y + PLAYER_HEIGHT):
            for j in range(0, PLAYER_WIDTH):
                self._bitmap[i, j] = LIGHT_GREEN

        for k in range(self.get_x(), self.get_x() + BALL_SIZE):
            for l in range(self.get_y(), self.get_y() + BALL_SIZE):
                self._bitmap[l, k] = RED

    def run(self):
        score = 0
        while True:
            self.move()
            self.draw()
            self._world.display()
            score+=1
            print(score)
            time.sleep(0.1)




    
    
    
    
    
