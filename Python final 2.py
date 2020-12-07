from graphics import *
from random import *
from time import *
from math import sqrt

win = GraphWin("My Program", 600, 600)
win.setBackground("springgreen3")

holidays = Text(Point(300, 100), "Happy Holidays!!!")
holidays.setStyle("bold italic")
holidays.draw(win)


class mycircle:
    circle = ""
    vel_x = 0
    vel_y = 0
    circle_fill = ""
    circle_outline = ""

    def __init__(self, circle, vel_x, vel_y, circle_fill, circle_outline):
        self.circle = circle
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.circle.setFill(circle_fill)
        self.circle.setOutline(circle_outline)
        self.circle.draw(win)


circle1 = mycircle(Circle(Point(100, 100), 30), randint(-8,8), randint(-8,8), "tan2", "red")
circle2 = mycircle(Circle(Point(300, 200), 30), randint(-8,8), randint(-8,8), "tan2", "red")
circle3 = mycircle(Circle(Point(400, 300), 30), randint(-8,8), randint(-8,8), "tan2", "red")
circle4 = mycircle(Circle(Point(500, 400), 30), randint(-8,8), randint(-8,8), "red2", "red")
circle5 = mycircle(Circle(Point(300, 500), 30), randint(-8,8), randint(-8,8), "red2", "red")
circle6 = mycircle(Circle(Point(150, 250), 30), randint(-8,8), randint(-8,8),  "red2", "red")
circle7 = mycircle(Circle(Point(25, 250), 30), randint(-8,8), randint(-8,8), "green", "red")
circle8 = mycircle(Circle(Point(350, 35), 30), randint(-8,8), randint(-8,8), "green", "red")
circle9 = mycircle(Circle(Point(45, 450), 30), randint(-8,8), randint(-8,8), "green", "red")

allcircles = [circle1, circle2, circle3, circle4, circle5, circle6, circle7, circle8, circle9]

key = win.checkKey()
while key == "":

    for c in allcircles:
        c.circle.move(c.vel_x, c.vel_y)
        sleep(0.000000001)

        find_center = c.circle.getCenter()
        center_x = find_center.getX()
        center_y = find_center.getY()

        if ((center_x - 30) <= 0) or ((center_x + 30) >= 600):
            c.vel_x = -c.vel_x

        if ((center_y - 30) <= 0) or ((center_y + 30) >= 600):
            c.vel_y = -c.vel_y

        def circleDistance(cir1, cir2):
            center1 = cir1.getCenter()
            center2 = cir2.getCenter()
            x1 = center1.getX()
            y1 = center1.getY()
            x2 = center2.getX()
            y2 = center2.getY()
            dist = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))
            return dist

        newlist = allcircles.copy()
        newlist.remove(c)

        for d in newlist:
            if circleDistance(d.circle, c.circle) <= 60:
                d.vel_x = -d.vel_x
                d.vel_y = -d.vel_y
                #c.vel_x = -c.vel_x
                #.vel_y = -c.vel_y

    key = win.checkKey()
