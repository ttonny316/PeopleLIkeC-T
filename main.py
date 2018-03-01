from tkinter import *
import table, ball, bat, random

window = Tk()
window.title("MyBreakout")
my_table = table.Table(window)

x_velocity = 4
y_velocity = 10
first_serve = True

my_ball = ball.Ball(table=my_table, x_speed=x_velocity, y_speed=y_velocity,
                    width=24, height=24, colour="red", x_start=288, y_start=188)

bat_B = bat.Bat(table = my_table, width=100, height=10,
               x_posn=250, y_posn=370, colour="blue")

bricks = []
b=1
while b < 7:
    i=80
    bricks.append(bat.Bat(table = my_table, width=50, height=20,
                          x_posn=(b*i), y_posn=75, colour="green"))
    b = b+1

def game_flow():
    global first_serve

    if(first_serve==True):
        my_ball.stop_ball()
        first_Serve = False

    bat_B.detect_collision(my_ball, sides_sweet_spot=False, topnbottom_sweet_spot=True)

    for b in bricks:
        if(b.detect_collision(my_ball, sides_sweet_spot=False) != None):
            my_table.remove_item(b.rectangle)
            bricks.remove(b)
        if(len(bricks) == 0):
            my_ball.stop_ball()
            my_ball.start_position()
            my_table.draw_score("", " YOU WIN!")

    if(my_ball.y_posn >= my_table.height - my_ball.height):
        my_ball.stop_ball()
        my_ball.start_position()
        first_serve = True
        my_table.draw_score("", " WHOOPS!")

    my_ball.move_next()
    window.after(50, game_flow)

def restart_game(master):
        my_ball.start_ball(x_speed=x_velocity, y_speed=y_velocity)
        my_table.draw_score("", "")

window.bind("<Left>", bat_B.move_left)
window.bind("<Right>", bat_B.move_right)

game_flow()
window.mainloop()

