class Dog:
    '''创建一个Ｄｏｇ类，此类用于描述一种小动物的行为和属性'''

    def eat(self,food): #self绑定调用的对象
        print('eat',food)

dog1 = Dog()
#print(id(dog1))
dog1.eat('Bone')
dog1.color = 'red'
print(dog1.color)

dog2 = Dog()
dog2.eat('Dog food')
#print(id(dog2))