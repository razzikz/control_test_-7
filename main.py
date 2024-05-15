from tkinter import *
from abc import abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, x, y, r, color):
        self.r = r
        self.x = x + 250
        self.y = y + 250
        self.color = color

    def area(self):
        return self.r ** 2 * 3.14

    def create_circle(self):
        canvas.create_oval(self.x-self.r, self.y-self.r,
                           self.x+self.r, self.y+self.r,
                           fill=self.color)
        canvas.create_text(self.x, self.y, text=f"{round(self.area(), 1)}", fill="black")


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a  * self.b


root = Tk()
root.title("Circle")
root.geometry("600x400")
root.resizable(width=False, height=False)

canvas = Canvas(bg="white", width=600, height=400)
canvas.pack(anchor=CENTER, expand=1)

circle1, circle2 = Circle(10, 20, 50, "#ff0000"), Circle(80, 90, 10, "#008000")
circle1.create_circle()
circle2.create_circle()

rect = Rectangle(int(input("a: ")), int(input("b: ")))

print(f"Area rectangle: {rect.area()}")

root.mainloop()