from turtle import Turtle

ALIGN = "center"
FONT = ("arial",18,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.score_update

    def score_update(self):
        self.write(f"Score {self.score}",align=ALIGN,font=FONT)


    def game_over (self):
        self.goto (0,0)
        self.write("Game Over", align=ALIGN , font=FONT)



    def score_place(self):
        self.score +=1
        self.clear()
        self.score_update()
       
        

