
class Bicycle():

    def run(self, km):
        print('骑行了',km,'公里')

class EBicycle(Bicycle):
    def __init__(self,vol):
        self.volume = vol
        print("新买的电动车内有",vol,'度电')
    def fill_chrge(self,vol):
        self.volume += vol
        print("充电",self.volume,'度')

    def run(self, km):
        if km /10 > self.volume:
            km = (km/10-self.volume)*10
            self.volume = 0
            print('电动车骑行了', km, '千米', '还剩', self.volume, '度电')

        else:
            self.volume -= km/10
            print('电动车骑行了', km, '千米', '还剩', self.volume, '度电')

        if self.volume == 0:
            super(EBicycle,self).run(km)


b = EBicycle(5)
b.run(10)
b.run(100)
b.fill_chrge(10)
b.run(50)