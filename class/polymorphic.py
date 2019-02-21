class Shape:
    def draw(self):
        print("shap的draw()")

class Point(Shape):
    def draw(self):
        print("画一个点")

class Circle(Point):
    def draw(self):
        print("画一个圆")

def my_draw(s):
    s.draw()

s1 = Circle()
s2 = Point()
my_draw(s1)
my_draw(s2)