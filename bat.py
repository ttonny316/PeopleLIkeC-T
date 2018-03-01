import table, random

class Bat:

    def __init__(self, table, width=35, height=1, x_posn=100, y_posn=50, colour="white", x_speed=23, y_speed=23):
        self.width = width
        self.height = height
        self.x_posn = x_posn
        self.y_posn = y_posn
        self.colour = colour
        self.x_start = x_posn
        self.y_start = y_posn
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.table = table
        self.rectangle = self.table.draw_rectangle(self)

    def start_position(self):
        self.x_posn = self.x_start
        self.y_posn = self.y_start

    def detect_collision(self, ball, sides_sweet_spot=True, topnbottom_sweet_spot=False):
        collision_direction = ""
        collision = False
        feel = 5
        top = self.y_posn
        bottom = self.y_posn + self.height
        left = self.x_posn
        right = self.x_posn + self.width
        v_centre = top + (self.height/2)
        h_centre = left + (self.width/2)
        top_b = ball.y_posn
        bottom_b = ball.y_posn + ball.height
        left_b = ball.x_posn
        right_b = ball.x_posn + ball.width
        r = (right_b - left_b)/2
        v_centre_b = top_b + r
        h_centre_b = left_b + r
                        
    def move_left(self, master):
        self.x_posn = self.x_posn - self.x_speed
        if(self.x_posn <= 0):
            self.x_posn = 0
            x1 = self.x_posn
            x2 = self.x_posn+self.width
            y1 = self.y_posn
            y2 = self.y_posn+self.height
            self.table.move_item(self.rectangle, x1, y1, x2, y2)

    def move_right(self, master):
        self.x_posn = self.x_posn + self.x_speed
        far_right = self.table.width - self.width
        if(self.x_posn >= far_right):
            self.x_posn = far_right
        x1 = self.x_posn
        x2 = self.x_posn+self.width
        y1 = self.y_posn
        y2 = self.y_posn+self.height
        self.table.move_item(self.rectangle, x1, y1, x2, y2)
            




























                        
