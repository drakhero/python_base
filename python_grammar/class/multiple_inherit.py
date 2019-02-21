class Car:
    def run(self,speed):
        print(speed)

    def a(self,x):
        print(1,x)

class Plane:
    def fly(self,height):
        print(height)

    def a(self,x):
        print(2,x)

class PlaneCar(Car,Plane):
    pass

p = PlaneCar()
#p.fly(10000)
# p.run(300)
p.a(10)